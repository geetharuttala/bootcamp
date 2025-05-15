from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u1 = User("Geetha", 24)
u2 = User("Geetha", 30)
print("Equal?", u1 == u2)
