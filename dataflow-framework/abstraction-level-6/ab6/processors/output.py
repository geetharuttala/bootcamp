# ab6/processors/output.py

from rich import print
from ab6.common.types import TaggedLine
from typing import Iterator

def terminal(lines: Iterator[TaggedLine]) -> Iterator[TaggedLine]:
    for tag, line in lines:
        print(f"[bold cyan]{tag.upper()}[/]: {line}")
    yield from ()  # Ensures function is a generator and returns an empty iterator