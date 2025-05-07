from pydantic import BaseModel

class User(BaseModel):
    age: int

u = User(age="42")
print(u)
