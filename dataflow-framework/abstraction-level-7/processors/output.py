# processors/output.py
from utils.metrics import metrics_store

class TerminalOutputProcessor:
    def process(self, line: str):
        try:
            # Simulate an error when a specific word is in the line
            if "fail" in line.lower():
                raise ValueError("Simulated terminal output failure")
            print(f"[OUTPUT] {line}")
        except Exception as e:
            metrics_store.log_error("terminal_output", str(e))
        return None, None

def get_terminal_processor():
    return TerminalOutputProcessor()
