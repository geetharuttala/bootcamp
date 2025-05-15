# Abstraction Level 6 – Stateful Tag-Based Routing Engine

## Goal

Build a **stateful, configurable routing engine** that processes streaming text data using dynamically loaded processors based on tags. This level introduces:

* A routing graph where nodes are processing functions
* Tagged output, enabling conditional fan-out and fan-in
* Modular, pluggable processors via YAML config
* Stateful processors that operate over `(tag, line)` streams
* (New) Graph visualization to debug and inspect routing
* (Planned) Cycle detection and config validation

---

## Features

* Dynamic routing based on emitted tags
* Modular processor registration using import paths
* Fan-in / fan-out routing logic
* Tagged stateful processors
* Start–End lifecycle: processing starts at a `start` node and ends at an `end` node
* Visualization of routing graph using `networkx` + `matplotlib`

---

## Example Config

```yaml
nodes:
  - tag: start
    type: ab6.processors.start.tag_lines
  - tag: error
    type: ab6.processors.filters.only_error
  - tag: warn
    type: ab6.processors.filters.only_warn
  - tag: general
    type: ab6.processors.formatters.snakecase
  - tag: end
    type: ab6.processors.output.terminal

edges:
  - from: start
    to: error
  - from: start
    to: warn
  - from: start
    to: general
  - from: error
    to: end
  - from: warn
    to: end
  - from: general
    to: end
````

---

## Sample Input (`input.txt`)

```
[INFO] ServiceStartedSuccessfully
[WARN] DiskSpaceLow
[ERROR] FailedToConnectToDatabase
```

## Sample Output (from terminal)

```
END: [FORMATTED] service_started_successfully
END: [FORMATTED] disk_space_low
END: [FORMATTED] failed_to_connect_to_database
```

---

## How to Run

```bash
# Without visualization
python -m ab6.main --input input.txt --config config.yaml

# With routing graph visualization
python -m ab6.main --input input.txt --config config.yaml --visualize
```

This will:

1. Load the YAML-defined processor DAG
2. Begin at the `start` tag
3. Route and process lines dynamically based on emitted tags
4. Print final output via the `end` processor
5. If `--visualize` is set, it will save a routing diagram to `routing_graph.png`

---

## Project Structure

```
abstraction-level-6/
├── ab6/                         # Main package directory
│   ├── __init__.py
│   ├── main.py                  # CLI entrypoint
│   ├── router_engine.py         # Core routing logic + visualization
│   ├── config_loader.py 
│   ├── common/
│       ├── __init__.py
│   │   └── types.py             # TaggedLine definition
│   └── processors/              # Modular processors
│       ├── __init__.py
│       ├── start.py             # Emits initial tags
│       ├── filters.py           # Tag-based filters (error, warn, etc.)
│       ├── formatters.py        # Formatters (e.g., snakecase)
│       └── output.py            # Terminal or file output processors
├── config.yaml                  # Sample processor DAG configuration
├── input.txt                    # Sample input lines
├── routing_graph.png            # Visualized routing DAG (output)
├── requirements.txt             # Project dependencies
└── README.md                    # Project overview and instructions

```

---

## Requirements

See below `requirements.txt` or install directly:

```bash
pip install -r requirements.txt
```

---

## requirements.txt

```txt
pyyaml
typer
rich
matplotlib
networkx
```

---

