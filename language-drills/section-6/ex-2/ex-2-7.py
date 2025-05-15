from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

u = User(name="Geetha", age=30)
print(u.dict())
print(u.json())
