import shutil
from pathlib import Path

src = Path("source.txt")
dst = Path("copied.txt")
src.write_text("Copy this content")

shutil.copy(src, dst)
print("Copied:", dst.read_text())
