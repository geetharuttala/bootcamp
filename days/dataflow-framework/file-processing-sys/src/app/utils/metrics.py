# Fixed version of app/utils/metrics.py

import time
from collections import defaultdict
import threading


class MetricsStore:
    def __init__(self):
        self.lock = threading.Lock()
        self.metrics = defaultdict(int)
        self.recent_errors = []
        # Track processed error messages to avoid duplicates
        self.processed_errors = set()

    def increment(self, tag, count=1):
        """Increment a metric by count (default 1)"""
        with self.lock:
            self.metrics[tag] += count

    def get_metrics(self):
        with self.lock:
            return dict(self.metrics)

    def log_error(self, processor_name, error_msg):
        """Log an error, avoiding duplicates with same processor+message"""
        error_key = f"{processor_name}:{error_msg}"

        with self.lock:
            # Skip if we've seen this exact error before
            if error_key in self.processed_errors:
                return

            self.processed_errors.add(error_key)
            self.recent_errors.append({
                "processor": processor_name,
                "message": error_msg,
                "timestamp": time.time()
            })
            # Keep only the most recent 100 errors
            if len(self.recent_errors) > 100:
                self.recent_errors.pop(0)

    def get_recent_errors(self):
        with self.lock:
            return self.recent_errors

    def clear_errors(self):
        """Clear all error records - useful for testing or resets"""
        with self.lock:
            self.recent_errors = []
            self.processed_errors = set()


metrics_store = MetricsStore()