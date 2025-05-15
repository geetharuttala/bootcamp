# many-hellos

A command-line tool that greets multiple people using the `geetha-hello` package. This project demonstrates how to build a reusable CLI by consuming an external Python package with support for YAML configuration and logging.

---

## Project Structure

```

basic-drills/
├── README.md
└── exercises/
    ├── many-hellos/
    └── configs.bak/
     

````

---

## Features

- Accepts multiple names via CLI and greets each using `say_hello` from `geetha-hello`
- Repeats the greeting based on a `num_times` value configured in `_config.yaml`
- Supports config loading from:
  - Current directory
  - Environment variable `CONFIG_PATH` (colon-separated list)
  - Default bundled config inside the `geetha-hello` module
- Logging integration (optional):
  - Log where the config was loaded from
  - Turn on or off specific loggers (e.g., only for config loader)

---

## Installation

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
````

### 2. Install `geetha-hello` from TestPyPI

```bash
uv pip install --index-url https://test.pypi.org/simple/ --no-deps geetha-hello==0.1.11
```

---

## Usage

### Basic usage

```bash
python main.py Geetha Anil Maya
```

> Output:

```
Hello, Geetha!
Hello, Anil!
Hello, Maya!
```

---

## Configuration Options

The greeting repetition is controlled by a YAML config with a `num_times` field.

### Option A: Current directory

Create a file called `_config.yaml` in the same folder where you run the command:

```yaml
num_times: 2
```

```bash
python main.py Geetha
```

> Output:

```
Hello, Geetha!
Hello, Geetha!
```

---

### Option B: Environment variable (`CONFIG_PATH`)

```bash
export CONFIG_PATH=/path/to/config/dir1:/another/path
```

Each path will be searched for `_config.yaml`.

---

### Option C: Fallback (default bundled config)

If no file is found, it will use the default config bundled inside the `geetha-hello` package:

```yaml
num_times: 1
```

---

## Logging (Optional)

You can enable logging by editing `main.py`:

```python
import logging

logging.basicConfig(level=logging.INFO)  # Turn ON
# logging.getLogger("geetha_hello.config_loader").setLevel(logging.INFO)  # Selective logging
```

### Example: Enable logging only for the config loader

```python
logging.basicConfig(level=logging.WARNING)
logging.getLogger("geetha_hello.config_loader").setLevel(logging.INFO)
```

---

## Testing Matrix

| Scenario                            | Config Source     | Output Behavior          |
| ----------------------------------- | ----------------- | ------------------------ |
| `_config.yaml` in current directory | Current directory | Uses local config        |
| No local, but `CONFIG_PATH` set     | Env var           | Uses env config          |
| Neither present                     | Bundled default   | Uses default `num_times` |
| Logging ON                          | Logging enabled   | Shows config source logs |
| Logging OFF                         | No logs           | Silent config detection  |

---

## Reusability

This project reuses the `geetha-hello` library as a clean module:

* Isolated config loading
* No side effects on import
* Logging is caller-controlled
* CLI uses standard `typer` patterns

---

## Dependencies

* [typer](https://typer.tiangolo.com/)
* [rich](https://rich.readthedocs.io/)
* [pyyaml](https://pyyaml.org/)
* `geetha-hello` from [TestPyPI](https://test.pypi.org/project/geetha-hello/0.1.9/)

---

## Related Projects

* [geetha-hello](https://test.pypi.org/project/geetha-hello/0.1.9/) — the core package this project depends on.

---

## Author

Geetha R

