# processors/start.py

class StartProcessor:
    def process(self, line: str):
        if "error" in line.lower():
            return "error", line
        elif "warn" in line.lower():
            return "warn", line
        else:
            return "general", line

def get_processor():
    return StartProcessor()

