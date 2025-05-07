from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Geetha", 24)
print(u)
