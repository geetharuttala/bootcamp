# Updated output.py processor with state-based routing
from app.utils.metrics import metrics_store
from app.utils.tracing import trace_store
from typing import Iterator, Tuple


def terminal(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
    """Output lines to terminal and pass to next stage."""
    processed_lines = set()

    for tag, line in lines:
        # Skip if we've already processed this exact line
        if line in processed_lines:
            continue

        # Mark as processed
        processed_lines.add(line)

        # Log output metrics
        metrics_store.increment("output_lines")

        # Add to trace store
        trace_store.add_trace("output", line)

        # Print to terminal
        try:
            if "fail" in line.lower():
                raise ValueError("Simulated terminal output failure")

            print(f"[OUTPUT] {line}")
            metrics_store.increment("terminal_output")

        except Exception as e:
            # Log the error
            metrics_store.log_error("terminal_output", str(e))
            metrics_store.increment("output_errors")

        # Pass to end state
        yield "end", line


def finalize(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
    """Final processor that doesn't modify lines but marks them as complete."""
    for tag, line in lines:
        metrics_store.increment("finalized_lines")
        yield "end", line


class TerminalOutputProcessor:
    def process(self, line: str):
        try:
            # Simulate an error when a specific word is in the line
            if "fail" in line.lower():
                raise ValueError("Simulated terminal output failure")

            print(f"[OUTPUT] {line}")
            metrics_store.increment("terminal_output")

        except Exception as e:
            # Log the error
            metrics_store.log_error("terminal_output", str(e))
            metrics_store.increment("output_errors")

        return "end", line


def get_terminal_processor():
    return TerminalOutputProcessor()