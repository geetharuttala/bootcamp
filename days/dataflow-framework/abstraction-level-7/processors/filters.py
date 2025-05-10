# processors/filters.py

class ErrorProcessor:
    def process(self, line: str):
        return "end", f"[ERROR] {line}"

class WarnProcessor:
    def process(self, line: str):
        return "end", f"[WARN] {line}"

def get_error_processor():
    return ErrorProcessor()

def get_warn_processor():
    return WarnProcessor()
