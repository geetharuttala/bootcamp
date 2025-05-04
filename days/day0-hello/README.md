````markdown
# geetha-hello

> A simple Python package that says hello 👋

[![TestPyPI Version](https://img.shields.io/badge/TestPyPI-geetha--hello-informational?logo=pypi&labelColor=gray&color=blue)](https://test.pypi.org/project/geetha-hello/)

---

## ✨ Description

`geetha-hello` is a minimal Python package that provides a friendly greeting.  
Perfect for testing Python packaging and publishing workflows!

Now includes a **Typer-based CLI** to say hello from your terminal! 🎉

---

## 📦 Installation

From **TestPyPI**:

```bash
uv pip install -i https://test.pypi.org/simple/ geetha-hello
````

Using `uv` (recommended for development):

```bash
uv pip install -e .
```

---

## 🚀 Usage

### In Python

```python
from geetha_hello.hello import say_hello

print(say_hello())           # Output: Hello, world!
print(say_hello("Geetha"))   # Output: Hello, Geetha!
```

### From CLI

```bash
geetha-hello                # Output: Hello, world!
geetha-hello --name Geetha        # Output: Hello, Geetha!
```

---

## 📁 Project Structure

```
day0-hello/
├── src/
│   └── geetha_hello/
│       ├── __init__.py
│       ├── hello.py
│       └── cli.py
├── pyproject.toml
├── README.md
└── ...
```

---

## 🔗 Links

* 📦 [View on TestPyPI](https://test.pypi.org/project/geetha-hello/)
* 🐙 [GitHub Repository](https://github.com/geetharuttala/geetha-hello)

---

## 👩‍💻 Author

**Geetha Ruttala**

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
