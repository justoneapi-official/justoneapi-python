from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class PixabayResource(BaseResource):
    """Generated resource for Pixabay."""

    def search_image_v1(
        self,
        *,
        keyword: str,
        limit: str | None = None,
        start_page: str | None = None,
        max_pages: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Photo Search

        Searches public Pixabay photo result pages by keyword with a requested image count and page controls. Each result includes its Pixabay photo page, public contributor information when shown, and a source-provided image URL.

        Args:
            keyword: Photo search keyword, up to 100 characters without control characters.
            limit: Maximum number of unique photos to return.
            start_page: First result page to search, starting from 1.
            max_pages: Maximum number of pages to visit in this request. The last page must not exceed 10000.
        """
        return self._get(
            "/api/pixabay/search-image/v1",
            {
                "keyword": keyword,
                "limit": limit,
                "startPage": start_page,
                "maxPages": max_pages,
            },
        )
