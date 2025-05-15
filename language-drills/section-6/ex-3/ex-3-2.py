from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., alias="user_id")

data = {"user_id": 101}
u = User(**data)
print(u)
print(u.dict(by_alias=True))
