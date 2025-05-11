# src/app/engine/runner.py
from app.core.engine import ProcessingEngine
from app.utils.metrics import metrics_store
from app.utils.tracing import trace_store

CONFIG_FILE = "config/pipeline.yaml"

def process_file(input_file, config_file=CONFIG_FILE, trace=False):
    # Set up the processing engine with the necessary arguments
    engine = ProcessingEngine(str(input_file), str(config_file), trace)
    engine.run()
