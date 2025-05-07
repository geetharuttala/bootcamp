from datetime import datetime

date1 = datetime(2023, 5, 1)
date2 = datetime(2025, 5, 1)

if date1 < date2:
    print("Earlier:", date1)
else:
    print("Earlier:", date2)
