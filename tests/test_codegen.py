from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest

from tools import sdk_codegen
from tools.sdk_codegen import (
    build_diff_summary,
    collect_resources,
    fetch_openapi,
    load_json,
    load_overrides,
    normalize_spec,
)

RAW_SPEC_PATH = Path("openapi/public-api.json")
OVERRIDES_PATH = Path("openapi/sdk_overrides.yaml")


@pytest.fixture
def mock_openapi_fetch(monkeypatch):
    outcomes = []
    requests = []
    delays = []

    def handle(request):
        requests.append(request)
        outcome = outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    client_type = httpx.Client
    monkeypatch.setattr(
        sdk_codegen.httpx,
        "Client",
        lambda **kwargs: client_type(transport=httpx.MockTransport(handle), **kwargs),
    )
    monkeypatch.setattr(sdk_codegen.time, "sleep", delays.append)
    return outcomes, requests, delays


@pytest.mark.parametrize("timeout_type", [httpx.ConnectTimeout, httpx.ReadTimeout])
@pytest.mark.parametrize("timeouts_before_success", [0, 1, 2])
def test_fetch_openapi_recovers_from_temporary_timeouts(
    mock_openapi_fetch, timeout_type, timeouts_before_success
):
    outcomes, requests, delays = mock_openapi_fetch
    spec = {"openapi": "3.0.3", "paths": {}}
    outcomes.extend(
        timeout_type("Temporary timeout") for _ in range(timeouts_before_success)
    )
    outcomes.append(httpx.Response(200, json=spec))

    assert (
        fetch_openapi("https://example.test/openapi", "test-user", "test-pass") == spec
    )

    assert len(requests) == timeouts_before_success + 1
    assert delays == [2, 4][:timeouts_before_success]
    assert all(request.method == "GET" for request in requests)
    assert all(
        request.headers["authorization"] == requests[0].headers["authorization"]
        for request in requests
    )


@pytest.mark.parametrize("timeout_type", [httpx.ConnectTimeout, httpx.ReadTimeout])
def test_fetch_openapi_raises_after_three_timeouts(mock_openapi_fetch, timeout_type):
    outcomes, requests, delays = mock_openapi_fetch
    last_error = timeout_type("Still unavailable")
    outcomes.extend(
        [
            timeout_type("Temporary timeout"),
            timeout_type("Temporary timeout"),
            last_error,
        ]
    )

    with pytest.raises(timeout_type) as caught:
        fetch_openapi("https://example.test/openapi", "test-user", "test-pass")

    assert caught.value is last_error
    assert len(requests) == 3
    assert delays == [2, 4]


@pytest.mark.parametrize("status_code", [401, 503])
def test_fetch_openapi_does_not_retry_http_errors(mock_openapi_fetch, status_code):
    outcomes, requests, delays = mock_openapi_fetch
    outcomes.append(httpx.Response(status_code))

    with pytest.raises(httpx.HTTPStatusError):
        fetch_openapi("https://example.test/openapi", "test-user", "test-pass")

    assert len(requests) == 1
    assert delays == []


def test_fetch_openapi_does_not_retry_invalid_json(mock_openapi_fetch):
    outcomes, requests, delays = mock_openapi_fetch
    outcomes.append(httpx.Response(200, text="not JSON"))

    with pytest.raises(json.JSONDecodeError):
        fetch_openapi("https://example.test/openapi", "test-user", "test-pass")

    assert len(requests) == 1
    assert delays == []


@pytest.mark.parametrize("error_type", [httpx.ConnectError, httpx.WriteTimeout])
def test_fetch_openapi_does_not_retry_other_transport_errors(
    mock_openapi_fetch, error_type
):
    outcomes, requests, delays = mock_openapi_fetch
    outcomes.append(error_type("Non-retryable transport failure"))

    with pytest.raises(error_type):
        fetch_openapi("https://example.test/openapi", "test-user", "test-pass")

    assert len(requests) == 1
    assert delays == []


def count_operations(spec: dict) -> int:
    return sum(
        1
        for path_item in spec.get("paths", {}).values()
        for method in path_item
        if not method.startswith("x-")
    )


def collect_resource_namespaces(spec: dict) -> set[str]:
    return {
        operation["x-sdk-resource"]
        for path_item in spec.get("paths", {}).values()
        for method, operation in path_item.items()
        if not method.startswith("x-")
    }


def test_normalize_spec_removes_token_and_adds_security_scheme():
    normalized = normalize_spec(
        load_json(RAW_SPEC_PATH), load_overrides(OVERRIDES_PATH)
    )
    search_operation = normalized["paths"]["/api/search/v1"]["get"]

    assert search_operation["x-sdk-resource"] == "search"
    assert search_operation["x-sdk-method-name"] == "search_v1"
    assert all(
        parameter["name"] != "token" for parameter in search_operation["parameters"]
    )
    assert normalized["components"]["securitySchemes"]["tokenAuth"]["name"] == "token"


def test_collect_resources_matches_expected_counts():
    normalized = normalize_spec(
        load_json(RAW_SPEC_PATH), load_overrides(OVERRIDES_PATH)
    )
    resources = collect_resources(normalized)
    expected_namespaces = collect_resource_namespaces(normalized)

    namespace_set = {resource.namespace for resource in resources}
    assert len(resources) == len(expected_namespaces)
    assert sum(len(resource.operations) for resource in resources) == count_operations(
        normalized
    )
    assert namespace_set == expected_namespaces
    assert {"douyin", "douyin_xingtu", "tiktok_shop", "xiaohongshu_pgy"}.issubset(
        namespace_set
    )


def test_diff_summary_reports_operation_changes():
    old_spec = {
        "paths": {
            "/api/demo/v1": {
                "get": {"operationId": "demoV1", "summary": "old"},
            }
        },
        "tags": [],
    }
    new_spec = {
        "paths": {
            "/api/demo/v1": {
                "get": {"operationId": "demoV1", "summary": "new"},
            },
            "/api/demo/v2": {
                "get": {"operationId": "demoV2", "summary": "added"},
            },
        },
        "tags": [],
    }

    summary = build_diff_summary(old_spec, new_spec)

    assert "demoV2 [GET /api/demo/v2]" in summary
    assert "demoV1 [GET /api/demo/v1]" in summary
    assert "Changed operationId count: 1" in summary


def test_normalize_spec_derives_method_name_from_path():
    spec = {
        "paths": {
            "/api/demo/v1": {"get": {"operationId": "stillWrong"}},
            "/api/demo/path-derived/v1": {"get": {"operationId": "totallyWrongMethod"}},
            "/api/demo/nested/child/v2": {"get": {"operationId": "anotherBadNameV9"}},
            "/api/demo/get-kol-show-items-v2/v1": {
                "get": {"operationId": "irrelevantOperationId"}
            },
        }
    }

    normalized = normalize_spec(spec, {})

    assert (
        normalized["paths"]["/api/demo/v1"]["get"]["x-sdk-method-name"] == "demo_v1"
    )
    assert (
        normalized["paths"]["/api/demo/path-derived/v1"]["get"]["x-sdk-method-name"]
        == "path_derived_v1"
    )
    assert (
        normalized["paths"]["/api/demo/nested/child/v2"]["get"]["x-sdk-method-name"]
        == "nested_child_v2"
    )
    assert (
        normalized["paths"]["/api/demo/get-kol-show-items-v2/v1"]["get"][
            "x-sdk-method-name"
        ]
        == "get_kol_show_items_v2_v1"
    )
