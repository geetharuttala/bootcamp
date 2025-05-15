# Abstraction Level 4

## Overview

**Abstraction Level 4** introduces **stream-based processing**, allowing processors to:

* Handle input as a stream of lines (`Iterator[str]`)
* Emit **zero**, **one**, or **multiple** output lines per input line
* Maintain **internal state** across lines
* Be **configured independently** using options in the config file

This level lays the foundation for real-world data pipelines that support **fan-in**, **fan-out**, and **stateful processing**.

---

## Features Introduced

* Streaming processor interface: `Iterator[str] → Iterator[str]`
* Legacy `str → str` processors still reusable via decorators
* **Fan-out support** (e.g., splitting a line into words)
* **Stateful processing** (e.g., line counter)
* Processor-specific configuration via `pipeline.yaml`

---

## Directory Structure

```
abstraction-level-4/
├── main.py
├── cli.py
├── core.py
├── pipeline.py
├── types.py
├── pipeline.yaml
└── processors/
    ├── upper.py              # to_uppercase: str → str
    ├── snake.py              # to_snakecase: str → str
    ├── fanout_splitter.py    # SplitLines: stream-based, fan-out
    └── stateful_counter.py   # LineCounter: stream-based, stateful
```

---

## How It Works

The `pipeline.yaml` defines the processing steps using full import paths and optional config:

```yaml
pipeline:
  - type: processors.stateful_counter.LineCounter
    config:
      prefix: "Line"
  - type: processors.upper.to_uppercase
  - type: processors.fanout_splitter.SplitLines
    config:
      delimiter: " "
```

This config defines a **3-step stream pipeline**:

1. **LineCounter** – Prefixes each line with `"Line {n}:"`
2. **to\_uppercase** – Converts the line to uppercase
3. **SplitLines** – Splits the line into multiple lines using space as the delimiter

---

## Sample Input (`input.txt`)

```
hello world
python is fun
data flow pipelines are powerful
```

---

## Output

```
LINE
1:
HELLO
WORLD
LINE
2:
PYTHON
IS
FUN
LINE
3:
DATA
FLOW
PIPELINES
ARE
POWERFUL
```

Each input line was:

1. Counted and tagged (e.g., `Line 1:`)
2. Transformed to uppercase
3. Split into multiple lines based on spaces

---

## How to Run

```bash
python main.py --input input.txt --config pipeline.yaml
```

---

## Checklist

* [x] Processors support `Iterator[str] -> Iterator[str]`
* [x] Legacy `str -> str` functions are reused via wrappers
* [x] `LineCounter` maintains state and emits prefix
* [x] `SplitLines` performs fan-out
* [x] Configuration passed cleanly to processors
* [x] All processors are testable in isolation

