# processors/start.py
from typing import Iterator, Tuple

def process(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
    for tag, line in lines:
        if tag == current_tag:
            yield tag, line

class StartProcessor:
    def process(self, line: str):
        if "error" in line.lower():
            return "error", line
        elif "warn" in line.lower():
            return "warn", line
        else:
            return "general", line

def get_processor():
    return StartProcessor()

