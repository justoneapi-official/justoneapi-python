from __future__ import annotations

import inspect
import json
from pathlib import Path
from urllib.parse import parse_qs

import httpx
import pytest

from justoneapi import JustOneAPIClient
from justoneapi._exceptions import BusinessError, ProtocolError, TransportError
from tools.sdk_codegen import to_python_identifier

RAW_SPEC = json.loads(
    (Path(__file__).resolve().parents[1] / "openapi/public-api.json").read_text()
)
POST_OPERATIONS = [
    (path, item["post"]) for path, item in RAW_SPEC["paths"].items() if "post" in item
]


@pytest.fixture()
def make_client():
    clients: list[JustOneAPIClient] = []

    def _make(handler, *, raise_on_business_error: bool = False) -> JustOneAPIClient:
        client = JustOneAPIClient(
            token="test-token", raise_on_business_error=raise_on_business_error
        )
        client._transport.close()
        client._transport._client = httpx.Client(
            transport=httpx.MockTransport(handler),
            base_url="https://api.justoneapi.com",
            follow_redirects=True,
        )
        clients.append(client)
        return client

    yield _make

    for client in clients:
        client.close()


def test_code_zero_is_success(make_client):
    captured: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["query"] = str(request.url)
        return httpx.Response(
            200, json={"code": 0, "message": "ok", "data": {"value": 1}}
        )

    client = make_client(handler)
    response = client.search.search_v1(keyword="deepseek")

    assert response.success is True
    assert response.code == 0
    assert response.data == {"value": 1}
    assert "token=test-token" in captured["query"]
    assert "keyword=deepseek" in captured["query"]


def test_non_zero_code_is_failure(make_client):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"code": 200, "message": "not ok", "data": {}})

    client = make_client(handler)
    response = client.search.search_v1(keyword="deepseek")

    assert response.success is False
    assert response.code == 200
    assert response.message == "not ok"


def test_http_error_with_json_payload_returns_api_response(make_client):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            401,
            json={"code": 100, "message": "invalid token", "data": None},
        )

    client = make_client(handler)
    response = client.search.search_v1(keyword="deepseek")

    assert response.success is False
    assert response.code == 100
    assert response.message == "invalid token"


def test_raise_on_business_error(make_client):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200, json={"code": "300", "message": "quota exceeded", "data": None}
        )

    client = make_client(handler, raise_on_business_error=True)

    with pytest.raises(BusinessError) as excinfo:
        client.search.search_v1(keyword="deepseek")

    assert excinfo.value.response.code == "300"


def test_non_json_response_raises_protocol_error(make_client):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200, text="not json", headers={"content-type": "text/plain"}
        )

    client = make_client(handler)

    with pytest.raises(ProtocolError):
        client.search.search_v1(keyword="deepseek")


def test_string_zero_is_not_treated_as_success(make_client):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"code": "0", "message": "ok", "data": {}})

    client = make_client(handler)
    response = client.search.search_v1(keyword="deepseek")

    assert response.success is False
    assert response.code == "0"


def test_optional_none_is_omitted_and_bool_is_lowercase(make_client):
    captured: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["query"] = str(request.url)
        return httpx.Response(200, json={"code": 0, "message": "ok", "data": []})

    client = make_client(handler)
    response = client.taobao.search_item_list_v1(
        keyword="bag", sort="_sale", tmall=True, end_price=None
    )

    assert response.success is True
    assert "tmall=true" in captured["query"]
    assert "endPrice" not in captured["query"]


