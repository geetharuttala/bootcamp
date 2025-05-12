import time
from collections import defaultdict
import threading


class MetricsStore:
   def __init__(self):
       self.lock = threading.Lock()
       self.metrics = defaultdict(int)
       self.recent_errors = []


   def increment(self, tag):
       with self.lock:
           self.metrics[tag] += 1


   def get_metrics(self):
       with self.lock:
           return dict(self.metrics)


   def log_error(self, processor_name, error_msg):
       with self.lock:
           self.recent_errors.append({
               "processor": processor_name,
               "message": error_msg,
               "timestamp": time.time()
           })
           if len(self.recent_errors) > 100:
               self.recent_errors.pop(0)


   def get_recent_errors(self):
       with self.lock:
           return self.recent_errors


metrics_store = MetricsStore()
