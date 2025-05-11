from core.engine import ProcessingEngine
from utils.metrics import metrics_store
from utils.tracing import trace_store

CONFIG_FILE = "config/pipeline.yaml"


def process_file(input_file):
    trace = True  # Enable dashboard/trace mode when using watcher
    engine = ProcessingEngine(str(input_file), CONFIG_FILE, trace)
    engine.run()