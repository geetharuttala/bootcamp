from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

u = User("Geetha", 24)
print(u)
# u.age = 40  # Uncommenting this will raise FrozenInstanceError
