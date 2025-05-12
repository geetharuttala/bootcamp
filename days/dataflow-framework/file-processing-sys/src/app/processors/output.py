# Fixed version of app/processors/output.py

from app.utils.metrics import metrics_store
from app.utils.tracing import trace_store
from typing import Iterator, Tuple


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

            # Log that we're outputting a line
            metrics_store.increment("output_lines")

            # Add to trace store - this is now deduplication-aware
            trace_store.add_trace("output", line)

            # Yield the processed line
            yield "end", line


class TerminalOutputProcessor:
    def process(self, line: str):
        try:
            # Simulate an error when a specific word is in the line
            if "fail" in line.lower():
                raise ValueError("Simulated terminal output failure")

            metrics_store.increment("terminal_output")
            print(f"[OUTPUT] {line}")

        except Exception as e:
            # Log the error with deduplication
            metrics_store.log_error("terminal_output", str(e))
            metrics_store.increment("output_errors")

        return None, None


def get_terminal_processor():
    return TerminalOutputProcessor()