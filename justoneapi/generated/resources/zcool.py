from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class ZcoolResource(BaseResource):
    """Generated resource for ZCOOL."""

    def search_image_v1(
        self,
        *,
        keyword: str,
        limit: str | None = None,
        start_page: str | None = None,
        max_pages: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Image Search

        Searches ZCool community work images by keyword with a requested image count and page controls. Each returned image carries its own work-image page URL and the author of the source work.

        Args:
            keyword: Image search keyword, up to 200 characters without control characters.
            limit: Maximum number of unique images to return.
            start_page: First page to search, starting from 1. For continuation, use the next page returned by the previous request.
            max_pages: Maximum number of pages to visit in this request. The last requested page must not exceed 10000.
        """
        return self._get(
            "/api/zcool/search-image/v1",
            {
                "keyword": keyword,
                "limit": limit,
                "startPage": start_page,
                "maxPages": max_pages,
            },
        )
