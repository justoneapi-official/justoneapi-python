from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class VcgResource(BaseResource):
    """Generated resource for VCG."""

    def search_image_v1(
        self,
        *,
        keyword: str,
        limit: str | None = None,
        start_page: str | None = None,
        max_pages: str | None = None,
        exclude_resource_ids: list[Any] | None = None,
        content_filter: str | None = "all",
    ) -> ApiResponse[Any]:
        """
        Image Search

        Searches VCG images by keyword with a requested image count, page controls, exclusions for previously collected resource IDs, and an optional 500px Select/Prime filter excluding AIGC. Use the same content filter when continuing an interrupted search.

        Args:
            keyword: Image search keyword, up to 200 characters without control characters.
            limit: Maximum number of unique images to return, excluding the supplied resource IDs.
            start_page: First page to search, starting from 1. For continuation, use the next page returned by the previous request.
            max_pages: Maximum number of pages to visit in this request. The last requested page must not exceed 10000.
            exclude_resource_ids: Previously collected VCG resource IDs to exclude when continuing a search. Supply comma-separated IDs or repeat this query parameter.
            content_filter: Optional brand and AIGC search restriction. Keep this value unchanged across pagination and continuation.  Available Values: - `all`: Keep the default search without additional brand or AIGC filters. - `selected_500px_no_aigc`: Select only 500px Select and 500px Prime, exclude AIGC using the site's filter, and retain best ordering. Do not expand to other brands when results run out.
        """
        return self._get(
            "/api/vcg/search-image/v1",
            {
                "keyword": keyword,
                "limit": limit,
                "startPage": start_page,
                "maxPages": max_pages,
                "excludeResourceIds": exclude_resource_ids,
                "contentFilter": content_filter,
            },
        )
