from pathlib import Path

path = Path("output.txt")
print("Exists?", path.exists())
print("Is file?", path.is_file())
