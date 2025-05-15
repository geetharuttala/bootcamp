import subprocess
import time

p = subprocess.Popen(["sleep", "10"])
print("Subprocess started. Will terminate after 2 seconds.")
time.sleep(2)
p.terminate()
print("Subprocess terminated.")
