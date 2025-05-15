from pathlib import Path

path = Path("myfile.txt")
path.write_text("Hello from pathlib!")
print("File content:", path.read_text())
