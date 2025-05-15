## Python Module Packaging 

### `geetha-hello`

A simple Python package that says hello

[![TestPyPI Version](https://img.shields.io/badge/TestPyPI-geetha--hello-informational?logo=pypi\&labelColor=gray\&color=blue)](https://test.pypi.org/project/geetha-hello/)

### Description

`geetha-hello` is a minimal Python package that provides a friendly greeting. It is designed to test Python packaging and publishing workflows. It also includes a Typer-based CLI to say hello from the terminal.

### Installation

From TestPyPI:

```bash
uv pip install -i https://test.pypi.org/simple/ geetha-hello
```

Or in editable mode during development:

```bash
uv pip install -e .
```

### Usage

In Python:

```python
from geetha_hello.hello import say_hello

print(say_hello())           # Output: Hello, world!
print(say_hello("Geetha"))   # Output: Hello, Geetha!
```

From CLI:

```bash
geetha-hello                      # Output: Hello, world!
geetha-hello --name Geetha        # Output: Hello, Geetha!
```

### Project Structure

```
ex-basics-3/
├── src/
│   └── geetha_hello/
│       ├── __init__.py
│       ├── hello.py
│       └── cli.py
├── pyproject.toml
├── README.md
└── ...
```

### Setting Up on SSH Server (with uv)

1. Clone the repository into your SSH server (if not already done):

```bash
git clone git@github.com:geetharuttala/bootcamp.git
```

2. Navigate to the cloned repo:

```bash
cd ~/bootcamp
```

3. Create the virtual environment named `bootcamp` inside the repo folder:

```bash
uv venv bootcamp
```

4. Activate the virtual environment:

```bash
source ~/bootcamp/bootcamp/bin/activate
```

Note: The reason the command has two `bootcamp` segments is because:

* The first `bootcamp` is your repo folder (from GitHub)
* The second `bootcamp` is the virtual environment directory inside it

5. Navigate to your package directory:

```bash
cd basics
```

6. Install the package in editable mode:

```bash
uv pip install -e .
```

7. Run the CLI to confirm:

```bash
geetha-hello
geetha-hello --name Geetha
```

### Tips for Working Between PyCharm and SSH

* If you change code in PyCharm (local machine), you must **commit and push** to GitHub.
* On your SSH server, **pull the latest changes** using:

```bash
cd ~/bootcamp
git pull origin main
```

* Your SSH PyCharm interpreter will use the remote venv directly.
* To activate the venv manually in the terminal:

```bash
source ~/bootcamp/bootcamp/bin/activate
```

### Links

* [View on TestPyPI](https://test.pypi.org/project/geetha-hello/)
* [GitHub Repository](https://github.com/geetharuttala/bootcamp/tree/main/days/day0)
* [Asciinema Demo](https://asciinema.org/a/SyUQvXPtwQ2JwJaU3qnag2VMC)
* [Live Website](https://geethar.mooo.com)

---

### Author

Geetha Ruttala

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
