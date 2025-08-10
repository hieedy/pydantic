from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True # Default value for in_stock is True
