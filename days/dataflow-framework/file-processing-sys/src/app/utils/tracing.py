from collections import deque
import threading

class TraceStore:
    def __init__(self, maxlen=1000):
        self.lock = threading.Lock()
        self.traces = deque(maxlen=maxlen)

    def store(self, filename: str, trace: dict):
        self.traces.append(trace)

    def add_trace(self, tag, line):
        with self.lock:
            self.traces.append({'tag': tag, 'line': line})

    def get_traces(self):
        with self.lock:
            return list(self.traces)

trace_store = TraceStore()
