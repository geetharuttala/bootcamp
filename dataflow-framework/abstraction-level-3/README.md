# Abstraction Level 3

## Overview

In **Level 3**, the line-processing framework takes a significant leap forward in abstraction and flexibility. The processing logic is now **fully decoupled from the code**, allowing the user to define processing steps through an external **YAML configuration file**. This opens the door to **extensibility**, enabling users to build and plug in their own processors without modifying your source code.

## Features

* Dynamically loads processing functions based on dotted import paths defined in `pipeline.yaml`.
* Replaces static mode-based pipelines with fully **config-driven workflows**.
* Clean and modular codebase organized across `cli.py`, `core.py`, `pipeline.py`, and a dedicated `processors/` module.
* Enhanced CLI interface that supports input file path and pipeline configuration file.

## Folder Structure

```
abstraction-level-3/
├── main.py
├── cli.py
├── core.py
├── pipeline.py
├── processor_types.py
├── pipeline.yaml
└── processors/
    ├── upper.py
    └── snake.py
```

## How it works

1. **pipeline.yaml** defines the list of transformations:

   ```yaml
   pipeline:
     - type: processors.snake.to_snakecase
     - type: processors.upper.to_uppercase
   ```

2. **pipeline.py** dynamically imports the listed functions using Python’s importlib.

3. Each function is a simple `str -> str` processor that is composed into a pipeline and applied to each line of the input.

4. The final transformed lines are either printed or written to an output file.

## Usage

```bash
python main.py --input input.txt --config pipeline.yaml
```

* `--input`: Required, path to the input text file.
* `--config`: Required, path to the pipeline YAML configuration.

## Sample Input and Output

### Input (`input.txt`)

```
hello world
dynamic import paths
```

### pipeline.yaml

```yaml
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase
```

### Output

```
HELLO_WORLD
DYNAMIC_IMPORT_PATHS
```

## Abstraction Level 3

At this stage:

* Your pipeline is now **driven by external configuration**.
* You’ve eliminated hardcoded logic and modes, replacing them with importable, composable functions.
* Each processor lives in its own module and follows a clean signature: `def processor(line: str) -> str`.
* Users can extend your tool by writing their own processors and referencing them via dotted paths in `pipeline.yaml`.

This level introduces a **plugin-style architecture**, where behavior can be modified without editing the core source — a key milestone in designing modular, reusable systems.

---

