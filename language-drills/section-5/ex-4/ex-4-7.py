import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {"event": "meeting", "time": datetime.now()}
json_str = json.dumps(data, cls=DateTimeEncoder)
print(json_str)
