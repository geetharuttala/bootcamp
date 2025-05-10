# processors/formatters.py

class SnakeCaseFormatter:
    def process(self, line: str):
        snake_line = line.replace(" ", "_").lower()
        return "end", f"[SNAKE] {snake_line}"

def get_snakecase_processor():
    return SnakeCaseFormatter()

