from app.transformers import (
    transform_shopify_product,
    transform_woocommerce_product
)

def route_product(source: str, payload: dict) -> dict:
    if source == "shopify":
        return transform_shopify_product(payload)

    if source == "woocommerce":
        return transform_woocommerce_product(payload)

    raise ValueError("Unsupported source")
