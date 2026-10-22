from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class WeixinChannelsResource(BaseResource):
    """Generated resource for WeChat Channels."""

    def search_video_v1(
        self,
        *,
        keyword: str,
        cookies_buffer: str | None = "",
        current_page: int | None = 1,
        offset: int | None = 0,
        publish_time_type: str | None = "ALL",
        sort_type: str | None = "COMPREHENSIVE",
    ) -> ApiResponse[Any]:
        """
        Video Search

        Searches WeChat Channels videos by keyword with publish-time, sort, page, offset, and continuation-state controls. Use it to find recent or ordered video results and continue web-search pages.

        Args:
            keyword: Search keyword for WeChat Channels video results.
            cookies_buffer: Opaque pagination state returned by the previous WeChat Channels web search response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
            current_page: Current page number starting from 1 for WeChat Channels web search pagination.
            offset: Search result offset returned by the previous WeChat Channels search response. Use 0 for the first page.
            publish_time_type: Publish time filter for WeChat Channels video web search.  Available Values: - `ALL`: All publish times - `ONE_DAY`: Published in the last day - `SEVEN_DAYS`: Published in the last seven days - `HALF_YEAR`: Published in the last half year
            sort_type: Sort order for WeChat Channels video search results.  Available Values: - `COMPREHENSIVE`: Comprehensive sort - `LATEST`: Latest first - `HOT`: Hot first
        """
        return self._post(
            "/api/weixin-channels/search-video/v1",
            {},
            data={
                "keyword": keyword,
                "cookies_buffer": cookies_buffer,
                "currentPage": current_page,
                "offset": offset,
                "publishTimeType": publish_time_type,
                "sortType": sort_type,
            },
            token_in_form=True,
        )

    def search_video_v2(
        self,
        *,
        keyword: str,
        cookies_buffer: str | None = "",
        current_page: int | None = 1,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        Video Search

        Searches the WeChat Channels video category by keyword with page, offset, and continuation-state controls. Use it to retrieve categorized video results and continue additional pages.

        Args:
            keyword: Search keyword for categorized WeChat Channels video results.
            cookies_buffer: Opaque pagination state returned by the previous WeChat Channels web search response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
            current_page: Current page number starting from 1 for WeChat Channels web search pagination.
            offset: Search result offset returned by the previous WeChat Channels search response. Use 0 for the first page.
        """
        return self._post(
            "/api/weixin-channels/search-video/v2",
            {},
            data={
                "keyword": keyword,
                "cookies_buffer": cookies_buffer,
                "currentPage": current_page,
                "offset": offset,
            },
            token_in_form=True,
        )

    def search_account_v1(
        self,
        *,
        keyword: str,
        cookies_buffer: str | None = "",
        current_page: int | None = 1,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        Account Search

        Searches the WeChat Channels account category by keyword with page, offset, and continuation-state controls. Use it to discover creator accounts through paginated web-search results.

        Args:
            keyword: Search keyword for WeChat Channels account web search.
            cookies_buffer: Opaque pagination state returned by the previous WeChat Channels account search response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
            current_page: Current page number starting from 1 for WeChat Channels web search pagination.
            offset: Search result offset returned by the previous WeChat Channels account search response. Use 0 for the first page.
        """
        return self._post(
            "/api/weixin-channels/search-account/v1",
            {},
            data={
                "keyword": keyword,
                "cookies_buffer": cookies_buffer,
                "currentPage": current_page,
                "offset": offset,
            },
            token_in_form=True,
        )

    def search_account_v2(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Account Search

        Searches WeChat Channels account-related records by keyword using the direct Channels lookup. Use it to discover creator accounts and related channel objects without pagination input.

        Args:
            keyword: Search keyword used to find WeChat Channels accounts and related video objects.
        """
        return self._post(
            "/api/weixin-channels/search-account/v2",
            {
                "keyword": keyword,
            },
        )

    def search_account_v3(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Account Search

        Looks up a specific WeChat Channels account identity by keyword. Use it to resolve a creator name or account term to the identifier required by account-video queries.

        Args:
            keyword: Search keyword used to resolve a WeChat Channels account id.
        """
        return self._post(
            "/api/weixin-channels/search-account/v3",
            {
                "keyword": keyword,
            },
        )

    def get_account_videos_v1(
        self,
        *,
        v2_name: str,
        last_buffer: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Account Videos

        Retrieves a paginated WeChat Channels account feed by v2Name with continuation-buffer support. Use it to browse videos and other feed entries published by a known creator account.

        Args:
            v2_name: WeChat Channels account unique id, usually ending with @finder.
            last_buffer: Pagination buffer returned by the previous WeChat Channels account videos response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
        """
        return self._post(
            "/api/weixin-channels/get-account-videos/v1",
            {},
            data={
                "v2Name": v2_name,
                "last_buffer": last_buffer,
            },
            token_in_form=True,
        )

    def get_bound_channel_v1(
        self,
        *,
        ghid: str | None = "",
        url: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Get Bound Channel

        Finds the WeChat Channels account bound to a WeChat Official Account using either its original ID or an article URL. Use it to connect an official account with its Channels identity.

        Args:
            ghid: WeChat Official Account original id used to find the bound WeChat Channels account. Use either ghid or url.
            url: WeChat Official Account article URL used to find the bound WeChat Channels account. Use either ghid or url.
        """
        return self._get(
            "/api/weixin-channels/get-bound-channel/v1",
            {
                "ghid": ghid,
                "url": url,
            },
        )

    def get_video_basic_info_v1(
        self,
        *,
        feed_info: str,
    ) -> ApiResponse[Any]:
        """
        Video Basic Info

        Resolves a copied WeChat Channels video link, preview URL, or short feed ID to basic video information. Use it to identify a shared Channels video before further lookups.

        Args:
            feed_info: WeChat Channels copied video link, finder-preview URL, or short feed id.
        """
        return self._get(
            "/api/weixin-channels/get-video-basic-info/v1",
            {
                "feedInfo": feed_info,
            },
        )

    def get_video_title_v1(
        self,
        *,
        object_id: str,
        object_nonce_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Video Title

        Retrieves lightweight title information for a WeChat Channels video by object ID and optional nonce ID. Use it to identify known video content without requesting downloadable media.

        Args:
            object_id: WeChat Channels video object id.
            object_nonce_id: Optional WeChat Channels object nonce id. Supplying it can improve lookup accuracy.
        """
        return self._get(
            "/api/weixin-channels/get-video-title/v1",
            {
                "objectId": object_id,
                "objectNonceId": object_nonce_id,
            },
        )

    def convert_export_id_v1(
        self,
        *,
        export_id: str,
    ) -> ApiResponse[Any]:
        """
        Export Id Conversion

        Converts an encrypted WeChat Channels export ID from search results into a usable video object identity. Use it to prepare the identifier required by video lookup endpoints.

        Args:
            export_id: Encrypted WeChat Channels exportId returned by video search results.
        """
        return self._get(
            "/api/weixin-channels/convert-export-id/v1",
            {
                "exportId": export_id,
            },
        )

    def get_video_download_url_v1(
        self,
        *,
        object_id: str,
        object_nonce_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Video Download URL

        Retrieves a downloadable media URL for a WeChat Channels video by object ID and optional nonce ID. Use it to download or play media from a known Channels video.

        Args:
            object_id: WeChat Channels video object id used to fetch downloadable media links.
            object_nonce_id: Optional WeChat Channels object nonce id. Supplying it can improve media lookup accuracy.
        """
        return self._get(
            "/api/weixin-channels/get-video-download-url/v1",
            {
                "objectId": object_id,
                "objectNonceId": object_nonce_id,
            },
        )

    def get_video_share_url_v1(
        self,
        *,
        object_id: str,
    ) -> ApiResponse[Any]:
        """
        Video Share URL

        Generates a share link for a WeChat Channels video identified by objectId. Use it to share a known Channels video or obtain its link for a subsequent lookup.

        Args:
            object_id: WeChat Channels video objectId as a numeric string of up to 32 digits.
        """
        return self._get(
            "/api/weixin-channels/get-video-share-url/v1",
            {
                "objectId": object_id,
            },
        )

    def get_video_metrics_v1(
        self,
        *,
        object_id: str,
        last_buffer: str | None = "",
        object_nonce_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Video Metrics

        Retrieves interaction metrics for a WeChat Channels video by object ID with optional continuation-buffer input. Use it to review engagement for known video content.

        Args:
            object_id: WeChat Channels video object id used to fetch interaction metrics.
            last_buffer: Pagination buffer returned by the previous WeChat Channels metrics response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
            object_nonce_id: Optional WeChat Channels object nonce id.
        """
        return self._post(
            "/api/weixin-channels/get-video-metrics/v1",
            {},
            data={
                "objectId": object_id,
                "last_buffer": last_buffer,
                "objectNonceId": object_nonce_id,
            },
            token_in_form=True,
        )

    def get_video_comment_v1(
        self,
        *,
        object_id: str,
        last_buffer: str | None = "",
        object_nonce_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Video Comments

        Retrieves first-level comments for a WeChat Channels video by object ID with continuation-buffer pagination. Use it to review audience discussion on known video content.

        Args:
            object_id: WeChat Channels video object id used to fetch first-level comments. If you only have the exportId returned by a video search result, first call the Export Id Conversion (V1) endpoint at /api/weixin-channels/convert-export-id/v1 to convert it to an objectId.
            last_buffer: Pagination buffer returned by the previous first-level WeChat Channels comment response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
            object_nonce_id: Optional WeChat Channels object nonce id.
        """
        return self._post(
            "/api/weixin-channels/get-video-comment/v1",
            {},
            data={
                "objectId": object_id,
                "last_buffer": last_buffer,
                "objectNonceId": object_nonce_id,
            },
            token_in_form=True,
        )

    def get_video_sub_comment_v1(
        self,
        *,
        object_id: str,
        root_comment_id: str,
        last_buffer: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Video Sub Comments

        Retrieves replies under a first-level WeChat Channels video comment using the video and root-comment IDs. Use it to continue a threaded comment discussion with buffer pagination.

        Args:
            object_id: WeChat Channels video object id used to fetch second-level comment replies.
            root_comment_id: Root first-level comment id returned by the WeChat Channels video comments endpoint.
            last_buffer: Pagination buffer for WeChat Channels second-level comment replies. Use the first-level comment's last_buffer for the first reply page when present. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
        """
        return self._post(
            "/api/weixin-channels/get-video-sub-comment/v1",
            {},
            data={
                "objectId": object_id,
                "rootCommentId": root_comment_id,
                "last_buffer": last_buffer,
            },
            token_in_form=True,
        )
