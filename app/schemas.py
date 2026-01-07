from pydantic import BaseModel
from typing import Dict, Any

class IntegrationInput(BaseModel):
    source: str
    type: str
    payload: Dict[str, Any]

class ProductOutput(BaseModel):
    product_id: str
    name: str
    price: int
    currency: str
    stock: int
    source: str
