from __future__ import annotations

from typing import Any

from justoneapi._resource import BaseResource
from justoneapi._response import ApiResponse


class Field1688Resource(BaseResource):
    """Generated resource for 1688."""

    def get_item_detail_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves the public product detail for a 1688 wholesale listing by item ID. Use it to review a known offer during product sourcing or catalog research.

        Args:
            item_id: A unique product identifier on 1688.
        """
        return self._get(
            "/api/1688/get-item-detail/v1",
            {
                "itemId": item_id,
            },
        )

    def get_item_detail_v2(
        self,
        *,
        item_id: str,
        scene: str | None = None,
        optimize_title: bool | None = False,
        language: str | None = "zh",
    ) -> ApiResponse[Any]:
        """
        Product Details

        Retrieves 1688 product details by item ID with an optional output language and dropshipping scene. Use it to inspect a known product during sourcing and catalog research.

        Args:
            item_id: 1688 product ID.
            scene: Optional dropshipping pricing scene.  Available Values: - `drop_shipping`: Dropshipping
            optimize_title: Optimize Chinese titles by removing non-core words.
            language: Output language.  Available Values: - `en`: English - `zh`: Chinese - `ru`: Russian - `th`: Thai - `pt`: Portuguese - `es`: Spanish - `tr`: Turkish - `vi`: Vietnamese - `ja`: Japanese - `ko`: Korean
        """
        return self._get(
            "/api/1688/get-item-detail/v2",
            {
                "itemId": item_id,
                "scene": scene,
                "optimizeTitle": optimize_title,
                "language": language,
            },
        )

    def get_item_detail_by_url_v1(
        self,
        *,
        url: str,
        scene: str | None = None,
        optimize_title: bool | None = False,
        language: str | None = "zh",
    ) -> ApiResponse[Any]:
        """
        Product Details [URL]

        Retrieves 1688 product details by product URL with an optional output language. Use it to inspect a known listing during sourcing and catalog research.

        Args:
            url: 1688 product URL.
            scene: Optional dropshipping pricing scene.  Available Values: - `drop_shipping`: Dropshipping
            optimize_title: Optimize Chinese titles by removing non-core words.
            language: Output language.  Available Values: - `en`: English - `zh`: Chinese - `ru`: Russian - `th`: Thai - `pt`: Portuguese - `es`: Spanish - `tr`: Turkish - `vi`: Vietnamese - `ja`: Japanese - `ko`: Korean
        """
        return self._get(
            "/api/1688/get-item-detail-by-url/v1",
            {
                "url": url,
                "scene": scene,
                "optimizeTitle": optimize_title,
                "language": language,
            },
        )

    def get_item_description_images_v1(
        self,
        *,
        item_id: str,
    ) -> ApiResponse[Any]:
        """
        Product Description Images

        Retrieves 1688 product description images by item ID. Use it to review listing descriptions during catalog preparation and product research.

        Args:
            item_id: 1688 product ID.
        """
        return self._get(
            "/api/1688/get-item-description-images/v1",
            {
                "itemId": item_id,
            },
        )

    def get_item_rating_list_v1(
        self,
        *,
        item_id: str,
        page: int | None = 1,
        sort_type: str | None = "default",
    ) -> ApiResponse[Any]:
        """
        Product Reviews

        Retrieves 1688 product reviews by item ID with pagination and default or latest sorting. Use it to review buyer feedback during product sourcing.

        Args:
            item_id: 1688 product ID.
            page: Page number, starting at 1.
            sort_type: Review sort order.  Available Values: - `default`: Default order - `latest`: Latest reviews first
        """
        return self._get(
            "/api/1688/get-item-rating-list/v1",
            {
                "itemId": item_id,
                "page": page,
                "sortType": sort_type,
            },
        )

    def get_item_shipping_v1(
        self,
        *,
        item_id: str,
        province: str,
        total_quantity: int | None = 1,
        total_weight: float | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Shipping Fee

        Retrieves a 1688 product shipping estimate for a Chinese province using quantity and optional total weight. Use it to estimate domestic procurement shipping costs.

        Args:
            item_id: 1688 product ID.
            province: Chinese province name or abbreviation, for example Guangdong or gd.
            total_quantity: Total number of items to ship.
            total_weight: Total shipment weight in kilograms.
        """
        return self._get(
            "/api/1688/get-item-shipping/v1",
            {
                "itemId": item_id,
                "province": province,
                "totalQuantity": total_quantity,
                "totalWeight": total_weight,
            },
        )

    def search_item_list_v1(
        self,
        *,
        keyword: str,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Searches 1688 wholesale product listings by keyword. Use it to discover candidate products or suppliers during sourcing and market research.

        Args:
            keyword: Search keyword.
        """
        return self._get(
            "/api/1688/search-item-list/v1",
            {
                "keyword": keyword,
            },
        )

    def search_item_list_v2(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        page_size: int | None = 20,
        sort: str | None = "default",
        moq: int | None = None,
        price_start: str | None = None,
        price_end: str | None = None,
        new_arrival: bool | None = None,
        support_dropshipping: bool | None = None,
        free_shipping: bool | None = None,
        is_super_factory: bool | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Search

        Searches 1688 products by keyword with pagination, sorting, price ranges and optional sourcing filters. Use it to discover products during procurement and market research.

        Args:
            keyword: Search keyword.
            page: Page number, starting at 1.
            page_size: Number of items requested per page. The returned count may differ.
            sort: Product sort order.  Available Values: - `default`: Default order - `sales`: Sales order - `price_up`: Price ascending - `price_down`: Price descending
            moq: Minimum order quantity filter.
            price_start: Minimum price filter in CNY.
            price_end: Maximum price filter in CNY.
            new_arrival: Filter for new products.
            support_dropshipping: Filter for support for dropshipping.
            free_shipping: Filter for free shipping.
            is_super_factory: Optional super-factory filter.
        """
        return self._get(
            "/api/1688/search-item-list/v2",
            {
                "keyword": keyword,
                "page": page,
                "pageSize": page_size,
                "sort": sort,
                "moq": moq,
                "priceStart": price_start,
                "priceEnd": price_end,
                "newArrival": new_arrival,
                "supportDropshipping": support_dropshipping,
                "freeShipping": free_shipping,
                "isSuperFactory": is_super_factory,
            },
        )

    def search_item_by_image_v1(
        self,
        *,
        img_url: str,
        page: int | None = 1,
        page_size: int | None = 20,
        sort: str | None = "default",
        moq: int | None = None,
        price_start: str | None = None,
        price_end: str | None = None,
        support_dropshipping: bool | None = None,
        is_factory: bool | None = None,
        verified_supplier: bool | None = None,
        free_shipping: bool | None = None,
        new_arrival: bool | None = None,
    ) -> ApiResponse[Any]:
        """
        Product Search by Image

        Searches 1688 products by image with pagination, sorting and optional sourcing filters. Use it to find matching products during visual sourcing.

        Args:
            img_url: Image URL or image reference returned by Image Conversion. Convert external images for the selected search target before searching.
            page: Page number, starting at 1.
            page_size: Number of items requested per page. The returned count may differ.
            sort: Product sort order.  Available Values: - `default`: Default order - `sales`: Sales order - `price_up`: Price ascending - `price_down`: Price descending
            moq: Minimum order quantity filter.
            price_start: Minimum price filter in CNY.
            price_end: Maximum price filter in CNY.
            support_dropshipping: Filter for support for dropshipping.
            is_factory: Filter by factory status.
            verified_supplier: Filter for verified sellers.
            free_shipping: Filter for free shipping.
            new_arrival: Filter for new products.
        """
        return self._get(
            "/api/1688/search-item-by-image/v1",
            {
                "imgUrl": img_url,
                "page": page,
                "pageSize": page_size,
                "sort": sort,
                "moq": moq,
                "priceStart": price_start,
                "priceEnd": price_end,
                "supportDropshipping": support_dropshipping,
                "isFactory": is_factory,
                "verifiedSupplier": verified_supplier,
                "freeShipping": free_shipping,
                "newArrival": new_arrival,
            },
        )

    def get_shop_item_list_v1(
        self,
        *,
        member_id: str,
        page: int | None = 1,
        page_size: int | None = 20,
        sort: str | None = "default",
        shop_cat_id: str | None = None,
        price_start: str | None = None,
        price_end: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Shop Products [ID]

        Retrieves 1688 shop products by seller member ID with pagination, sorting and optional category and price filters. Use it to research a shop product catalog.

        Args:
            member_id: Seller member ID.
            page: Page number, starting at 1.
            page_size: Number of items requested per page. The returned count may differ.
            sort: Shop product sort order.  Available Values: - `default`: Default order - `sales`: Sales order - `price_up`: Price ascending - `price_down`: Price descending - `time_up`: Time ascending - `time_down`: Time descending
            shop_cat_id: Shop category ID.
            price_start: Minimum price filter in CNY.
            price_end: Maximum price filter in CNY.
        """
        return self._get(
            "/api/1688/get-shop-item-list/v1",
            {
                "memberId": member_id,
                "page": page,
                "pageSize": page_size,
                "sort": sort,
                "shopCatId": shop_cat_id,
                "priceStart": price_start,
                "priceEnd": price_end,
            },
        )

    def get_shop_item_list_by_url_v1(
        self,
        *,
        shop_url: str,
        page: int | None = 1,
        page_size: int | None = 20,
        sort: str | None = "default",
        cat: str | None = None,
        cat_type: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Shop Products [URL]

        Retrieves 1688 shop products by shop homepage URL with pagination, sorting and optional category filters. Use it to research a shop product catalog.

        Args:
            shop_url: 1688 shop homepage URL.
            page: Page number, starting at 1.
            page_size: Number of items requested per page. The returned count may differ.
            sort: Shop product sort order.  Available Values: - `default`: Default order - `sales`: Sales order - `price_up`: Price ascending - `price_down`: Price descending - `time_up`: Time ascending - `time_down`: Time descending
            cat: Optional category ID filter.
            cat_type: Optional category mode: 0 or 1.  Available Values: - `0`: Category mode 0 - `1`: Category mode 1
        """
        return self._get(
            "/api/1688/get-shop-item-list-by-url/v1",
            {
                "shopUrl": shop_url,
                "page": page,
                "pageSize": page_size,
                "sort": sort,
                "cat": cat,
                "catType": cat_type,
            },
        )

    def get_shop_info_v1(
        self,
        *,
        shop_url: str | None = None,
        member_id: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Shop Information

        Retrieves 1688 shop information by shop URL or seller member ID. Use it to research a known shop during procurement.

        Args:
            shop_url: 1688 shop homepage URL. Supply shopUrl or memberId.
            member_id: Seller member ID. Supply memberId or shopUrl.
        """
        return self._get(
            "/api/1688/get-shop-info/v1",
            {
                "shopUrl": shop_url,
                "memberId": member_id,
            },
        )

    def get_shop_category_v1(
        self,
        *,
        shop_url: str | None = None,
        member_id: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Shop Categories

        Retrieves all categories for a 1688 shop by shop URL or seller member ID. Use it to navigate a shop catalog during product sourcing.

        Args:
            shop_url: 1688 shop homepage URL. Supply shopUrl or memberId.
            member_id: Seller member ID. Supply memberId or shopUrl.
        """
        return self._get(
            "/api/1688/get-shop-category/v1",
            {
                "shopUrl": shop_url,
                "memberId": member_id,
            },
        )

    def get_category_info_v1(
        self,
        *,
        cat_id: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Category Information

        Retrieves 1688 category information by category ID, or root categories when no ID is supplied. Use it to navigate categories during product sourcing.

        Args:
            cat_id: 1688 platform category ID.
        """
        return self._get(
            "/api/1688/get-category-info/v1",
            {
                "catId": cat_id,
            },
        )

    def get_category_item_list_v1(
        self,
        *,
        cat_id: str,
        page: int | None = 1,
        is_super_factory: bool | None = None,
        support_dropshipping: bool | None = None,
        free_shipping: bool | None = None,
    ) -> ApiResponse[Any]:
        """
        Category Products

        Retrieves 1688 products by platform category ID with pagination and optional sourcing filters. Use it to discover products within a known category.

        Args:
            cat_id: 1688 platform category ID.
            page: Page number, starting at 1.
            is_super_factory: Optional super-factory filter.
            support_dropshipping: Filter for support for dropshipping.
            free_shipping: Filter for free shipping.
        """
        return self._get(
            "/api/1688/get-category-item-list/v1",
            {
                "catId": cat_id,
                "page": page,
                "isSuperFactory": is_super_factory,
                "supportDropshipping": support_dropshipping,
                "freeShipping": free_shipping,
            },
        )

    def get_category_item_list_v2(
        self,
        *,
        cat_id: str,
        language: str | None = "zh",
        page: int | None = 1,
        page_size: int | None = 20,
        sort: str | None = "default",
        price_start: str | None = None,
        price_end: str | None = None,
        new_arrival: bool | None = None,
        support_dropshipping: bool | None = None,
        free_shipping: bool | None = None,
        is_super_factory: bool | None = None,
    ) -> ApiResponse[Any]:
        """
        Category Products

        Retrieves 1688 products by category ID with output language, pagination, sorting and price filters. Use it to discover category products for multilingual sourcing.

        Args:
            cat_id: 1688 platform category ID.
            language: Output language.  Available Values: - `en`: English - `zh`: Chinese - `ru`: Russian - `vi`: Vietnamese - `ja`: Japanese - `ko`: Korean
            page: Page number, starting at 1.
            page_size: Number of items requested per page. The returned count may differ.
            sort: Product sort order.  Available Values: - `default`: Default order - `sales`: Sales order - `price_up`: Price ascending - `price_down`: Price descending
            price_start: Minimum price filter in CNY.
            price_end: Maximum price filter in CNY.
            new_arrival: Filter for new products.
            support_dropshipping: Filter for support for dropshipping.
            free_shipping: Filter for free shipping.
            is_super_factory: Optional super-factory filter.
        """
        return self._get(
            "/api/1688/get-category-item-list/v2",
            {
                "catId": cat_id,
                "language": language,
                "page": page,
                "pageSize": page_size,
                "sort": sort,
                "priceStart": price_start,
                "priceEnd": price_end,
                "newArrival": new_arrival,
                "supportDropshipping": support_dropshipping,
                "freeShipping": free_shipping,
                "isSuperFactory": is_super_factory,
            },
        )

    def search_factory_v1(
        self,
        *,
        keyword: str,
        page: int | None = 1,
        page_size: int | None = 20,
        sort: str | None = "default",
    ) -> ApiResponse[Any]:
        """
        Factory Search

        Searches 1688 factories by keyword with pagination and default or repurchase-rate sorting. Use it to discover manufacturers during procurement research.

        Args:
            keyword: Factory search keyword.
            page: Page number, starting at 1.
            page_size: Number of items requested per page. The returned count may differ.
            sort: Factory sort order.  Available Values: - `default`: Default order - `repurchase_rate`: Repurchase-rate order
        """
        return self._get(
            "/api/1688/search-factory/v1",
            {
                "keyword": keyword,
                "page": page,
                "pageSize": page_size,
                "sort": sort,
            },
        )

    def search_cross_border_item_list_v1(
        self,
        *,
        keyword: str | None = None,
        cat_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        language: str | None = "en",
        sort: str | None = "default",
        price_start: str | None = None,
        price_end: str | None = None,
        new_arrival: bool | None = None,
        support_dropshipping: bool | None = None,
        free_shipping: bool | None = None,
        is_super_factory: bool | None = None,
    ) -> ApiResponse[Any]:
        """
        Cross-border Product Search

        Searches 1688 cross-border products by keyword or category with language selection, pagination and sourcing filters. Use it to discover products for multilingual procurement.

        Args:
            keyword: Search keyword. Supply keyword or catId.
            cat_id: 1688 category ID. Supply catId or keyword.
            page: Page number, starting at 1.
            page_size: Number of items requested per page. The returned count may differ.
            language: Output language.  Available Values: - `en`: English - `zh`: Chinese - `ru`: Russian - `vi`: Vietnamese - `ja`: Japanese - `ko`: Korean
            sort: Product sort order.  Available Values: - `default`: Default order - `sales`: Sales order - `price_up`: Price ascending - `price_down`: Price descending
            price_start: Minimum price filter in CNY.
            price_end: Maximum price filter in CNY.
            new_arrival: Filter for new products.
            support_dropshipping: Filter for support for dropshipping.
            free_shipping: Filter for free shipping.
            is_super_factory: Optional super-factory filter.
        """
        return self._get(
            "/api/1688/search-cross-border-item-list/v1",
            {
                "keyword": keyword,
                "catId": cat_id,
                "page": page,
                "pageSize": page_size,
                "language": language,
                "sort": sort,
                "priceStart": price_start,
                "priceEnd": price_end,
                "newArrival": new_arrival,
                "supportDropshipping": support_dropshipping,
                "freeShipping": free_shipping,
                "isSuperFactory": is_super_factory,
            },
        )

    def search_cross_border_item_by_image_v1(
        self,
        *,
        img_url: str,
        language: str | None = "en",
        page: int | None = 1,
        page_size: int | None = 20,
        sort: str | None = "default",
        price_start: str | None = None,
        price_end: str | None = None,
        support_dropshipping: bool | None = None,
        is_factory: bool | None = None,
        verified_supplier: bool | None = None,
        free_shipping: bool | None = None,
        new_arrival: bool | None = None,
    ) -> ApiResponse[Any]:
        """
        Cross-border Image Search

        Searches 1688 cross-border products by image with language selection, pagination, sorting and sourcing filters. Use it to find products for multilingual visual sourcing.

        Args:
            img_url: Image URL or image reference returned by Image Conversion. Convert external images for the selected search target before searching.
            language: Output language.  Available Values: - `en`: English - `zh`: Chinese - `ru`: Russian - `th`: Thai - `pt`: Portuguese - `es`: Spanish - `tr`: Turkish - `vi`: Vietnamese - `ja`: Japanese - `ko`: Korean
            page: Page number, starting at 1.
            page_size: Number of items requested per page. The returned count may differ.
            sort: Product sort order.  Available Values: - `default`: Default order - `sales`: Sales order - `price_up`: Price ascending - `price_down`: Price descending
            price_start: Minimum price filter in CNY.
            price_end: Maximum price filter in CNY.
            support_dropshipping: Filter for support for dropshipping.
            is_factory: Filter by factory status.
            verified_supplier: Filter for verified sellers.
            free_shipping: Filter for free shipping.
            new_arrival: Filter for new products.
        """
        return self._get(
            "/api/1688/search-cross-border-item-by-image/v1",
            {
                "imgUrl": img_url,
                "language": language,
                "page": page,
                "pageSize": page_size,
                "sort": sort,
                "priceStart": price_start,
                "priceEnd": price_end,
                "supportDropshipping": support_dropshipping,
                "isFactory": is_factory,
                "verifiedSupplier": verified_supplier,
                "freeShipping": free_shipping,
                "newArrival": new_arrival,
            },
        )

    def search_cross_border_item_by_image_v2(
        self,
        *,
        img_url: str,
        language: str | None = "en",
        page: int | None = 1,
        page_size: int | None = 20,
        sort: str | None = "default",
        price_start: str | None = None,
        price_end: str | None = None,
        support_dropshipping: bool | None = None,
        is_factory: bool | None = None,
        verified_supplier: bool | None = None,
        free_shipping: bool | None = None,
        new_arrival: bool | None = None,
    ) -> ApiResponse[Any]:
        """
        Cross-border Image Search

        Searches 1688 cross-border products by image with language selection, pagination, sorting and sourcing filters. Use it to find products for multilingual visual sourcing.

        Args:
            img_url: Image reference returned by Image Conversion with searchApiEndpoint=cross_border_v2. Convert full image URLs before searching.
            language: Output language.  Available Values: - `en`: English - `zh`: Chinese - `ru`: Russian - `vi`: Vietnamese - `ja`: Japanese - `ko`: Korean
            page: Page number, starting at 1.
            page_size: Number of items requested per page. The returned count may differ.
            sort: Product sort order.  Available Values: - `default`: Default order - `sales`: Sales order - `price_up`: Price ascending - `price_down`: Price descending
            price_start: Minimum price filter in CNY.
            price_end: Maximum price filter in CNY.
            support_dropshipping: Filter for support for dropshipping.
            is_factory: Filter by factory status.
            verified_supplier: Filter for verified sellers.
            free_shipping: Filter for free shipping.
            new_arrival: Filter for new products.
        """
        return self._get(
            "/api/1688/search-cross-border-item-by-image/v2",
            {
                "imgUrl": img_url,
                "language": language,
                "page": page,
                "pageSize": page_size,
                "sort": sort,
                "priceStart": price_start,
                "priceEnd": price_end,
                "supportDropshipping": support_dropshipping,
                "isFactory": is_factory,
                "verifiedSupplier": verified_supplier,
                "freeShipping": free_shipping,
                "newArrival": new_arrival,
            },
        )

    def convert_image_v1(
        self,
        *,
        img_base64: str | None = None,
        search_api_endpoint: str | None = "standard",
        url: str | None = None,
    ) -> ApiResponse[Any]:
        """
        Image Conversion

        Converts an image URL or JPEG Base64 input into an image reference for a selected 1688 image search endpoint. Use it to prepare external images for visual product sourcing.

        Args:
            img_base64: JPEG image encoded as Base64 without a data URI prefix; decoded size must not exceed 100 KB.
            search_api_endpoint: Image search target for the converted reference.
            url: Image URL. Supply either url or imgBase64.
        """
        return self._post(
            "/api/1688/convert-image/v1",
            {},
            json={
                "imgBase64": img_base64,
                "searchApiEndpoint": search_api_endpoint,
                "url": url,
            },
        )
