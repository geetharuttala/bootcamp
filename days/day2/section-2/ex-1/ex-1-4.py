class Person:
    def __init__(self, name):
        self.name = name

p = Person("Bob")
print(getattr(p, "age", "Unknown"))