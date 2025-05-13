# Fixed version of app/core/engine.py with state-based routing

from app.processors import filters, formatters, output, start
from app.utils.tracing import trace_store
from app.utils.metrics import metrics_store
from typing import Dict, List, Tuple, Optional
import yaml
import importlib


class ProcessingEngine:
    def __init__(self, input_file: str, config_file: str, trace: bool = False):
        self.input_file = input_file
        self.trace = trace
        self.nodes, self.processors = self.load_pipeline(config_file)
        self.trace_data = []

    def load_processor_function(self, processor_type: str):
        """Dynamically load processor function from a string path."""
        try:
            # Split the path into module and function
            module_path, function_name = processor_type.rsplit('.', 1)

            # Import the module
            module = importlib.import_module(f"app.{module_path}")

            # Get the function
            return getattr(module, function_name)
        except (ImportError, AttributeError) as e:
            print(f"[ENGINE ERROR] Failed to load processor {processor_type}: {e}")
            # Return a dummy processor as fallback
            return lambda lines, tag: []

    def load_pipeline(self, config_file: str):
        """Load pipeline configuration from YAML file."""
        with open(config_file) as f:
            config = yaml.safe_load(f)

        nodes = {}
        processors = {}

        # Process each node in the configuration
        for node in config.get('nodes', []):
            tag = node.get('tag')
            processor_type = node.get('type')
            next_states = node.get('next', {})

            # Store node configuration
            nodes[tag] = {
                'type': processor_type,
                'next': next_states
            }

            # Load processor function
            if processor_type:
                processors[tag] = self.load_processor_function(processor_type)

        return nodes, processors

    def run(self):
        """Run the processing pipeline on the input file."""
        print(f"[ENGINE] Processing file: {self.input_file}")

        with open(self.input_file) as f:
            lines = [line.strip() for line in f if line.strip()]

        # Start with all lines in the 'start' state
        state_buckets = {'start': [(None, line) for line in lines]}
        processed_count = 0
        metrics_store.increment("total_lines", len(lines))

        # Process until no lines left or we reach max iterations
        max_iterations = 100  # Safety limit
        iteration = 0

        while state_buckets and iteration < max_iterations:
            iteration += 1
            next_state_buckets = {}

            # Process each state bucket
            for current_state, lines_in_state in state_buckets.items():
                if not lines_in_state:
                    continue

                # Skip terminal states
                if current_state == 'end' or current_state not in self.nodes:
                    if current_state == 'end':
                        processed_count += len(lines_in_state)
                    continue

                # Get processor for this state
                processor = self.processors.get(current_state)
                if not processor:
                    print(f"[ENGINE WARNING] No processor found for state: {current_state}")
                    continue

                print(f"[ENGINE] Processing {len(lines_in_state)} lines in state '{current_state}'")
                metrics_store.increment(f"state_{current_state}", len(lines_in_state))

                # Process the lines
                results = list(processor(lines_in_state, current_state))
                metrics_store.increment(f"processed_{current_state}", len(results))

                # Add trace data if enabled
                if self.trace:
                    self.trace_data.append({
                        "step": current_state,
                        "input_count": len(lines_in_state),
                        "output_count": len(results)
                    })

                # Route results to next states based on tags
                node_config = self.nodes[current_state]
                next_state_map = node_config.get('next', {})

                # Handle different types of next state configurations
                for tag, line in results:
                    if isinstance(next_state_map, dict):
                        # Map-based routing: use the tag to determine next state
                        next_state = next_state_map.get(tag, 'end')
                    elif isinstance(next_state_map, str):
                        # String-based routing: always go to the same next state
                        next_state = next_state_map
                    else:
                        # Default to end state if no valid routing
                        next_state = 'end'

                    # Add to next state bucket
                    if next_state not in next_state_buckets:
                        next_state_buckets[next_state] = []

                    next_state_buckets[next_state].append((tag, line))

                    # Count errors and warnings
                    if "ERROR" in line:
                        metrics_store.increment("error_count")
                        metrics_store.log_error("file_processor", f"Error in line: {line}")
                    elif "WARN" in line:
                        metrics_store.increment("warning_count")

                    # Add traces
                    trace_store.add_trace(tag, line)

            # Move to next iteration with updated state buckets
            state_buckets = next_state_buckets

            # Debug output
            print(f"[ENGINE] After iteration {iteration}, states: {', '.join(state_buckets.keys())}")

        # Store final trace data
        if self.trace and self.trace_data:
            print(f"[ENGINE] Storing trace data from {self.input_file}...")
            trace_store.store(self.input_file, self.trace_data)

        # Calculate completion metrics
        metrics_store.increment("processed_files")
        metrics_store.increment("successfully_processed", processed_count)