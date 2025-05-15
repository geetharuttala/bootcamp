# Updated start.py processor with state-based routing
from typing import Iterator, Tuple, List
from app.utils.metrics import metrics_store

def tag_lines(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
    """Process input lines and tag them based on content."""
    for _, line in lines:
        # Categorize the line based on its content
        if "error" in line.lower() or "ERROR" in line:
            metrics_store.increment("error_lines")
            yield "error", line
        elif "warn" in line.lower() or "WARN" in line or "WARNING" in line:
            metrics_store.increment("warn_lines")
            yield "warn", line
        else:
            metrics_store.increment("general_lines")
            yield "general", line

class StartProcessor:
    def process(self, line: str):
        if "error" in line.lower() or "ERROR" in line:
            metrics_store.increment("error_line")
            return "error", line
        elif "warn" in line.lower() or "WARN" in line or "WARNING" in line:
            metrics_store.increment("warn_line")
            return "warn", line
        else:
            metrics_store.increment("general_line")
            return "general", line

def get_processor():
    return StartProcessor()