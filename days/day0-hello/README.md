# geetha-hello

> A simple Python package that says hello 👋

[![TestPyPI Version](https://img.shields.io/badge/TestPyPI-geetha--hello-informational?logo=pypi&labelColor=gray&color=blue)](https://test.pypi.org/project/geetha-hello/)

---

## ✨ Description

`geetha-hello` is a minimal Python package that provides a friendly greeting using `rich`.  
Perfect for testing Python packaging, CLI tools, and publishing workflows!

---

## 📦 Installation

From **TestPyPI**:

```bash
pip install -i https://test.pypi.org/simple/ geetha-hello
```

---

## 🚀 Usage

### 1. As a Python module

```python
from geetha_hello.hello import say_hello

say_hello()           # Output: Hello, World!
say_hello("Geetha")   # Output: Hello, Geetha!
```

### 2. As a CLI script

```bash
python -m geetha_hello.hello
# Output: Hello, World!

python -m geetha_hello.hello Geetha
# Output: Hello, Geetha!
```

✅ Uses the [rich](https://pypi.org/project/rich/) library to display colored text in the terminal.

---

## 📁 Project Structure

```
geetha-hello/
├── src/
│   └── geetha_hello/
│       ├── __init__.py
│       └── hello.py
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
