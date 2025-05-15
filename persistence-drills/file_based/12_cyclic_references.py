import pickle


class Person:
    """A class representing a person."""
    def __init__(self, name: str):
        self.name = name
        self.friend = None  # Reference to another Person object

    def __repr__(self):
        return f"Person(name={self.name})"

    def set_friend(self, friend):
        """Set another Person as a friend."""
        self.friend = friend

    def serialize(self, filename: str):
        """Serialize the Person object, handling cyclic references."""
        seen = set()

        def _reduce(obj):
            if id(obj) in seen:
                return None  # Handle cyclic reference by skipping
            seen.add(id(obj))
            return obj

        with open(filename, "wb") as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

    @classmethod
    def deserialize(cls, filename: str):
        """Deserialize a Person object from a file."""
        with open(filename, "rb") as f:
            person = pickle.load(f)
        return person

# Create two Person objects that reference each other
geetha = Person("Geetha")
mahi = Person("Mahi")
geetha.set_friend(mahi)
mahi.set_friend(geetha)

# Show the initial cyclic relationship
print("Before serialization:")
print(f"Geetha's friend: {geetha.friend}")
print(f"Mahi's friend: {mahi.friend}")

# Serialize the cyclic reference objects
geetha.serialize("cyclic_people.pkl")

# Deserialize the objects
restored_geetha = Person.deserialize("cyclic_people.pkl")

print("\nAfter deserialization:")
print(f"Geetha's friend: {restored_geetha.friend}")
print(f"Mahi's friend: {restored_geetha.friend.friend}")
