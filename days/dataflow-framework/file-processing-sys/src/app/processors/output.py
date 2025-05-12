# processors/output.py
# processors/output.py
from app.utils.metrics import metrics_store
from app.utils.tracing import trace_store
from typing import Iterator, Tuple




def process(lines: Iterator[Tuple[str, str]], current_tag: str) -> Iterator[Tuple[str, str]]:
   for tag, line in lines:
       if tag == current_tag:
           # Log that we're outputting a line
           metrics_store.increment("output_lines")
           trace_store.add_trace("output", line)
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
           metrics_store.log_error("terminal_output", str(e))
           metrics_store.increment("output_errors")


       return None, None




def get_terminal_processor():
   return TerminalOutputProcessor()
