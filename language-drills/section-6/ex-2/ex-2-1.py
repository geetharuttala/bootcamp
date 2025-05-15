from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

data = {"name": "Geetha", "age": 24}
u = User(**data)
print(u)