@pytest.mark.parametrize(
    "path,operation", POST_OPERATIONS, ids=[p for p, _ in POST_OPERATIONS]
)
def test_post_operations_follow_public_request_contract(make_client, path, operation):
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(200, json={"code": 0, "message": "ok", "data": []})

    client = make_client(handler)
    namespace = path.split("/")[2].replace("-", "_")
    method_name = to_python_identifier("_".join(path.split("/")[3:]))
    method = getattr(getattr(client, namespace), method_name)
    form_schema = (
        operation.get("requestBody", {})
        .get("content", {})
        .get("application/x-www-form-urlencoded", {})
        .get("schema")
    )
    fields = (
        form_schema["properties"]
        if form_schema is not None
        else {p["name"]: p["schema"] for p in operation.get("parameters", [])}
    )
    required = (
        set(form_schema.get("required", []))
        if form_schema is not None
        else {p["name"] for p in operation.get("parameters", []) if p.get("required")}
    )
    signature = inspect.signature(method)
    assert "token" not in signature.parameters
    arguments = {}
    expected = {"token": ["test-token"]}
    for name, schema in fields.items():
        if name == "token":
            continue
        python_name = to_python_identifier(name)
        parameter = signature.parameters[python_name]
        if name in required and "default" not in schema:
            assert parameter.default is inspect.Parameter.empty
        else:
            assert parameter.default == schema.get("default")
        value = schema.get("enum", [None])[-1]
        if value is None:
            value = 7 if schema.get("type") == "integer" else "微信 + & = / ?"
        arguments[python_name] = value
        expected[name] = [str(value)]

    response = method(**arguments)

    assert response.success is True
    assert len(requests) == 1
    request = requests[0]
    assert request.method == "POST"
    assert request.url.path == path
    if form_schema is not None:
        assert request.headers["Content-Type"] == "application/x-www-form-urlencoded"
        assert not request.url.query
        assert parse_qs(request.content.decode(), keep_blank_values=True) == expected
    else:
        assert not request.content
        assert parse_qs(request.url.query.decode(), keep_blank_values=True) == expected


@pytest.mark.parametrize("version", ["v1", "v2"])
def test_article_search_form_defaults(make_client, version):
    forms = []

    def handler(request):
        forms.append(parse_qs(request.content.decode(), keep_blank_values=True))
        return httpx.Response(200, json={"code": 0, "message": "ok", "data": []})

    client = make_client(handler)
    getattr(client.weixin, f"search_article_{version}")(keyword="人工智能")

    expected = {
        "token": ["test-token"],
        "keyword": ["人工智能"],
        "currentPage": ["1"],
        "offset": ["0"],
        "cookies_buffer": [""],
    }
    if version == "v1":
        expected.update(publishTimeType=["ALL"], sortType=["COMPREHENSIVE"])
    else:
        expected["subSearchType"] = ["ALL"]
    assert forms == [expected]


@pytest.mark.parametrize("version", ["v1", "v2"])
def test_article_search_requires_keyword_before_sending(make_client, version):
    def handler(request):
        pytest.fail("Missing keyword must not send a request")

    client = make_client(handler)
    with pytest.raises(TypeError, match="keyword"):
        getattr(client.weixin, f"search_article_{version}")()


def test_article_search_omits_none_form_values(make_client):
    def handler(request):
        form = parse_qs(request.content.decode(), keep_blank_values=True)
        assert "publishTimeType" not in form
        assert "cookies_buffer" not in form
        assert form["offset"] == ["0"]
        return httpx.Response(200, json={"code": 0, "message": "ok", "data": []})

    client = make_client(handler)
    client.weixin.search_article_v1(
        keyword="测试", publish_time_type=None, cookies_buffer=None
    )


@pytest.mark.parametrize(
    "outcome,error_type",
    [
        (httpx.Response(200, text="not JSON"), ProtocolError),
        (httpx.Response(200, json=[]), ProtocolError),
        (httpx.ConnectError("connection failed"), TransportError),
        (httpx.Response(200, json={"code": 301, "message": "failed"}), BusinessError),
    ],
)
def test_post_preserves_error_handling_without_retry(make_client, outcome, error_type):
    requests = []

    def handler(request):
        requests.append(request)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    client = make_client(handler, raise_on_business_error=True)
    with pytest.raises(error_type) as exc:
        client.weixin.search_article_v1(keyword="测试")
    if error_type is not BusinessError:
        assert "POST /api/weixin/search-article/v1" in str(exc.value)
    assert len(requests) == 1
