# Password Strength Checker CLI

Welcome to the documentation site for the **Password Strength Checker**, a simple and effective command-line tool that evaluates the strength of a password using visual and color-coded feedback.

---

## Features

- Command-line interface built with [`typer`](https://typer.tiangolo.com/)
- Styled output using [`rich`](https://rich.readthedocs.io/)
- Evaluates password strength based on:
  - Length
  - Case sensitivity
  - Special characters
  - Numeric digits
- Easy to install and use locally
- Fully testable and extensible

---

## Project Structure

```text
password-strength-checker/
├── src/passcheck/        # CLI logic and core checker
├── tests/                # Unit tests for checker logic
├── docs/                 # MkDocs documentation
├── README.md             # CLI usage and installation guide
├── pyproject.toml        # Typer CLI entry point configuration
```