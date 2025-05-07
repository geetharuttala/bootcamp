from datetime import datetime, timedelta

now = datetime.now()
rounded = now.replace(minute=0, second=0, microsecond=0)
if now.minute >= 30:
    rounded += timedelta(hours=1)
print("Now:", now)
print("Rounded to nearest hour:", rounded)
