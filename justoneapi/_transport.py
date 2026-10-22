from __future__ import annotations

from typing import Any

import httpx

from justoneapi._exceptions import (
    BusinessError,
    ProtocolError,
    TransportError,
)
from justoneapi._response import ApiResponse
from justoneapi._version import __version__
from justoneapi.log import logger


class Transport:
    def __init__(
        self,
        *,
        token: str,
        base_url: str,
        timeout: int,
        raise_on_business_error: bool,
    ):
        self._token = token
        self._base_url = base_url.rstrip("/")
        self._raise_on_business_error = raise_on_business_error
        self._client = httpx.Client(
            base_url=self._base_url,
            timeout=timeout,
            follow_redirects=True,
            headers={"JUSTONEAPI_PYTHON_SKD_VERSION": __version__},
        )

    def close(self) -> None:
        self._client.close()

    def get(self, path: str, params: dict[str, Any]) -> ApiResponse[Any]:
        return self._request("GET", path, params)

    def post(
        self,
        path: str,
        params: dict[str, Any],
        *,
        data: dict[str, Any] | None = None,
        token_in_form: bool = False,
    ) -> ApiResponse[Any]:
        return self._request(
            "POST", path, params, data=data, token_in_form=token_in_form
        )

    def _request(
        self,
        method: str,
        path: str,
        params: dict[str, Any],
        *,
        data: dict[str, Any] | None = None,
        token_in_form: bool = False,
    ) -> ApiResponse[Any]:
        request_params = self._clean_params(params)
        request_data = self._clean_params(data) if data is not None else None
        if token_in_form:
            request_data = {"token": self._token, **(request_data or {})}
        else:
            request_params = {"token": self._token, **request_params}
        try:
            response = self._client.request(
                method, path, params=request_params, data=request_data
            )
        except httpx.HTTPError as exc:
            raise TransportError(f"Request failed for {method} {path}: {exc}") from exc

        log_message = response.headers.get("JUSTONEAPI_PYTHON_SDK_LOG_MESSAGE")
        if log_message:
            logger.warning(log_message)

        try:
            payload = response.json()
        except ValueError as exc:
            raise ProtocolError(
                f"Server returned a non-JSON response for {method} {path}"
            ) from exc

        if not isinstance(payload, dict):
            raise ProtocolError(
                f"Server returned a non-object JSON payload for {method} {path}"
            )

        api_response = ApiResponse(
            success=self._is_success_code(payload.get("code")),
            code=payload.get("code"),
            message=str(payload.get("message") or ""),
            data=payload.get("data"),
            raw_json=payload,
        )

        if self._raise_on_business_error and not api_response.success:
            raise BusinessError(api_response)
        return api_response

    @staticmethod
    def _is_success_code(code: Any) -> bool:
        return code == 0

    @staticmethod
    def _clean_params(params: dict[str, Any]) -> dict[str, Any]:
        cleaned: dict[str, Any] = {}
        for key, value in params.items():
            if value is None:
                continue
            if isinstance(value, bool):
                cleaned[key] = str(value).lower()
            else:
                cleaned[key] = value
        return cleaned
