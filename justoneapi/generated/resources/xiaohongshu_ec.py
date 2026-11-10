from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class XiaohongshuEcResource(BaseResource):
    """Generated resource for Xiaohongshu E-commerce (RedNote)."""

    def search_products_v1(
        self,
        *,
        keyword: str,
        page: str | None = None,
        search_id: str | None = "",
    ) -> ApiResponse[Any]:
        """
        Product Search

        Searches Xiaohongshu E-commerce (RedNote) products by keyword with page and search-ID pagination; pages after the first require the search ID returned by the initial search. Use it to discover marketplace products and continue through multi-page results.

        Args:
            keyword: Search keyword.
            page: Page number, starting from 1.
            search_id: Search ID returned by the first-page response; required when page is greater than 1.
        """
        return self._get(
            "/api/xiaohongshu-ec/search-products/v1",
            {
                "keyword": keyword,
                "page": page,
                "searchId": search_id,
            },
        )

    def get_product_detail_v1(
        self,
        *,
        sku_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Detail

        Retrieves Xiaohongshu E-commerce (RedNote) product details by SKU ID. Use it to look up a specific marketplace product for product research and catalog workflows.

        Args:
            sku_id: Product SKU ID.
        """
        return self._get(
            "/api/xiaohongshu-ec/get-product-detail/v1",
            {
                "skuId": sku_id,
            },
        )
