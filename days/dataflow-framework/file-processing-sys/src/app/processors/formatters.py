# Updated formatters.py processor with state-based routing
from typing import Iterator, Tuple

def snakecase(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
    """Convert lines to snake_case format."""
    for tag, line in lines:
        # Convert spaces to underscores and make lowercase
        snake_line = line.replace(" ", "_").lower()
        yield "formatted", f"[SNAKE] {snake_line}"

class SnakeCaseFormatter:
    def process(self, line: str):
        snake_line = line.replace(" ", "_").lower()
        return "formatted", f"[SNAKE] {snake_line}"

def get_snakecase_processor():
    return SnakeCaseFormatter()