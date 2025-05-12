
from app.processors import filters, formatters, output, start
from app.utils.tracing import trace_store
from app.utils.metrics import metrics_store
from typing import Iterator, List, Tuple
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


           # Count initial lines and record metrics
           initial_count = len(tagged_lines)
           metrics_store.increment("total_lines")


           # Create a list to ensure we can iterate multiple times
           tagged_lines = list(tagged_lines)


           for tag, processor_steps in self.pipeline.items():
               # Convert to list because we'll need to iterate multiple times
               matching_lines = [(t, l) for t, l in tagged_lines if t == tag]
               if matching_lines:
                   metrics_store.increment(f"tag_{tag}")
                   print(f"[ENGINE] Found {len(matching_lines)} lines with tag '{tag}'")


               for step in processor_steps:
                   func = PROCESSOR_MAP[step]
                   print(f"[ENGINE] Applying {step} to tag: {tag}")


                   # Process the lines
                   processed_lines = list(func(matching_lines, tag))


                   # Count processed lines for metrics
                   if processed_lines:
                       metrics_store.increment(f"processed_{step}")


                       # Update the main list with the processed lines
                       # First, remove lines with the current tag
                       tagged_lines = [(t, l) for t, l in tagged_lines if t != tag]
                       # Then add the processed lines
                       tagged_lines.extend(processed_lines)


                   # Add trace data for each step
                   if self.trace:
                       trace_entry = {
                           "step": step,
                           "tag": tag,
                           "input_count": len(matching_lines),
                           "output_count": len(processed_lines)
                       }
                       self.trace_data.append(trace_entry)


                   # Log any error lines
                   for t, l in processed_lines:
                       if "ERROR" in l:
                           metrics_store.increment("error_count")
                           metrics_store.log_error("file_processor", f"Error in line: {l}")
                       elif "WARN" in l:
                           metrics_store.increment("warning_count")


                       # Add individual traces
                       trace_store.add_trace(t, l)


                   print(f"[DEBUG] After step '{step}' on tag '{tag}':")
                   for t, l in tagged_lines:
                       print(f"  {t}: {l}")


       # Store final trace data
       if self.trace:
           print(f"[ENGINE] Storing trace data from {self.input_file}...")
           trace_store.store(self.input_file, self.trace_data)


       # Calculate completion metrics
       final_count = len(tagged_lines)
       metrics_store.increment("processed_files")
       if final_count > 0:
           metrics_store.increment("successfully_processed")


