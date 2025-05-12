# processors/start.py
from typing import Iterator, Tuple
from app.utils.metrics import metrics_store


def process(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
   for tag, line in lines:
       if tag == current_tag:
           # Categorize the line based on its content
           if "error" in line.lower():
               metrics_store.increment("error_lines")
               yield "error", line
           elif "warn" in line.lower():
               metrics_store.increment("warn_lines")
               yield "warn", line
           else:
               metrics_store.increment("general_lines")
               yield "general", line


class StartProcessor:
   def process(self, line: str):
       if "error" in line.lower():
           metrics_store.increment("error_line")
           return "error", line
       elif "warn" in line.lower():
           metrics_store.increment("warn_line")
           return "warn", line
       else:
           metrics_store.increment("general_line")
           return "general", line


def get_processor():
   return StartProcessor()


