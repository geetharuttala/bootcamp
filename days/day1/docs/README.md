# Password Strength Checker

A simple and interactive CLI tool to evaluate the strength of passwords based on length, character variety, and complexity. Built using Python, [Typer](https://typer.tiangolo.com/) for the CLI interface, and [Rich](https://rich.readthedocs.io/) for colorful output.

---

## Documentation

📚 **View Full Docs:**  
 [Password Strength Checker Documentation (MkDocs)](https://geetharuttala.github.io/bootcamp/password-strength-checker)

Includes:
- Sequence diagram
- Block diagram
- Design & architecture write-up
- CLI interface explanation

---

## Purpose

Weak passwords are a common security risk. This tool helps users **check the strength** of a password before using it — ideal for personal use, scripting, or integration into onboarding flows where password validation is required.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/geetharuttala/bootcamp.git
cd password-strength-checker
````

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/macOS
# OR
.venv\Scripts\activate     # On Windows
```

### 3. Install the Project

We recommend using [uv](https://github.com/astral-sh/uv) for fast dependency management, but pip also works.

#### With `uv`:

```bash
uv pip install -e .
```

#### Or with pip:

```bash
pip install -e .
```

---

## Usage

Run the CLI using the installed command:

```bash
passcheck 'YourPassword123'
```

> ✅ Use **single quotes** around the password to avoid shell interpretation issues.

### Example Outputs

```bash
$ passcheck 12345678
Password Strength: Weak 

$ passcheck 'Random@257'
Password Strength: Moderate 

$ passcheck 'G33tha$SuperPass2025!'
Password Strength: Strong 
```

---

## Troubleshooting

### "Command not found: passcheck"

* Make sure you installed the project in **editable mode** with `-e .`
* Confirm your virtual environment is activated:
  Run `which python` or `which passcheck` to confirm it's from `.venv/bin/`

### Imports showing red in PyCharm

* **Mark `src/` folder as "Sources Root"** in PyCharm to resolve import errors.
* Make sure the correct interpreter (`.venv/bin/python`) is selected in your project settings.
* Restart PyCharm or run `File → Invalidate Caches / Restart…` if needed.

### Bash error: `!Password123: event not found`

Use **single quotes** around the password:

```bash
passcheck 'MyStrong!Password123'
```

Or escape the `!` like this:

```bash
passcheck "MyStrong\!Password123"
```

---

## Project Structure

```
password-strength-checker/
├── pyproject.toml
├── README.md
├── src/
│   └── passcheck/
│       ├── __init__.py
│       └── checker.py
├── tests/
│   ├── test_checker.py
│   └── README.md
├── docs/
│   ├── index.md
│   ├── sequence.md
│   ├── block-diagram.md
│   ├── design.md
│   └── architecture.md
├── mkdocs.yml
```

---

## Features

* Password strength evaluated as **Weak**, **Moderate**, or **Strong**
* Checks for:

  * Minimum length
  * Digits
  * Upper/lowercase letters
  * Special characters
* CLI made with [Typer](https://typer.tiangolo.com/)
* Styled output using [Rich](https://rich.readthedocs.io/)
* Testable via `pytest`

---

## Author

**Geetha R**
Part of bootcamp Day 1 Capstone

---

## 📄 License

MIT License



