# processors/trim.py
from typing import Iterator, Tuple
from processor_types import TaggedProcessor, TaggedLine

class Trim(TaggedProcessor):
    def process(self, lines: Iterator[str]) -> Iterator[TaggedLine]:
        for line in lines:
            yield "main", line.strip()
