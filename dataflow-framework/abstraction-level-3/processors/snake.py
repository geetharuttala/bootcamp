def to_snakecase(line: str) -> str:
    return line.strip().replace(" ", "_").lower()
