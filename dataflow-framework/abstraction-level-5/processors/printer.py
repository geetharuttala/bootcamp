# processors/printer.py
from typing import Iterator
from processor_types import TaggedProcessor, TaggedLine

class Printer(TaggedProcessor):
    def process(self, lines: Iterator[str]) -> Iterator[TaggedLine]:
        for line in lines:
            print(line)
        return iter([])
