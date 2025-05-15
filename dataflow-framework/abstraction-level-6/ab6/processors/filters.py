from typing import Iterator
from ab6.common.types import TaggedLine

def only_error(lines: Iterator[str]) -> Iterator[TaggedLine]:
    for line in lines:
        if "[ERROR]" in line:
            yield "end", f"[FILTERED ERROR] {line}"

def only_warn(lines: Iterator[str]) -> Iterator[TaggedLine]:
    for line in lines:
        if "[WARNING]" in line:
            yield "end", f"[FILTERED WARNING] {line}"
