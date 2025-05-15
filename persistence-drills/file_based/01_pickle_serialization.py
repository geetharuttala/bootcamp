import pickle

class Person:
    def __init__(self, name: str, institutions: list[str], colleagues: list[str]):
        self.name = name
        self.institutions = institutions
        self.colleagues = colleagues

    def __repr__(self):
        return f"Person(name={self.name}, institutions={self.institutions}, colleagues={self.colleagues})"

person =Person(
    name="Geetha",
    institutions=["NIT Calicut", "Sri Chaitanya"],
    colleagues=["Dhoni", "Mahi"]
)

with open("person.pkl", "wb") as f:
    pickle.dump(person, f)

print("Person object serialized to 'person.pkl'")