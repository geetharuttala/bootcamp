# processors/formatters.py
from typing import Iterator
from processor_types import TaggedProcessor, TaggedLine

class Format(TaggedProcessor):
    def process(self, lines: Iterator[str]) -> Iterator[TaggedLine]:
        for line in lines:
            formatted = f"* {line.capitalize()}"
            yield "formatted", formatted
