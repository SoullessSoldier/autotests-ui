"""Модуль экспериментов с pydantic."""
from pydantic import BaseModel, Field


class Market(BaseModel):
    """Класс рынков."""

    id: int
    name: str


class Product(BaseModel):
    """Класс продуктов."""

    name: str
    price: float = Field(
        ...,
        gt=0,
        description='Price should be greater than 0'
    )
    tags: list[str] = []
    market: Market


product_data = {
    'name': 'Phone',
    'price': 499.99,
    'tags': ['electronics', 'smartphone'],
    'market': {
        'id': 1,
        'name': 'Ozon'
    }
}

product = Product(**product_data)
print(product)
