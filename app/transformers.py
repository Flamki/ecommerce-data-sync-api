def transform_shopify_product(payload: dict) -> dict:
    return {
        "product_id": payload["id"],
        "name": payload["title"],
        "price": int(payload["price"]),
        "currency": payload["currency"],
        "stock": int(payload["inventory"]),
        "source": "shopify"
    }

def transform_woocommerce_product(payload: dict) -> dict:
    return {
        "product_id": payload["sku"],
        "name": payload["name"],
        "price": int(payload["price"]),
        "currency": payload["currency"],
        "stock": int(payload["stock_quantity"]),
        "source": "woocommerce"
    }
