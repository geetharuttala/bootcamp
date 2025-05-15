# processors/tally.py
from processor_types import TaggedProcessor
from typing import Iterator

class Tally(TaggedProcessor):
    def __init__(self):
        self.count = 0

    def process(self, lines: Iterator[str]) -> Iterator[tuple[str, str]]:
        for line in lines:
            self.count += 1
            # Yield with 'formatted' so it reaches the printer
            yield "formatted", f"Tally[{self.count}]: {line}"

