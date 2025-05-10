from typing import Iterator, Tuple

TaggedLine = Tuple[str, str]

class TaggedProcessor:
    def process(self, lines: Iterator[str]) -> Iterator[TaggedLine]:
        raise NotImplementedError
