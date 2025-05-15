from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def is_adult(self):
        return self.age >= 18

u = User("Geetha", 17)
print("Is adult?", u.is_adult())
