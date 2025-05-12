# src/app/engine/runner.py
from app.core.engine import ProcessingEngine
from app.utils.metrics import metrics_store
from app.utils.tracing import trace_store
import os


CONFIG_FILE = "src/app/config/pipeline.yaml"  # Updated path




def process_file(input_file, config_file=None, trace=True):
   """
   Process a file through the pipeline


   Args:
       input_file: Path to the file to process
       config_file: Path to the pipeline configuration file
       trace: Whether to enable tracing
   """
   # Use the default config if none provided
   if config_file is None:
       # Try to find the config file
       if os.path.exists(CONFIG_FILE):
           config_file = CONFIG_FILE
       elif os.path.exists("app/config/pipeline.yaml"):
           config_file = "app/config/pipeline.yaml"
       else:
           # Last resort - use relative path from current directory
           config_file = "config/pipeline.yaml"


   print(f"Using config file: {config_file}")
   print(f"Processing file: {input_file}")


   # Log metrics about the processing
   metrics_store.increment("files_processed")


   try:
       # Set up the processing engine with the necessary arguments
       engine = ProcessingEngine(str(input_file), str(config_file), trace)
       engine.run()
       metrics_store.increment("successful_runs")
   except Exception as e:
       # Log any errors that occur during processing
       error_msg = f"Error processing file {input_file}: {str(e)}"
       print(f"ERROR: {error_msg}")
       metrics_store.log_error("file_runner", error_msg)
       metrics_store.increment("failed_runs")
       raise


