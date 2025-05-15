from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., title="Product Name", example="Laptop")
    price: float = Field(..., title="Price in USD", example=999.99)

print(Product.schema_json(indent=2))
