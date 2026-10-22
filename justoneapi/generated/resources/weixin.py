from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class WeixinResource(BaseResource):
    """Generated resource for WeChat Official Accounts."""

    def get_account_today_articles_v1(
        self,
        *,
        biz: str | None = "",
        url: str | None = "",
        name: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Account Today Articles

        Retrieves articles published today by a WeChat Official Account identified by biz ID, article URL, account name, or wxid. Use it to monitor same-day publishing activity for a known account.

        Args:
            biz: WeChat Official Account biz id. You can read it from the __biz query parameter in an article URL. Use one of biz, url, or name.
            url: WeChat Official Account article URL used to identify the account. Use one of biz, url, or name.
            name: WeChat Official Account name or wxid. Use one of biz, url, or name.
        """
        return self._get(
            "/api/weixin/get-account-today-articles/v1",
            {
                "biz": biz,
                "url": url,
                "name": name,
            },
        )

    def get_account_history_articles_v1(
        self,
        *,
        username: str,
        item_show_type: str | None = "ARTICLE",
        offset: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Account Historical Articles

        Retrieves historical posts for a WeChat Official Account by username, with cursor pagination and article, video, audio, or image content tabs. Use it to browse an account's publishing history.

        Args:
            username: WeChat Official Account username with the gh_ prefix.
            item_show_type: Content tab. Defaults to ARTICLE.  Available Values: - `ARTICLE`: Articles - `VIDEO`: Videos - `AUDIO`: Audio - `IMAGE`: Images
            offset: Base64 pagination cursor. Leave empty for the first page; pass next_offset from the previous response for the next page. Send it in the URL-encoded form body.
        """
        return self._post(
            "/api/weixin/get-account-history-articles/v1",
            {},
            data={
                "username": username,
                "itemShowType": item_show_type,
                "offset": offset,
            },
            token_in_form=True,
        )

    def get_account_history_articles_v2(
        self,
        *,
        ghid: str | None = "",
        offset: str | None = "",
        url: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Account Historical Articles

        Retrieves historical articles for a WeChat Official Account identified by ghid or article URL, with an offset cursor from the previous page. Use it to continue through an account's article archive with cursor pagination.

        Args:
            ghid: WeChat Official Account original identifier, using the gh_ prefix returned by WeChat. Use either ghid or url.
            offset: PagingInfo.Offset cursor returned by the previous response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
            url: WeChat Official Account article URL used to identify the account and fetch historical articles. Use either ghid or url.
        """
        return self._post(
            "/api/weixin/get-account-history-articles/v2",
            {},
            data={
                "ghid": ghid,
                "offset": offset,
                "url": url,
            },
            token_in_form=True,
        )

    def get_article_metrics_v1(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Metrics

        Retrieves basic interaction metrics for a WeChat Official Account article URL that ends with #rd or #wechat_redirect. Use it to perform a lightweight popularity check for a known article.

        Args:
            article_url: WeChat Official Account article URL used to fetch basic interaction metrics such as reads and likes. It must end with #rd or #wechat_redirect.
        """
        return self._get(
            "/api/weixin/get-article-metrics/v1",
            {
                "articleUrl": article_url,
            },
        )

    def get_article_metrics_v2(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Metrics

        Retrieves extended interaction metrics for a WeChat Official Account article by URL. Use it to compare article performance or support deeper engagement analysis for known content.

        Args:
            article_url: WeChat Official Account article URL used to fetch extended interaction and article performance metrics.
        """
        return self._get(
            "/api/weixin/get-article-metrics/v2",
            {
                "articleUrl": article_url,
            },
        )

    def get_article_detail_v1(
        self,
        *,
        article_url: str,
        mode: str | None = "TEXT",
    ) -> ApiResponse[Any]:
        """
        Article Details

        Retrieves a WeChat Official Account article by URL with selectable plain-text or rich-text content mode. Use it to collect a known article in the preferred representation for reading, extraction, or storage.

        Args:
            article_url: WeChat Official Account article URL used to fetch article detail content and metadata.
            mode: Article body format. TEXT returns plain text, and RICH_TEXT returns rich text when supported.  Available Values: - `TEXT`: Plain text article detail - `RICH_TEXT`: Rich text article detail
        """
        return self._get(
            "/api/weixin/get-article-detail/v1",
            {
                "articleUrl": article_url,
                "mode": mode,
            },
        )

    def get_article_detail_v2(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Details

        Retrieves structured details for a WeChat Official Account article by URL. Use it to collect a known article for parsing, indexing, or structured content archiving.

        Args:
            article_url: WeChat Official Account article URL used to fetch structured article detail fields and an HTML content fragment.
        """
        return self._get(
            "/api/weixin/get-article-detail/v2",
            {
                "articleUrl": article_url,
            },
        )

    def get_article_detail_v3(
        self,
        *,
        article_url: str,
        mode: str | None = "TEXT",
    ) -> ApiResponse[Any]:
        """
        Article Details

        Retrieves details for a WeChat Official Account article that may include video content, with selectable plain-text or rich-text mode. Use it to process known articles containing video material.

        Args:
            article_url: WeChat Official Account article URL used to fetch article details with video-related fields when available.
            mode: Article body format. TEXT returns plain text, and RICH_TEXT returns rich text when supported.  Available Values: - `TEXT`: Plain text article detail - `RICH_TEXT`: Rich text article detail
        """
        return self._get(
            "/api/weixin/get-article-detail/v3",
            {
                "articleUrl": article_url,
                "mode": mode,
            },
        )

    def get_article_detail_v4(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Details

        Retrieves an HTML representation of a WeChat Official Account article by URL. Use it to preserve, render, or archive a known article as a web document.

        Args:
            article_url: WeChat Official Account article URL used to fetch a full HTML document for rendering or archiving.
        """
        return self._get(
            "/api/weixin/get-article-detail/v4",
            {
                "articleUrl": article_url,
            },
        )

    def get_article_detail_v5(
        self,
        *,
        article_url: str,
    ) -> ApiResponse[Any]:
        """
        Article Details

        Retrieves lightweight information for a WeChat Official Account article by URL. Use it to perform a quick article lookup before deeper content, metric, or comment retrieval.

        Args:
            article_url: WeChat Official Account article URL used to fetch lightweight article metadata and status information.
        """
        return self._get(
            "/api/weixin/get-article-detail/v5",
            {
                "articleUrl": article_url,
            },
        )

    def get_article_comment_v1(
        self,
        *,
        article_url: str,
        buffer: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Article Comments

        Retrieves top-level comments for a WeChat Official Account article by URL, with an optional buffer cursor for pagination. Use it to review reader discussion or continue through comment pages for a known article.

        Args:
            article_url: WeChat Official Account article URL used to fetch top-level article comments.
            buffer: Comment pagination buffer returned by the previous response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
        """
        return self._post(
            "/api/weixin/get-article-comment/v1",
            {},
            data={
                "articleUrl": article_url,
                "buffer": buffer,
            },
            token_in_form=True,
        )

    def get_article_sub_comment_v1(
        self,
        *,
        article_url: str,
        content_id: str,
    ) -> ApiResponse[Any]:
        """
        Article Comment Replies

        Retrieves replies under a top-level comment for a WeChat Official Account article, identified by article URL and contentId. Use it to inspect threaded discussion beneath a known comment.

        Args:
            article_url: WeChat Official Account article URL used to fetch replies under a top-level comment.
            content_id: Top-level comment content id used to fetch nested comment replies.
        """
        return self._get(
            "/api/weixin/get-article-sub-comment/v1",
            {
                "articleUrl": article_url,
                "contentId": content_id,
            },
        )

    def search_article_hot_v1(
        self,
        *,
        start_day: str,
        end_day: str,
        keyword: str | None = "",
        publish_type: str | None = "IMAGE_TEXT",
        category: str | None = "ALL",
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Hot Article Search

        Searches hot WeChat Official Account articles within a required date range of up to 7 days, with optional keyword plus publication-format, category, and page filters. Use it to identify high-interest content for trend research or editorial benchmarking.

        Args:
            start_day: Start date for hot article search in yyyy-MM-dd format. The range through endDay must not exceed 7 days.
            end_day: End date for hot article search in yyyy-MM-dd format. It must be on or after startDay and no more than 7 days later.
            keyword: Optional keyword used to filter hot WeChat Official Account articles.
            publish_type: Publish type filter for hot WeChat Official Account article results.  Available Values: - `IMAGE_TEXT`: Image and text article - `VIDEO`: Pure video article - `AUDIO`: Pure audio or music article - `IMAGE`: Pure image article - `TEXT`: Pure text article - `REPRINT`: Reprinted article
            category: Category filter for hot WeChat Official Account article results.  Available Values: - `ALL`: All categories - `INTERNATIONAL`: International - `SPORTS`: Sports - `ENTERTAINMENT`: Entertainment - `SOCIETY`: Society - `FINANCE`: Finance - `CURRENT_AFFAIRS`: Current affairs - `TECHNOLOGY`: Technology - `EMOTION`: Emotion - `AUTOMOTIVE`: Automotive - `EDUCATION`: Education - `FASHION`: Fashion - `GAMES`: Games - `MILITARY`: Military - `TRAVEL`: Travel - `FOOD`: Food - `CULTURE`: Culture - `HEALTH`: Health - `HUMOR`: Humor - `HOME`: Home - `ANIMATION`: Animation - `PETS`: Pets - `PARENTING`: Parenting - `ASTROLOGY`: Astrology - `HISTORY`: History - `MUSIC`: Music - `UNCATEGORIZED`: Uncategorized - `COMPREHENSIVE`: Comprehensive - `WORKPLACE`: Workplace - `AGRICULTURE`: Agriculture - `ELDERLY_CARE`: Elderly care
            page: Page number starting from 1 for hot WeChat Official Account article results.
        """
        return self._get(
            "/api/weixin/search-article-hot/v1",
            {
                "startDay": start_day,
                "endDay": end_day,
                "keyword": keyword,
                "publishType": publish_type,
                "category": category,
                "page": page,
            },
        )

    def search_article_v1(
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
        Article Search

        Searches WeChat Official Account articles by keyword with publish-time and sort filters plus page, offset, and continuation-state pagination. Use it to discover recent or high-interest articles for topic research and content monitoring.

        Args:
            keyword: Search keyword for WeChat Official Account articles.
            cookies_buffer: Opaque pagination state returned by the previous WeChat web search response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
            current_page: Current page number starting from 1 for WeChat web search pagination.
            offset: Search result offset returned by the previous response. Use 0 for the first page.
            publish_time_type: Publish time filter for WeChat Official Account article web search.  Available Values: - `ALL`: All time - `ONE_DAY`: Last day - `SEVEN_DAYS`: Last seven days - `HALF_YEAR`: Last half year
            sort_type: Sort order for WeChat Official Account article web search results.  Available Values: - `COMPREHENSIVE`: Comprehensive sort - `LATEST`: Latest first - `HOT`: Hot first
        """
        return self._post(
            "/api/weixin/search-article/v1",
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

    def search_article_v2(
        self,
        *,
        keyword: str,
        cookies_buffer: str | None = "",
        current_page: int | None = 1,
        offset: int | None = 0,
        sub_search_type: str | None = "ALL",
    ) -> ApiResponse[Any]:
        """
        Article Search

        Searches WeChat Official Account articles by keyword within a selected category such as followed accounts, latest, recently read, or hot, with continuation pagination. Use it to focus article discovery on a particular result stream.

        Args:
            keyword: Search keyword for categorized WeChat Official Account article web search.
            cookies_buffer: Opaque pagination state returned by the previous WeChat web search response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
            current_page: Current page number starting from 1 for WeChat web search pagination.
            offset: Search result offset returned by the previous response. Use 0 for the first page.
            sub_search_type: Subcategory filter for categorized WeChat Official Account article web search.  Available Values: - `ALL`: All - `FOLLOWED`: Followed accounts - `LATEST`: Latest - `RECENT_READ`: Recently read - `HOT`: Hot
        """
        return self._post(
            "/api/weixin/search-article/v2",
            {},
            data={
                "keyword": keyword,
                "cookies_buffer": cookies_buffer,
                "currentPage": current_page,
                "offset": offset,
                "subSearchType": sub_search_type,
            },
            token_in_form=True,
        )

    def search_miniprogram_v1(
        self,
        *,
        keyword: str,
        cookies_buffer: str | None = "",
        current_page: int | None = 1,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        Mini Program Search

        Searches WeChat Mini Programs by keyword with page, offset, and continuation-state pagination. Use it to discover mini programs related to a brand, service, topic, or product.

        Args:
            keyword: Search keyword for WeChat mini program web search.
            cookies_buffer: Opaque pagination state returned by the previous WeChat web search response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
            current_page: Current page number starting from 1 for WeChat web search pagination.
            offset: Search result offset returned by the previous response. Use 0 for the first page.
        """
        return self._post(
            "/api/weixin/search-miniprogram/v1",
            {},
            data={
                "keyword": keyword,
                "cookies_buffer": cookies_buffer,
                "currentPage": current_page,
                "offset": offset,
            },
            token_in_form=True,
        )

    def search_wechat_index_v1(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        WeChat Index Search

        Queries WeChat Index for a keyword. Use it to examine trend interest within WeChat before planning content, campaigns, or further article research.

        Args:
            keyword: Keyword used to query WeChat Index trend signals.
        """
        return self._get(
            "/api/weixin/search-wechat-index/v1",
            {
                "keyword": keyword,
            },
        )

    def search_suggestions_v1(
        self,
        *,
        keyword: str,
        business_type: str | None = "ALL",
    ) -> ApiResponse[Any]:
        """
        Search Suggestions

        Retrieves WeChat search suggestions for a keyword, optionally scoped by a supported business type. Use it to expand or refine a query before a targeted WeChat search.

        Args:
            keyword: Keyword used to fetch WeChat search suggestions.
            business_type: WeChat search business type used to scope suggestion results.  Available Values: - `ALL`: All - `ACCOUNT`: Official accounts - `ARTICLE`: Articles - `CHANNEL`: Channels - `MOMENTS`: Moments - `LIVE`: Live - `EMOJI`: Emoji - `AUDIO`: Audio - `BOOK`: Books - `WECHAT_INDEX`: WeChat index - `NEWS`: News - `MINI_PROGRAM`: Mini programs - `ENCYCLOPEDIA`: Encyclopedia
        """
        return self._get(
            "/api/weixin/search-suggestions/v1",
            {
                "keyword": keyword,
                "businessType": business_type,
            },
        )

    def search_account_v1(
        self,
        *,
        keyword: str,
        page: int | None = 1,
    ) -> ApiResponse[Any]:
        """
        Account Search

        Searches WeChat Official Accounts by keyword with page-number pagination and one result per page. Use it to find an account by name or related term before profile or article lookup.

        Args:
            keyword: Search keyword for WeChat Official Account profiles.
            page: Page number starting from 1 for WeChat Official Account profile search.
        """
        return self._post(
            "/api/weixin/search-account/v1",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def search_account_v2(
        self,
        *,
        keyword: str,
        cookies_buffer: str | None = "",
        current_page: int | None = 1,
        offset: int | None = 0,
    ) -> ApiResponse[Any]:
        """
        Account Search

        Searches WeChat Official Accounts by keyword with page, offset, and continuation-state pagination. Use it to browse broader account results for creator, brand, or publisher discovery.

        Args:
            keyword: Search keyword for WeChat Official Account web search.
            cookies_buffer: Opaque pagination state returned by the previous WeChat web search response. Leave it empty for the first page. For this POST endpoint, send it in an application/x-www-form-urlencoded form body.
            current_page: Current page number starting from 1 for WeChat web search pagination.
            offset: Search result offset returned by the previous response. Use 0 for the first page.
        """
        return self._post(
            "/api/weixin/search-account/v2",
            {},
            data={
                "keyword": keyword,
                "cookies_buffer": cookies_buffer,
                "currentPage": current_page,
                "offset": offset,
            },
            token_in_form=True,
        )

    def get_account_original_count_v1(
        self,
        *,
        ghid: str | None = "",
        url: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Account Original Article Count

        Retrieves the original-article count for a WeChat Official Account identified by ghid or article URL. Use it to compare original publishing activity across known accounts.

        Args:
            ghid: WeChat Official Account original identifier, using the gh_ prefix returned by WeChat. Use either ghid or url.
            url: WeChat Official Account article URL used to identify the account. Use either ghid or url.
        """
        return self._get(
            "/api/weixin/get-account-original-count/v1",
            {
                "ghid": ghid,
                "url": url,
            },
        )

    def get_account_principal_info_v1(
        self,
        *,
        biz: str | None = "",
        url: str | None = "",
        wxid: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Account Principal Info

        Retrieves principal information for a WeChat Official Account identified by biz ID, article URL, or wxid. Use it to review the ownership or operating entity behind a known account.

        Args:
            biz: WeChat Official Account biz id. Use one of biz, url, or wxid.
            url: WeChat Official Account article URL used to identify the account. Use one of biz, url, or wxid.
            wxid: WeChat Official Account wxid used to identify the account. Use one of biz, url, or wxid.
        """
        return self._get(
            "/api/weixin/get-account-principal-info/v1",
            {
                "biz": biz,
                "url": url,
                "wxid": wxid,
            },
        )

    def get_account_basic_info_v1(
        self,
        *,
        name: str,
    ) -> ApiResponse[Any]:
        """
        Account Basic Info

        Retrieves basic profile information for a WeChat Official Account by account name. Use it to identify or enrich a known account before article, ownership, or publishing research.

        Args:
            name: WeChat Official Account name used to fetch basic profile information.
        """
        return self._get(
            "/api/weixin/get-account-basic-info/v1",
            {
                "name": name,
            },
        )

    def convert_article_link_v1(
        self,
        *,
        link: str,
    ) -> ApiResponse[Any]:
        """
        Article Link Conversion

        Expands a WeChat Official Account article link to its resolved long-form destination. Use it to normalize a short or intermediate link before article lookup or collection.

        Args:
            link: WeChat Official Account article short link or intermediate link to convert.
        """
        return self._get(
            "/api/weixin/convert-article-link/v1",
            {
                "link": link,
            },
        )
