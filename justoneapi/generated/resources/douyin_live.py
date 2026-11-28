from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class DouyinLiveResource(BaseResource):
    """Generated resource for Douyin Live."""

    def search_live_v1(
        self,
        *,
        keyword: str,
        cursor: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        Live Room Search

        Searches Douyin (TikTok China) live rooms by a creator's Douyin ID or nickname with cursor pagination. Use it to find live rooms for creator discovery and live-stream research.

        Args:
            keyword: The creator's Douyin ID or nickname.
            cursor: Pagination cursor. Use 0 for the first page, then the cursor returned by the previous response.
        """
        return self._get(
            "/api/douyin-live/search-live/v1",
            {
                "keyword": keyword,
                "cursor": cursor,
            },
        )

    def get_livestream_info_v1(
        self,
        *,
        webcast_id: str,
    ) -> ApiResponse[Any]:
        """
        Livestream Info

        Retrieves Douyin livestream information by webcast ID. Use it to look up a known live room using the ID from its Douyin live URL.

        Args:
            webcast_id: The digits in the final path segment of the Douyin live room URL.
        """
        return self._get(
            "/api/douyin-live/get-livestream-info/v1",
            {
                "webcastId": webcast_id,
            },
        )

    def get_livestream_info_v2(
        self,
        *,
        sec_uid: str,
    ) -> ApiResponse[Any]:
        """
        Livestream Info

        Retrieves Douyin livestream information by the user's secUid. Use it to look up a known user's livestream using the ID from their Douyin profile URL.

        Args:
            sec_uid: The user's secUid from the Douyin profile URL, also called sec_user_id.
        """
        return self._get(
            "/api/douyin-live/get-livestream-info/v2",
            {
                "secUid": sec_uid,
            },
        )

    def get_livestream_info_v3(
        self,
        *,
        room_id: str,
    ) -> ApiResponse[Any]:
        """
        Livestream Info

        Retrieves Douyin livestream information by room ID. Use it to inspect a specific live room when you already have its roomId.

        Args:
            room_id: The Douyin live room ID (room_id), supplied as a string.
        """
        return self._get(
            "/api/douyin-live/get-livestream-info/v3",
            {
                "roomId": room_id,
            },
        )

    def get_live_gift_ranking_v1(
        self,
        *,
        room_id: str,
    ) -> ApiResponse[Any]:
        """
        Live Gift Ranking

        Retrieves the gift sender ranking for a Douyin livestream by room ID. Use it to review the leading gift senders for a known live room.

        Args:
            room_id: The Douyin live room ID (room_id), supplied as a string.
        """
        return self._get(
            "/api/douyin-live/get-live-gift-ranking/v1",
            {
                "roomId": room_id,
            },
        )

    def convert_webcast_id_v1(
        self,
        *,
        webcast_id: str,
    ) -> ApiResponse[Any]:
        """
        Webcast ID Conversion

        Converts a Douyin webcast ID from a live room URL to the corresponding room ID. Use the room ID to query livestream information or gift sender rankings.

        Args:
            webcast_id: The digits in the final path segment of the Douyin live room URL.
        """
        return self._get(
            "/api/douyin-live/convert-webcast-id/v1",
            {
                "webcastId": webcast_id,
            },
        )
