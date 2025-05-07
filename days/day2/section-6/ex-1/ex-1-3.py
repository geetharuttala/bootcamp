from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

# u = User("Geetha", -1)  # Uncomment to see the error
u = User("Geetha", 24)
print(u)
