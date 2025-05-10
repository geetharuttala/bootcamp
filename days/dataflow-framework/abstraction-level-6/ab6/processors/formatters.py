from typing import Iterator
from ab6.common.types import TaggedLine

def snakecase(lines: Iterator[TaggedLine]) -> Iterator[TaggedLine]:
    for tag, line in lines:
        # Unpack nested tuple if present
        if isinstance(line, tuple):
            _, line = line  # discard inner tag
        formatted = line.lower().replace(" ", "_")
        yield "end", f"[FORMATTED] {formatted}"

