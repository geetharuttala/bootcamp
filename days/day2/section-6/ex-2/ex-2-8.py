from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    nickname: Optional[str] = None

u = User(name="Geetha")
print(u)
