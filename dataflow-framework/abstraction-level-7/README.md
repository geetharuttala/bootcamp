# Abstraction Level 7 – Observability and System Introspection

This level adds real-time observability features to the streaming line processor system. It enables live tracking of metrics, execution traces, and error reports through a FastAPI-powered dashboard.

## Overview

In this level, the dataflow framework is enhanced with:

- A metrics store to track processing stats (e.g., count, errors)
- Tracing of how each line flows through the DAG
- A FastAPI dashboard running concurrently to expose real-time introspection data

## Features

- Per-processor metrics: count of lines, tags, processing stages
- Tracing of individual lines through the DAG
- Error logging with timestamps and processor context
- REST API for observability data
- Dashboard runs on a background thread

## CLI Usage

```bash
python cli.py --input input.txt --config config/pipeline.yaml --trace
````

* `--input`: Path to the input file to be processed
* `--config`: Path to the YAML pipeline configuration
* `--trace`: Enables tracing and the live dashboard server

## API Endpoints

| Endpoint  | Description                            |
| --------- | -------------------------------------- |
| `/stats`  | Returns current processing metrics     |
| `/trace`  | Shows recent traces of processed lines |
| `/errors` | Lists recent processing errors         |

## Sample Input

**input.txt**

```
This is a normal info line.
Warning: Disk space low.
ERROR: Unable to connect to server.
Just another general line.
warn: CPU usage high.
```

**pipeline.yaml**

```yaml
start: general
processors:
  general:
    type: filters.tag
    next: [output]
  output:
    type: output
```

## Sample Output

**Terminal Output**

```
[OUTPUT] [SNAKE] this_is_a_normal_info_line.
[OUTPUT] [WARN] Warning: Disk space low.
[OUTPUT] [ERROR] ERROR: Unable to connect to server.
[OUTPUT] [SNAKE] just_another_general_line.
[OUTPUT] [WARN] warn: CPU usage high.
```

**/stats**

```json
{
  "general": 2,
  "end": 5,
  "warn": 2,
  "error": 1
}
```

**/trace**

```json
[
  { "tag": "general", "line": "This is a normal info line." },
  { "tag": "end", "line": "[SNAKE] this_is_a_normal_info_line." },
  { "tag": "warn", "line": "Warning: Disk space low." },
  { "tag": "end", "line": "[WARN] Warning: Disk space low." },
  { "tag": "error", "line": "ERROR: Unable to connect to server." },
  { "tag": "end", "line": "[ERROR] ERROR: Unable to connect to server." }
]
```

**/errors**

```json
[
  {
    "processor": "output",
    "message": "ERROR: Unable to connect to server.",
    "timestamp": 1715324537.2782745
  }
]
```

## Dashboard Screenshots

You can visit the following URL during execution to observe live metrics and diagnostics:

Use `curl`, browser, or tools like Postman to inspect the live data.

```
http://localhost:8000/stats
http://localhost:8000/trace
http://localhost:8000/errors
```
### Stats Dashboard
![Stats Dashboard](/days/dataflow-framework/abstraction-level-7/images/stats.png)

### Trace Dashboard
![Trace Dashboard](/days/dataflow-framework/abstraction-level-7/images/trace.png)

### Errors Dashboard
![Errors Dashboard](/days/dataflow-framework/abstraction-level-7/images/errors.png)

---

## Internals

* The FastAPI app is launched on a background thread using `uvicorn`
* Metrics and traces are shared via thread-safe stores (`MetricsStore`, `TraceStore`)
* Errors are logged with timestamps and returned as structured JSON


## Folder Structure

```

abstraction-level-7/
├── cli.py
├── main.py
├── config/
│   └── pipeline.yaml
├── input.txt
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
├── README.md
├── requirements.txt

````



