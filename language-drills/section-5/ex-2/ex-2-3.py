from pathlib import Path

path = Path("output.txt")
path.write_text("hello")
print("Written 'hello' to output.txt")
