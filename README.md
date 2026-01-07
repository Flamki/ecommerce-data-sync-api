# E-commerce Integration Router API

A backend integration service that routes and transforms product data from multiple e-commerce platforms into a unified internal schema.  
This project demonstrates real-world backend integration patterns using FastAPI, including source-based routing, domain-specific transformation logic, and schema validation.

---

## 🚀 Project Overview

In real production systems, data often comes from multiple external platforms (e.g. Shopify, WooCommerce), each using different schemas.  
This service acts as an **integration layer** that:

- Accepts product data from external platforms
- Identifies the source system
- Routes the payload to the correct transformer
- Produces a consistent internal data format for downstream systems

This mirrors how e-commerce data synchronization and transformation systems work in practice.

---

## 🧠 Key Features

- Source-based routing (`shopify`, extensible to other platforms)
- Platform-specific transformation logic
- Unified internal product schema
- Automatic request validation with Pydantic
- Async FastAPI endpoint
- Interactive Swagger API documentation

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **asyncio**
- **REST APIs**

---

## 📦 API Endpoint

### `POST /sync/product`

#### Example Request (Shopify)
```json
{
  "source": "shopify",
  "type": "product",
  "payload": {
    "id": "p_456",
    "title": "Blue Hoodie",
    "price": "1299",
    "currency": "INR",
    "inventory": "12"
  }
}
