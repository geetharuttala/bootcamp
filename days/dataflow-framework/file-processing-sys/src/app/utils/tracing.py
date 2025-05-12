from collections import deque
import threading
import time


class TraceStore:
   def __init__(self, maxlen=1000):
       self.lock = threading.Lock()
       self.traces = deque(maxlen=maxlen)


   def store(self, filename: str, trace_data: list):
       """Store a full trace from file processing"""
       with self.lock:
           timestamp = time.time()
           self.traces.append({
               "filename": filename,
               "timestamp": timestamp,
               "data": trace_data
           })


   def add_trace(self, tag, line):
       """Add a single trace entry"""
       with self.lock:
           self.traces.append({
               'tag': tag,
               'line': line,
               'timestamp': time.time()
           })


   def get_traces(self):
       with self.lock:
           return list(self.traces)


trace_store = TraceStore()


