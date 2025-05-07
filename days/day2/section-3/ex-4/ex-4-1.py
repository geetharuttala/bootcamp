from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Alice", 30)
print(u)
