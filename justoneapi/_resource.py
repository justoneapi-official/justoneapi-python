from __future__ import annotations

from typing import Any

from justoneapi._response import ApiResponse
from justoneapi._transport import Transport


class BaseResource:
    def __init__(self, transport: Transport):
        self._transport = transport

    def _get(self, path: str, params: dict[str, Any]) -> ApiResponse[Any]:
        return self._transport.get(path, params)

    def _post(
        self,
        path: str,
        params: dict[str, Any],
        *,
        data: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        token_in_form: bool = False,
    ) -> ApiResponse[Any]:
        return self._transport.post(
            path, params, data=data, json=json, token_in_form=token_in_form
        )
