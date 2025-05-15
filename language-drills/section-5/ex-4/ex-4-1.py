import json

data = {"name": "Geetha", "age": 24}
json_str = json.dumps(data)
parsed_data = json.loads(json_str)

print("Serialized JSON:", json_str)
print("Deserialized Python dict:", parsed_data)
