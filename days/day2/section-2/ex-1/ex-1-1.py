data = {"name": "Alice"}

# EAFP style
try:
    print(data["age"])
except KeyError:
    print("Age not found")