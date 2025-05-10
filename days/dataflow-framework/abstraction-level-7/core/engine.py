import yaml
from core.pipeline import build_pipeline
from utils.metrics import metrics_store
from utils.tracing import trace_store

class ProcessingEngine:
    def __init__(self, input_file: str, config_file: str, trace: bool):
        self.input_file = input_file
        self.config_file = config_file
        self.trace = trace
        self.pipeline = build_pipeline(config_file)

    def run(self):
        with open(self.input_file, 'r') as f:
            lines = (line.strip() for line in f)
            for tag, line in self.pipeline.process(lines):
                # Update metrics
                metrics_store.increment(tag)
                # Update trace if enabled
                if self.trace:
                    trace_store.add_trace(tag, line)
