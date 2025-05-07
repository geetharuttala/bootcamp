# DANGER: Never unpickle data from untrusted sources!
# Use JSON when you don't need to serialize complex objects

import json

safe_data = {"framework": "FastAPI", "version": "0.95"}
json_str = json.dumps(safe_data)
recovered = json.loads(json_str)
print("Safe deserialization:", recovered)

# marshal is an internal tool and should not replace JSON for secure cases
