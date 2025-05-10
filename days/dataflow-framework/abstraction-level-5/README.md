# Abstraction-Level-5: DAG-Based Log Processing Framework

## Overview

This project implements a configurable DAG-based streaming line processor for logs. Each line in an input file is routed through a user-defined pipeline of processors based on its content. The routing and processor setup are fully configurable using a YAML file.

## Features

- Modular line processors (trim, tag, archive, count, format, etc.)
- Tagged output and dynamic routing
- Supports fan-in and fan-out DAG execution
- Easily extensible with new processing nodes

## Directory Structure

```

abstraction-level-5/
├── main.py                # CLI entry point
├── cli.py                 # CLI argument parsing
├── dag\_engine.py          # DAG execution engine
├── pipeline.yaml          # DAG and routing configuration
├── processor\_types.py     # Processor interface
├── processors/            # Modular processors
│   ├── **init**.py
│   ├── trim.py
│   ├── tagging.py
│   ├── archiver.py
│   ├── counter.py
│   ├── formatter.py
│   ├── tally.py
│   ├── printer.py

````

## How It Works

1. Input lines are read from a file.
2. Each line passes through a configurable DAG of processors.
3. Each processor may:
   - Transform the line
   - Tag the line for routing
   - Yield it to one or more downstream processors
4. The pipeline routes based on tags using `pipeline.yaml`.

## Installation

Ensure Python 3.8+ and install dependencies:

```bash
pip install pyyaml
````

## Usage

```bash
python main.py --input input.txt --config pipeline.yaml
```

* `--input`: Path to the input file
* `--config`: Path to the DAG pipeline YAML file

## Example

### Input (`input.txt`)

```
[ERROR] Disk full
[WARNING] Low memory
Just a normal message
Another normal message
[ERROR] Timeout occurred
```

### Configuration (`pipeline.yaml`)

Defines:

* Nodes (processors)
* Entry point
* Routing rules based on tags like `errors`, `warnings`, `general`, etc.

See your existing `pipeline.yaml` for the full config example.

### Sample Output

```
[COUNT 1] [ERROR] Disk full
[COUNT 2] [ERROR] Timeout occurred
[ARCHIVED] [ERROR] Disk full
[ARCHIVED] [ERROR] Timeout occurred
Tally[1]: [WARNING] Low memory
* Just a normal message
* Another normal message
```

## Processor Overview

| Processor   | Description                                 |
| ----------- | ------------------------------------------- |
| `trim`      | Strips whitespace from each line            |
| `tagging`   | Tags lines: `errors`, `warnings`, `general` |
| `counter`   | Counts error lines                          |
| `archiver`  | Archives error lines                        |
| `tally`     | Tallies warning lines                       |
| `formatter` | Formats general lines with bullet points    |
| `printer`   | Outputs formatted lines to the terminal     |

## Extending the Pipeline

1. Create a new file in `processors/`.
2. Inherit from `TaggedProcessor`.
3. Implement the `process()` method yielding `(tag, line)` tuples.
4. Update `pipeline.yaml` to include the new node and routing.

## License

This project is intended for educational use during a Python bootcamp. No license is currently specified.


