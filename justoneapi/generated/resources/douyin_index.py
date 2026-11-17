from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DouyinIndexResource(BaseResource):
    """Generated resource for Douyin Index."""

    def get_keyword_trends_v1(
        self,
        *,
        since: str,
        until: str,
        keyword: str | None = None,
        keywords: list[Any] | None = None,
    ) -> ApiResponse[Any]:
        """
        Keyword Trends

        Retrieves Douyin Index (Ocean Engine trend index) keyword trends for one keyword or up to five keywords over an inclusive date range in China time (UTC+8). Use it for topic research and comparing keyword interest over time.

        Args:
            since: First day to include. Use YYYY-MM-DD or an RFC 3339 timestamp with a timezone; timestamps are interpreted as calendar days in China time (UTC+8).
            until: Last day to include, in the same format as since, on or after since in China time (UTC+8). Figures are usually published one or two days later.
            keyword: One keyword, at most 50 characters without commas. Provide exactly one of keyword or keywords; letter case does not matter.
            keywords: One to five keywords, separated by commas or supplied as repeated query parameters. Each keyword must contain at most 50 characters without commas. Provide exactly one of keyword or keywords; letter case does not matter.
        """
        return self._get(
            "/api/douyin-index/get-keyword-trends/v1",
            {
                "since": since,
                "until": until,
                "keyword": keyword,
                "keywords": keywords,
            },
        )

    def get_realtime_hotspots_v1(
        self,
    ) -> ApiResponse[Any]:
        """
        Realtime Hotspots

        Retrieves the current hotspot lists from Douyin Index in Creator Center. Use it to monitor trending topics and plan timely content.
        """
        return self._get(
            "/api/douyin-index/get-realtime-hotspots/v1",
            {},
        )
