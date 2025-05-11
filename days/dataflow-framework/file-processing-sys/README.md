# Real-Time File Processing System

This project implements a dynamic, observable, fault-tolerant file processing pipeline using FastAPI, a plugin-based engine, and streaming abstractions. It supports both one-shot and continuous file processing modes.

## Features

- Dual execution modes: single file or watch directory
- Modular processing pipeline with YAML-based configuration
- FastAPI-based monitoring and dashboard
- Docker support
- Package build and publishing support
- Real-time file drop handling
- Tag-based routing and stateful processing

---

## Installation

### Prerequisites

- Python 3.10+
- Docker (optional, for containerized usage)
- `pip`, `build`, `twine`, etc., for packaging

### Clone and Setup

```bash
git clone https://github.com/geetharuttala/bootcamp/days/dataflow-framework/file-processing-sys.git
cd file-processing-sys
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

---

## Execution Modes

### 1. Watch Mode

Continuously monitors the `watch_dir/unprocessed/` folder for incoming files.

```bash
make run
```

Or directly:

```bash
python main.py --watch
```

### 2. Single File Mode

Processes a single file and exits.

```bash
make run-file FILE=sample.txt
```

Or directly:

```bash
python main.py --input sample.txt
```

---

## Sample Input

Place the following content into a file named `sample.txt` inside `watch_dir/unprocessed/`:

```
start:ERROR: Something bad happened
start:INFO: All good
start:WARNING: Potential issue
```

---

## Sample Output

After processing, output may look like:

```
filter: start:ERROR: Something bad happened
format: [ERROR] Something bad happened
output: Logged to system
```

Processed files are moved to:

* `watch_dir/processed/` (success)
* `watch_dir/failed/` (if errors occur)

---

## FastAPI Dashboard

When running in `--watch` mode, a FastAPI server starts at:

```
http://localhost:8000
```

### Available Endpoints

| Endpoint  | Description                        |
| --------- | ---------------------------------- |
| `/`       | Dashboard homepage                 |
| `/stats`  | Metrics and statistics             |
| `/health` | Health check for uptime monitoring |
| `/files`  | Processed file history             |
| `/trace`  | Full processing traces             |
| `/errors` | Error logs                         |

---

## Docker Usage

### Build Image

```bash
make docker-build
```

### Run Container

```bash
make docker-run
```

This mounts the local `watch_dir/` into the container for real-time processing.

---

## Package Build and Publish

To build and upload your package to PyPI or TestPyPI:

```bash
make publish
```

Make sure your `pyproject.toml` is correctly configured.

---

## Uptime Monitoring

To monitor your system externally:

1. Deploy it on a server (e.g., a GCP VM or AWS EC2).
2. Use a free uptime monitoring service like [Better Uptime](https://betteruptime.com).
3. Point it to the `/health` endpoint (e.g., `http://yourdomain.com:8000/health`).
4. Configure alerts if the service is unavailable.

---

## Development and Maintenance

* All core functionality is structured and modular.
* New processors can be added dynamically by editing `pipeline.yaml` and implementing corresponding Python modules.
* Logging and trace support are built-in for observability.

---

## License

MIT License. See `LICENSE` file for details.



