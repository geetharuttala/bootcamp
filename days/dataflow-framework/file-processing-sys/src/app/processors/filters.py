# Updated filters.py processor with state-based routing
from typing import Iterator, Tuple
from app.utils.metrics import metrics_store


def only_error(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
    """Process only error lines."""
    processed_lines = set()

    for tag, line in lines:
        # Skip if we've already processed this exact line
        if line in processed_lines:
            continue

        # Mark as processed
        processed_lines.add(line)

        if "ERROR" in line or tag == "error":
            metrics_store.increment("error_filtered")
            yield "formatted", f"[ERROR] {line}"


def only_warn(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
    """Process only warning lines."""
    processed_lines = set()

    for tag, line in lines:
        # Skip if we've already processed this exact line
        if line in processed_lines:
            continue

        # Mark as processed
        processed_lines.add(line)

        if "WARN" in line or "WARNING" in line or tag == "warn":
            metrics_store.increment("warn_filtered")
            yield "formatted", f"[WARNING] {line}"


class ErrorProcessor:
    def process(self, line: str):
        metrics_store.increment("error_processed")
        return "formatted", f"[ERROR] {line}"


class WarnProcessor:
    def process(self, line: str):
        metrics_store.increment("warn_processed")
        return "formatted", f"[WARNING] {line}"


def get_error_processor():
    return ErrorProcessor()


def get_warn_processor():
    return WarnProcessor()