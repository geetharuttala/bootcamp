from pydantic import BaseModel

class Profile(BaseModel):
    bio: str
    website: str

class User(BaseModel):
    name: str
    age: int
    profile: Profile

data = {
    "name": "Geetha",
    "age": 24,
    "profile": {"bio": "Developer", "website": "https://beyondity.framer.website/"}
}

u = User(**data)
print(u)
