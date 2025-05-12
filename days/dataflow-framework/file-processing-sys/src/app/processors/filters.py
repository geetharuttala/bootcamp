# Fixed version of app/processors/filters.py

from typing import Iterator, Tuple
from app.utils.metrics import metrics_store


def process(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
    # Track processed lines to avoid duplicates
    processed_lines = set()

    for tag, line in lines:
        if tag == current_tag:
            # Skip if we've already processed this exact line
            if line in processed_lines:
                continue

            # Mark as processed
            processed_lines.add(line)

            if "ERROR" in line:
                metrics_store.increment("error_filtered")
                yield "error", line
            elif "WARN" in line:
                metrics_store.increment("warn_filtered")
                yield "warn", line
            else:
                yield "general", line


class ErrorProcessor:
    def process(self, line: str):
        metrics_store.increment("error_processed")
        return "end", f"[ERROR] {line}"


class WarnProcessor:
    def process(self, line: str):
        metrics_store.increment("warn_processed")
        return "end", f"[WARN] {line}"


def get_error_processor():
    return ErrorProcessor()


def get_warn_processor():
    return WarnProcessor()