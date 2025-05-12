from mycollection import MyCollection

# Create a collection
collection = MyCollection()
collection.add_item("The Catcher in the Rye")
collection.add_item("To Kill a Mockingbird")
collection.add_item("1984")

print("Before serialization:")
print(collection)

# Serialize the collection
collection.serialize("my_collection.pkl")

# Deserialize the collection
restored_collection = MyCollection.deserialize("my_collection.pkl")

print("\nAfter deserialization:")
print(restored_collection)
