from processor_types import ProcessorFn
from typing import Iterator

def apply_pipeline(lines: Iterator[str], processors: list[ProcessorFn]) -> Iterator[str]:
    for line in lines:
        for processor in processors:
            line = processor(line)
        yield line
