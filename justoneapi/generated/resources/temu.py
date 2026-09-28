from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class TemuResource(BaseResource):
    """Generated resource for Temu."""

    def get_homepage_goods_v1(
        self,
        *,
        site: str,
        offset: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Homepage Product Feed

        Retrieves Temu homepage product feed cards for a selected site with offset pagination. Use it for product sourcing, catalog monitoring, and marketplace trend analysis.

        Args:
            site: Temu site used to select the regional homepage feed.  Available Values: - `US`: United States - `EU`: Europe - `UK`: United Kingdom - `CA`: Canada - `AU`: Australia
            offset: Zero-based offset for pagination.
        """
        return self._get(
            "/api/temu/get-homepage-goods/v1",
            {
                "site": site,
                "offset": offset,
            },
        )

    def get_product_detail_v1(
        self,
        *,
        goods_id: str,
        site: str | None = "US",
        slug: str | None = None,
        product_url: str | None = None,
        include_skus: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Full Product Details

        Retrieves full Temu product details by product ID for a selected site, with an option to include SKU data. Use it for product research and catalog analysis.

        Args:
            goods_id: Temu product ID.
            site: Temu regional site. Defaults to US.  Available Values: - `US`: United States - `EU`: Europe - `UK`: United Kingdom - `CA`: Canada - `AU`: Australia
            slug: Product URL slug. Defaults to item.
            product_url: Full Temu product URL, when available.
            include_skus: Whether to include SKU data in the product detail request.
        """
        return self._get(
            "/api/temu/get-product-detail/v1",
            {
                "goodsId": goods_id,
                "site": site,
                "slug": slug,
                "productUrl": product_url,
                "includeSkus": include_skus,
            },
        )

    def get_product_snapshot_v1(
        self,
        *,
        goods_id: str,
        site: str | None = "US",
    ) -> ApiResponse[Any]:
        """
        Product Core Snapshot

        Retrieves a Temu product core snapshot by product ID for a selected site. Use it for product monitoring and catalog research.

        Args:
            goods_id: Temu product ID.
            site: Temu regional site. Defaults to US.  Available Values: - `US`: United States - `EU`: Europe - `UK`: United Kingdom - `CA`: Canada - `AU`: Australia
        """
        return self._get(
            "/api/temu/get-product-snapshot/v1",
            {
                "goodsId": goods_id,
                "site": site,
            },
        )

    def get_category_top_sales_v1(
        self,
        *,
        opt_id: str | None = None,
        site: str | None = "US",
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Category Top Sales

        Retrieves Temu bestselling products in a category for a selected site with page number pagination. Use it for category research and product sourcing.

        Args:
            opt_id: Temu category ID. Defaults to 7320.
            site: Temu regional site. Defaults to US.  Available Values: - `US`: United States - `EU`: Europe - `UK`: United Kingdom - `CA`: Canada - `AU`: Australia
            page: Page number from 1 to 20.
        """
        return self._get(
            "/api/temu/get-category-top-sales/v1",
            {
                "optId": opt_id,
                "site": site,
                "page": page,
            },
        )

    def get_categories_v1(
        self,
        *,
        site: str | None = "US",
    ) -> ApiResponse[Any]:
        """
        Product Category Tree

        Retrieves the Temu product category tree for a selected site. Use it to browse category structure and select categories for product research.

        Args:
            site: Temu regional site. Defaults to US.  Available Values: - `US`: United States - `EU`: Europe - `UK`: United Kingdom - `CA`: Canada - `AU`: Australia
        """
        return self._get(
            "/api/temu/get-categories/v1",
            {
                "site": site,
            },
        )

    def get_product_reviews_v1(
        self,
        *,
        goods_id: str,
        site: str | None = "US",
        page: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Review List

        Retrieves Temu product reviews by product ID for a selected site with page number pagination. Use it to review customer feedback for product research.

        Args:
            goods_id: Temu product ID.
            site: Temu regional site. Defaults to US.  Available Values: - `US`: United States - `EU`: Europe - `UK`: United Kingdom - `CA`: Canada - `AU`: Australia
            page: Page number from 1 to 20.
        """
        return self._get(
            "/api/temu/get-product-reviews/v1",
            {
                "goodsId": goods_id,
                "site": site,
                "page": page,
            },
        )

    def get_mall_reviews_v1(
        self,
        *,
        mall_id: str,
        site: str | None = "US",
        page: str | None = None,
        sort_type: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Store Review List

        Retrieves Temu store reviews by store ID for a selected site with page number pagination and a sort type. Use it for store research and customer feedback analysis.

        Args:
            mall_id: Temu store ID.
            site: Temu regional site. Defaults to US.  Available Values: - `US`: United States - `EU`: Europe - `UK`: United Kingdom - `CA`: Canada - `AU`: Australia
            page: Page number from 1 to 20.
            sort_type: Review sort type. Defaults to 0.
        """
        return self._get(
            "/api/temu/get-mall-reviews/v1",
            {
                "mallId": mall_id,
                "site": site,
                "page": page,
                "sortType": sort_type,
            },
        )

    def get_product_reviews_info_v1(
        self,
        *,
        goods_id: str,
        site: str | None = "US",
    ) -> ApiResponse[Any]:
        """
        Product Review Summary

        Retrieves the Temu product review summary by product ID for a selected site. Use it to assess customer feedback during product research.

        Args:
            goods_id: Temu product ID.
            site: Temu regional site. Defaults to US.  Available Values: - `US`: United States - `EU`: Europe - `UK`: United Kingdom - `CA`: Canada - `AU`: Australia
        """
        return self._get(
            "/api/temu/get-product-reviews-info/v1",
            {
                "goodsId": goods_id,
                "site": site,
            },
        )

    def get_mall_goods_v1(
        self,
        *,
        mall_id: str,
        site: str | None = "US",
        page_number: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Store Product List

        Retrieves Temu store products by store ID for a selected site with page number pagination. Use it for store catalog research and product discovery.

        Args:
            mall_id: Temu store ID.
            site: Temu regional site. Defaults to US.  Available Values: - `US`: United States - `EU`: Europe - `UK`: United Kingdom - `CA`: Canada - `AU`: Australia
            page_number: Page number from 1 to 20.
        """
        return self._get(
            "/api/temu/get-mall-goods/v1",
            {
                "mallId": mall_id,
                "site": site,
                "pageNumber": page_number,
            },
        )

    def search_products_v1(
        self,
        *,
        keyword: str,
        site: str | None = "US",
        offset: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Keyword Product Search

        Searches Temu products by keyword for a selected site with offset pagination. Use it for product discovery and catalog research.

        Args:
            keyword: Keyword used to search Temu products.
            site: Temu regional site. Defaults to US.  Available Values: - `US`: United States - `EU`: Europe - `UK`: United Kingdom - `CA`: Canada - `AU`: Australia
            offset: Zero-based offset for pagination.
        """
        return self._get(
            "/api/temu/search-products/v1",
            {
                "keyword": keyword,
                "site": site,
                "offset": offset,
            },
        )
