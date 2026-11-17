from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class VipshopResource(BaseResource):
    """Generated resource for Vipshop."""

    def get_item_detail_v1(
        self,
        *,
        product_ids: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves Vipshop product details in batches using up to 15 comma-separated product IDs. Use it for product research and catalog monitoring.

        Args:
            product_ids: One to 15 positive decimal product IDs separated by commas. Spaces around each ID are ignored; order and duplicate IDs are preserved.
        """
        return self._get(
            "/api/vipshop/get-item-detail/v1",
            {
                "productIds": product_ids,
            },
        )
