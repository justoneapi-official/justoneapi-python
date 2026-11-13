from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class JdResource(BaseResource):
    """Generated resource for JD.com."""

    def get_item_detail_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieve JD.com product details for a known item ID. Use it to inspect an individual product after finding its identifier.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
        """
        return self._get(
            "/api/jd/get-item-detail/v1",
            {
                "itemId": item_id,
            },
        )

    def get_item_detail_v3(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieve JD.com product details by item ID. Use it to review product information and description images for catalog research or product displays.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
        """
        return self._get(
            "/api/jd/get-item-detail/v3",
            {
                "itemId": item_id,
            },
        )

    def get_item_detail_v4(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieve JD.com product details by item ID. Use it to review product information and images for catalog research or ecommerce analysis.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
        """
        return self._get(
            "/api/jd/get-item-detail/v4",
            {
                "itemId": item_id,
            },
        )

    def get_item_description_images_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Description Images

        Retrieve JD.com product description images and product attributes by item ID. Use it to review product introductions for catalog research and product presentation.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
        """
        return self._get(
            "/api/jd/get-item-description-images/v1",
            {
                "itemId": item_id,
            },
        )

    def get_item_price_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Price

        Retrieve the current JD.com product price for a known item ID. Use it to check a product's price before catalog comparison or purchase analysis.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
        """
        return self._get(
            "/api/jd/get-item-price/v1",
            {
                "itemId": item_id,
            },
        )

    def get_item_price_v2(
        self,
        *,
        item_ids: str,
    ) -> ApiResponse[Any]:
        """
        Product Price

        Retrieve JD.com product prices for up to 10 comma-separated item IDs in one request. Use it for batch price checks and catalog comparisons.

        Args:
            item_ids: Between 1 and 10 numeric JD.com item IDs, separated by commas without spaces.
        """
        return self._get(
            "/api/jd/get-item-price/v2",
            {
                "itemIds": item_ids,
            },
        )

    def search_item_list_v1(
        self,
        *,
        keyword: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Search JD.com products by keyword with page-based pagination. Use it to discover products and collect item IDs for follow-up lookups.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
        """
        return self._get(
            "/api/jd/search-item-list/v1",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def search_item_list_v2(
        self,
        *,
        keyword: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Search JD.com products by keyword with page-based pagination and sales-volume ordering. Use it to discover popular products and collect item IDs for follow-up lookups.

        Args:
            keyword: Search keyword.
            page: Page number for pagination.
        """
        return self._get(
            "/api/jd/search-item-list/v2",
            {
                "keyword": keyword,
                "page": page,
            },
        )

    def search_item_list_v3(
        self,
        *,
        keyword: str,
        cid: str | None = None,
        cid_level: str | None = None,
        page: str | None = None,
        sort: str | None = None,
        price_interval: str | None = None,
        brand: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Search JD.com products by keyword, including products in advertising placements, with category filtering, pagination, sorting and price-range filters. Use it to research sponsored product visibility and discover products within a selected category.

        Args:
            keyword: Search keyword. Required even when a category is selected.
            cid: Numeric category ID used to filter the search results.
            cid_level: Category ID level: 1 for a first-level category, 2 for a second-level category, or 3 for a third-level category.  Available Values: - `1`: First-level category - `2`: Second-level category - `3`: Third-level category
            page: Page number, starting at 1.
            sort: Sort order for the search results.  Available Values: - `0`: Comprehensive sorting - `1`: Sort by sales volume - `2`: Price, highest first - `3`: Price, lowest first - `6`: Sort by comments
            price_interval: Price range in minimum-maximum format, for example 0-100. Both values must be non-negative and the minimum must not exceed the maximum.
            brand: Brand name, for example iQOO or iPhone.
        """
        return self._get(
            "/api/jd/search-item-list/v3",
            {
                "keyword": keyword,
                "cid": cid,
                "cidLevel": cid_level,
                "page": page,
                "sort": sort,
                "priceInterval": price_interval,
                "brand": brand,
            },
        )

    def get_item_comments_v1(
        self,
        *,
        item_id: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Comments

        Retrieve paginated customer comments for a JD.com product identified by item ID. Use it to review buyer feedback for a known product.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
            page: Page number for paginated comments.
        """
        return self._get(
            "/api/jd/get-item-comments/v1",
            {
                "itemId": item_id,
                "page": page,
            },
        )

    def get_item_comments_v2(
        self,
        *,
        item_id: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Comments

        Retrieve paginated JD.com product comments for a specific SKU. Use it to review buyer feedback for that product.

        Args:
            item_id: A unique product identifier on JD.com (item ID).
            page: Page number for paginated comments.
        """
        return self._get(
            "/api/jd/get-item-comments/v2",
            {
                "itemId": item_id,
                "page": page,
            },
        )

    def get_shop_item_list_v1(
        self,
        *,
        shop_id: str,
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Shop Product List

        Retrieve a page of products from a JD.com shop identified by shop ID. Use it to browse a seller's catalog and collect item IDs for follow-up lookups.

        Args:
            shop_id: A unique shop identifier on JD.com (Shop ID).
            page: Page number for the paginated shop product list.
        """
        return self._get(
            "/api/jd/get-shop-item-list/v1",
            {
                "shopId": shop_id,
                "page": page,
            },
        )
