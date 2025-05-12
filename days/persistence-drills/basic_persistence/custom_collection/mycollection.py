import pickle
from typing import List


class MyCollection:
    """A custom collection class that holds multiple objects."""
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the collection."""
        self.items.append(item)

    def __repr__(self):
        return f"MyCollection(items={self.items})"

    def serialize(self, filename: str):
        """Serialize the collection to a file using pickle."""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename: str):
        """Deserialize a collection from a file."""
        with open(filename, "rb") as f:
            return pickle.load(f)
