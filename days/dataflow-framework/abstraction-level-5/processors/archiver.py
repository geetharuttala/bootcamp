# processors/archiver.py
from typing import Iterator
from processor_types import TaggedProcessor, TaggedLine

class Archive(TaggedProcessor):
    def __init__(self):
        self.archived = []

    def process(self, lines: Iterator[str]) -> Iterator[TaggedLine]:
        for line in lines:
            self.archived.append(line)
            # You can simulate file writing here if needed.
            yield "archived", f"[ARCHIVED] {line}"
