# Architecture Overview

## Code Layout

```

password-strength-checker/
├── src/passcheck/
│   ├── checker.py        # Password evaluation logic
│   └── **init**.py       # CLI entry point using Typer
├── tests/
│   └── test\_checker.py   # Unit tests for password strength logic
├── pyproject.toml        # CLI setup, dependencies

```

## Entry Point

The command `passcheck` maps to `passcheck.__init__:app` using Typer's CLI system.

## Dependency Flow

- `typer` → command and argument parsing
- `checker.py` → core strength logic
- `rich` → outputs styled messages to user

## Development Notes

- Supports local dev via `pip install -e .`
- Testable via `pytest`
- Easily extendable (e.g., masked input, GUI)




