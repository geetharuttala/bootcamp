import json

data = {"z": 3, "a": 1, "b": 2}
pretty_json = json.dumps(data, indent=4, sort_keys=True)
print(pretty_json)
