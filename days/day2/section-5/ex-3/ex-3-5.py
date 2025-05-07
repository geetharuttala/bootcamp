from datetime import datetime
import calendar

today = datetime.now()
weekday_name = calendar.day_name[today.weekday()]
print("Today is:", weekday_name)
