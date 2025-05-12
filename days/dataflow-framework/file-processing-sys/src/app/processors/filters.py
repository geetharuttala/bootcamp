# processors/filters.py
from typing import Iterator, Tuple
from app.utils.metrics import metrics_store


def process(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
   for tag, line in lines:
       if tag == current_tag:
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


