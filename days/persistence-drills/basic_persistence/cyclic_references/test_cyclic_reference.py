from cyclic_reference import Person

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
