from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(..., description="User's email address")

u = User(email="geetha@example.com")
print(u)
