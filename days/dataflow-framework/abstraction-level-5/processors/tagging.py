# processors/tagging.py
from typing import Iterator, Tuple
from processor_types import TaggedProcessor, TaggedLine

class TagError(TaggedProcessor):
    def process(self, lines: Iterator[str]) -> Iterator[TaggedLine]:
        for line in lines:
            tag = "errors" if "error" in line.lower() else "main"
            yield tag, line

class TagWarn(TaggedProcessor):
    def process(self, lines: Iterator[str]) -> Iterator[TaggedLine]:
        for line in lines:
            tag = "warnings" if "warn" in line.lower() else "main"
            yield tag, line

class TagRouter(TaggedProcessor):
    def process(self, lines: Iterator[str]) -> Iterator[TaggedLine]:
        for line in lines:
            if "[ERROR]" in line:
                yield "errors", line
            elif "[WARNING]" in line:
                yield "warnings", line
            else:
                yield "general", line
