from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u1 = User("Eve", 20)
u2 = User("Eve", 20)
u3 = User("Frank", 30)

print(u1 == u2)
print(u1 == u3)
