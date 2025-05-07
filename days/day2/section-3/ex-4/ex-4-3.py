from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

u = User("Diana", 40)
print(u)
