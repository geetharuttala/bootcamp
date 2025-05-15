from datetime import datetime

today = datetime.now()
formatted = today.strftime("%Y-%m-%d")
print("Formatted date:", formatted)
