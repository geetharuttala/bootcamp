from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    age: int

    @validator("name")
    def must_be_capitalized(cls, v):
        if not v[0].isupper():
            raise ValueError("Name must start with a capital letter")
        return v

u = User(name="Geetha", age=30)
print(u)
