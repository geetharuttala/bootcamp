import subprocess
result = subprocess.run(["false"])
print("Exit Code:", result.returncode)
