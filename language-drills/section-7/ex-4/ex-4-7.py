import os
import psutil

print(f"CPU load: {os.getloadavg()}")
print(f"Memory usage: {psutil.virtual_memory().percent}%")
