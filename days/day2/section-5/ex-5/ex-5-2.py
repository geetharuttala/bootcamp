import subprocess
result = subprocess.run(["echo", "hello"], capture_output=True, text=True)
print("Captured:", result.stdout.strip())
