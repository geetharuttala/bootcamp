from pydantic import BaseModel

class User(BaseModel):
    """
    User model represents a registered user in the system.
    Contains user ID and name.
    """
    id: int
    name: str

u = User(id=1, name="Geetha")
print(u)
