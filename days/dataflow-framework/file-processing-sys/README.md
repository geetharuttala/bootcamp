# Real-Time File Processing System

This project implements a dynamic, observable, fault-tolerant file processing system that supports both **single-file** and **folder-watch** modes. It is configurable, modular, and built using a plugin-based architecture.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/geetharuttala/bootcamp/tree/main/days/dataflow-framework/file-processing-sys.git
cd file-processing-sys
```

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Optional: Install in Editable Mode

```bash
pip install -e .
```

---

## Running the App

### Local Execution (with Makefile)

#### Folder Watch Mode

```bash
make run
```

#### Single File Mode

```bash
make run-file FILE=input.txt
```

### Docker Execution

#### Build Docker Image

```bash
make docker-build
```

#### Run Docker Container

```bash
make docker-run
```

### Docker Compose (Recommended)

#### Start in Detached Mode

```bash
make docker-compose-up
```

Logs will stream automatically to the terminal. Visit:

* [http://localhost:8000](http://localhost:8000)
* [http://localhost:8000/health](http://localhost:8000/health)

#### Stop the Container

```bash
make docker-compose-down
```

---

## Commands Summary

| Command                    | Description                              |
| -------------------------- | ---------------------------------------- |
| `make run`                 | Runs in watch mode (local)               |
| `make run-file FILE=x`     | Runs on a single file                    |
| `make docker-build`        | Builds the Docker image                  |
| `make docker-run`          | Runs the container manually              |
| `make docker-compose-up`   | Runs container using docker-compose      |
| `make docker-compose-down` | Stops the docker-compose service         |
| `make build-pkg`           | Builds a Python package                  |
| `make publish-pkg`         | Publishes package to PyPI                |
| `make clean`               | Cleans build artifacts and `__pycache__` |

---

## Manual CLI Usage

### Folder Watch Mode

```bash
python src/app/cli.py --watch --config src/app/config/pipeline.yaml
```

### Single File Mode

```bash
python src/app/cli.py --input test.txt --config src/app/config/pipeline.yaml
```

---

## FastAPI Endpoints

| Endpoint  | Description                |
| --------- | -------------------------- |
| `/files`  | View processed files       |
| `/stats`  | View processing statistics |
| `/errors` | View processing errors     |
| `/trace`  | Trace pipeline steps       |
| `/health` | Health check               |

Example: [http://geethar.mooo.com:8000/health](http://geethar.mooo.com:8000/health)

---

## Uploading Files

To upload files for processing:

### Use rsync (recommended for speed)

```bash
rsync -av input.txt geetha@geethar.mooo.com:watch_dir/unprocessed/
```

You can also manually drop files into the `watch_dir/unprocessed/` folder (inside Docker or locally).

---

## Monitoring

**Better Uptime** or other external monitoring services can ping `/health` to monitor system availability.

Example:

* Monitored URL: `http://geethar.mooo.com:8000/health`

---

## Sample Input(test.txt)

```bash
2025-05-12 10:04:12,512 ERROR api       External API failed: 503 Service Unavailable
2025-05-12 10:05:33,932 INFO  auth      User logout: user1
2025-05-12 09:58:32,456 WARN  auth      Failed login: user1
```

## Sample Output


## Project Structure

```
file-processing-sys/
├── src/
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── cli.py
│       ├── file_watcher.py
│       ├── config/
│       │   └── pipeline.yaml
│       ├── core/
│       │   └── engine.py
│       ├── engine/
│       │   └── runner.py
│       ├── processors/
│       │   ├── __init__.py
│       │   ├── filters.py
│       │   ├── formatters.py
│       │   ├── output.py
│       │   └── start.py
│       ├── dashboard/
│       │   ├── __init__.py
│       │   └── server.py
│       ├── utils/
│       │   ├── metrics.py
│       │   └── tracing.py
│       └── watch_dir/
│           ├── unprocessed/
│           ├── underprocess/
│           └── processed/
├── README.md
├── requirements.txt
├── pyproject.toml
├── docker-compose.yml
├── Makefile
└── Dockerfile
```

