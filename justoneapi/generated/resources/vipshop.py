from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class VipshopResource(BaseResource):
    """Generated resource for Vipshop."""

    def get_item_detail_v1(
        self,
        *,
        product_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves Vipshop product details using one product ID per request. Use it for product research and catalog monitoring.

        Args:
            product_id: Product ID.
        """
        return self._get(
            "/api/vipshop/get-item-detail/v1",
            {
                "productId": product_id,
            },
        )
