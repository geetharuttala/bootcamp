from datetime import datetime, timedelta

today = datetime.now()
next_week = today + timedelta(days=7)
print("Today:", today)
print("After 7 days:", next_week)
