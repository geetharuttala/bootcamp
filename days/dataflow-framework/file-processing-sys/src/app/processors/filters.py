# processors/filters.py
from typing import Iterator, Tuple

def process(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
    for tag, line in lines:
        if tag == current_tag and "ERROR" in line:
            yield "filter", line


class ErrorProcessor:
    def process(self, line: str):
        return "end", f"[ERROR] {line}"

class WarnProcessor:
    def process(self, line: str):
        return "end", f"[WARN] {line}"

def get_error_processor():
    return ErrorProcessor()

def get_warn_processor():
    return WarnProcessor()
