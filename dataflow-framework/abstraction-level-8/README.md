# Streaming File Processor – Level 8: Automated Folder Monitor and Recovery

This project implements a robust, fault-tolerant file ingestion system that continuously monitors a folder for incoming text files, processes them line by line using a dynamic streaming pipeline, and provides a live dashboard to visualize system activity.

## Features

- Continuously monitors `watch_dir/unprocessed/` for new files
- Automatically retries uncompleted files after a crash
- Processes files using a configurable tag-based streaming pipeline
- Displays live statistics, trace routes, and errors on a web dashboard
- Resilient, idempotent, and safe for long-running deployments

## Folder Structure

```

abstraction-level-8/
├── cli.py
├── file_watcher.py
├── main.py
├── config/
│   └── pipeline.yaml
├── core/
│   └── engine.py
├── engine/
│   └── runner.py      
├── processors/
│   ├── __init__.py
│   ├── filters.py
│   ├── formatters.py
│   ├── output.py
│   └── start.py
├── dashboard/
│   ├── __init__.py
│   └── server.py
├── utils/
│   ├── metrics.py
│   └── tracing.py
├── watch_dir/
│   ├── unprocessed/
│   ├── underprocess/
│   └── processed/
├── README.md
├── requirements.txt

````

## How It Works

1. **Startup Recovery:**  
   Any files left in `underprocess/` from a previous run are moved back to `unprocessed/` for reprocessing.

2. **Monitoring Loop:**  
   A background thread polls the `unprocessed/` folder. When a file appears:
   - It is moved to `underprocess/`
   - It is streamed through a configurable line processor based on tags
   - When complete, it is moved to `processed/`

3. **Processing Engine:**  
   Each line is tagged and routed through a DAG of processors like `filter`, `format`, and `output`. These processors are dynamically configured.

4. **Dashboard:**  
   A FastAPI web server serves a real-time dashboard that shows:
   - Current processing status and file counts
   - Trace of line tag flow between processors
   - Recent processed files
   - Any encountered errors

## Usage

### 1. Install Dependencies

```bash
pip install -r requirements.txt
````

Ensure `uvicorn`, `watchdog`, `typer`, and `fastapi` are installed.

### 2. Start the System

```bash
python main.py
```

This will:

* Start the file monitor in the background
* Launch the FastAPI dashboard at `http://localhost:8000`

### 3. Add Input Files

Place text files into the `watch_dir/unprocessed/` directory.

Example file: `watch_dir/unprocessed/input.txt`

```
start:ERROR: Something bad happened
```

### 4. View Output

* Processed file will move to `watch_dir/processed/`
* Live dashboard is accessible at:

  * `/files` → File state summary
  * `/trace` → Tag-based routing trace
  * `/stats` → System metrics
  * `/errors` → Captured errors

## Example

### Input: `input.txt`

```
start:ERROR: Something bad happened
```

### Processing Trace:

```
start → filter → format → output
```

### Output (post-formatting):

```
filter: start:ERROR: Something bad happened
```

### Dashboard JSON

**/files**

```json
{
  "current": null,
  "recent": [
    {
      "file": "input.txt",
      "timestamp": 1746891673.16802
    }
  ],
  "counts": {
    "unprocessed": 0,
    "underprocess": 0,
    "processed": 1
  }
}
```

**/trace**

```json
[
  [
    ["start", "filter", []],
    ["filter", "format", []],
    ["format", "output", []]
  ]
]
```

## Screenshots

### Files Dashboard
![Files Dashboard](/days/dataflow-framework/abstraction-level-8/images/files.png)

### Trace Dashboard
![Trace Dashboard](/days/dataflow-framework/abstraction-level-8/images/files.png)


## Notes

* The system is single-instance only. Running multiple instances may lead to file collisions.
* Make sure input files are fully written before placing them in `unprocessed/`
* Processing is idempotent: reprocessing the same file is safe.

## License

MIT License


