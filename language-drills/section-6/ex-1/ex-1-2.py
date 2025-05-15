from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

u = User("Geetha", 24)
print(u)
