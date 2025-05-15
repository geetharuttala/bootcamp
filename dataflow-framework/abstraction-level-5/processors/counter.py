# processors/counter.py
from typing import Iterator
from processor_types import TaggedProcessor, TaggedLine

class Count(TaggedProcessor):
    def __init__(self):
        self.count = 0

    def process(self, lines: Iterator[str]) -> Iterator[TaggedLine]:
        for line in lines:
            self.count += 1
            yield "counted", f"[COUNT {self.count}] {line}"
