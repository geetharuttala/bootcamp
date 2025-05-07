from pathlib import Path

py_files = list(Path(".").glob("*.py"))
print("Python files:", [file.name for file in py_files])
