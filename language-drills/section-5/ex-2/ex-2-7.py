from pathlib import Path

relative_path = Path("somefile.txt")
print("Absolute path:", relative_path.resolve())
