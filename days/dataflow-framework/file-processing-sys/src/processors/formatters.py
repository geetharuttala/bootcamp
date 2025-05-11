# processors/formatters.py
from typing import Iterator, Tuple

def process(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
    for tag, line in lines:
        if tag == current_tag and "ERROR" in line:
            yield "output", line

class SnakeCaseFormatter:
    def process(self, line: str):
        snake_line = line.replace(" ", "_").lower()
        return "end", f"[SNAKE] {snake_line}"

def get_snakecase_processor():
    return SnakeCaseFormatter()

