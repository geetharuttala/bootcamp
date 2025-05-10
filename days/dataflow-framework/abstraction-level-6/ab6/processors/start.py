# ab6/processors/start.py
from typing import Iterator
from ab6.common.types import TaggedLine
from rich import print

def tag_lines(lines: Iterator[str]) -> Iterator[TaggedLine]:
    for line in lines:
        if "[ERROR]" in line:
            yield "error", line.replace("[ERROR]", "").strip()
        elif "[WARNING]" in line:
            yield "warn", line.replace("[WARNING]", "").strip()
        elif "[INFO]" in line:
            yield "general", line.replace("[INFO]", "").strip()
        else:
            yield "general", line.strip()
