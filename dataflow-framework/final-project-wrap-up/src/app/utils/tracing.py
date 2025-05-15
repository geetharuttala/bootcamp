# Fixed version of app/utils/tracing.py

from collections import deque
import threading
import time


class TraceStore:
    def __init__(self, maxlen=1000):
        self.lock = threading.Lock()
        self.traces = deque(maxlen=maxlen)
        # Track processed traces to avoid duplicates
        self.processed_traces = set()

    def store(self, filename: str, trace_data: list):
        """Store a full trace from file processing"""
        with self.lock:
            # Create a unique identifier for this trace
            trace_id = f"{filename}:{len(trace_data)}"

            # Skip if we've already stored this exact trace
            if trace_id in self.processed_traces:
                return

            timestamp = time.time()
            self.processed_traces.add(trace_id)
            self.traces.append({
                "filename": filename,
                "timestamp": timestamp,
                "data": trace_data
            })

    def add_trace(self, tag, line):
        """Add a single trace entry"""
        with self.lock:
            # Create a unique identifier for this trace
            trace_id = f"{tag}:{line}"

            # Skip if we've already stored this exact trace
            if trace_id in self.processed_traces:
                return

            self.processed_traces.add(trace_id)
            self.traces.append({
                'tag': tag,
                'line': line,
                'timestamp': time.time()
            })

    def add_traces(self, tag, lines):
        """Add multiple trace entries efficiently"""
        with self.lock:
            for t, line in lines:
                trace_id = f"{t}:{line}"
                if trace_id not in self.processed_traces:
                    self.processed_traces.add(trace_id)
                    self.traces.append({
                        'tag': t,
                        'line': line,
                        'timestamp': time.time()
                    })

    def get_traces(self):
        with self.lock:
            return list(self.traces)

    def clear_traces(self):
        """Clear all trace records"""
        with self.lock:
            self.traces.clear()
            self.processed_traces = set()


trace_store = TraceStore()