from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int

try:
    u = User(name="Mahi", age="not a number")
except ValidationError as e:
    print(e)
