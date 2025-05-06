# geetha-hello

A simple Python CLI application that prints a greeting message. Built as part of a Python packaging and documentation bootcamp.

---

## Purpose

This project demonstrates how to:
- Create a Python package using the `src/` layout
- Build a CLI with [`typer`](https://typer.tiangolo.com)
- Add styled terminal output using [`rich`](https://rich.readthedocs.io)
- Publish to TestPyPI

---

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/geetha-hello.git
   cd geetha-hello


2. (Optional) Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the package:

   ```bash
   pip install -e .
   ```

Or install directly from TestPyPI:

```bash
pip install -i https://test.pypi.org/simple geetha-hello
```

---

## Usage

Once installed, you can run the CLI like this:

```bash
geetha-hello --name Geetha
```

This will output something like:

```text
Hello, Geetha! 
```

---

## Troubleshooting

* **Command not found:** Make sure your environment’s `bin/` directory is in your PATH.
* **Permission denied:** Try using `pip install --user` if you're not in a virtual environment.
* **No module named `typer` or `rich`:** Make sure dependencies are installed (`pip install -r requirements.txt` if you have one).
* If installing from TestPyPI, ensure the URL is correct and package name matches.

---

## 📄 License

MIT

---

## 👩‍💻 Author

Geetha R

---

