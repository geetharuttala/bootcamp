from app.processors import filters, formatters, output, start
from app.utils.tracing import trace_store
from app.utils.metrics import metrics_store
from typing import Iterator
import yaml

PROCESSOR_MAP = {
    "start": start.process,
    "filter": filters.process,
    "format": formatters.process,
    "output": output.process,
}

class ProcessingEngine:
    def __init__(self, input_file: str, config_file: str, trace: bool = False):
        self.input_file = input_file
        self.trace = trace
        self.pipeline = self.load_pipeline(config_file)
        self.trace_data = []

    def load_pipeline(self, config_file: str):
        with open(config_file) as f:
            raw_pipeline = yaml.safe_load(f)

        # Normalize the pipeline to always be: tag -> list of steps
        pipeline = {}
        for tag, config in raw_pipeline.items():
            if isinstance(config, dict) and "next" in config:
                next_step = config["next"]
                pipeline[tag] = [next_step] if isinstance(next_step, str) else next_step
            elif isinstance(config, list):
                pipeline[tag] = config
            else:
                pipeline[tag] = []

        return pipeline

    def run(self):
        print(f"[ENGINE] Processing file: {self.input_file}")
        with open(self.input_file) as f:
            lines = (line.strip() for line in f)
            tagged_lines = [("start", line) for line in lines]

            for tag, processor_steps in self.pipeline.items():
                for step in processor_steps:
                    func = PROCESSOR_MAP[step]
                    print(f"[ENGINE] Applying {step} to tag: {tag}")
                    tagged_lines = func(tagged_lines, tag)

                    # 👇 Add debug print to show the result after each step
                    print(f"[DEBUG] After step '{step}' on tag '{tag}':")
                    for t, l in tagged_lines:
                        print(f"  {t}: {l}")

                    if self.trace:
                        self.trace_data.append((tag, step, list(tagged_lines)))

        if self.trace:
            print("[ENGINE] Storing trace data...")
            trace_store.store(self.input_file, self.trace_data)
