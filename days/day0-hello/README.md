# Day 0 - Bootcamp Tasks

## 🧰 Exercise 1: Server Setup (ex-tools-1)

A web server with just one page displaying my name and photo. Used Google Cloud VM and Apache to run the server.
🔗 [Website link](https://geethar.mooo.com/)

### 🔧 Tools Used

* Google Cloud Platform (Compute Engine)
* Apache2 Web Server
* afraid.org (FreeDNS)
* ChatGPT and YouTube for support

### ⚙️ Steps Followed

1. **Set up VM** on GCP (Debian OS) following [this YouTube tutorial](https://youtu.be/6meDCnIW4sU?si=WvKlXC8kp6Z4ZCoU) and [Google Docs](https://cloud.google.com/compute/docs/tutorials/basic-webserver-apache).
2. **Installed Apache** with:

   ```bash
   sudo apt update
   sudo apt install apache2
   ```
3. **Uploaded HTML and image** to `/var/www/html` using the SSH file upload option.
4. **Set up free subdomain** using [afraid.org](https://freedns.afraid.org) and pointed it to my external IP.
5. **Configured Apache** with:

   ```bash
   sudo nano /etc/apache2/sites-available/000-default.conf
   # Added: ServerName geethar.mooo.com
   sudo systemctl reload apache2
   ```

### ✅ Website Live At

* IP: [http://35.184.39.201](http://35.184.39.201)
* Domain: [Website link](https://geethar.mooo.com/)

### 🧐 ChatGPT Help

Used ChatGPT for assistance. [ChatGPT Conversation](https://chatgpt.com/share/6815c99d-cfe8-800c-92ca-581a786a6baf)

---

## 🐍 Exercise 2: Python Module Packaging (ex-basics-1)

### 📆 `geetha-hello`

> A simple Python package that says hello 👋

[![TestPyPI Version](https://img.shields.io/badge/TestPyPI-geetha--hello-informational?logo=pypi\&labelColor=gray\&color=blue)](https://test.pypi.org/project/geetha-hello/)

### ✨ Description

`geetha-hello` is a minimal Python package that provides a friendly greeting. Perfect for testing Python packaging and publishing workflows! Now includes a **Typer-based CLI** to say hello from your terminal! 🎉

### 📆 Installation

From **TestPyPI**:

```bash
uv pip install -i https://test.pypi.org/simple/ geetha-hello
```

Or install in editable mode during development:

```bash
uv pip install -e .
```

### 🚀 Usage

#### In Python

```python
from geetha_hello.hello import say_hello

print(say_hello())           # Output: Hello, world!
print(say_hello("Geetha"))   # Output: Hello, Geetha!
```

#### From CLI

```bash
geetha-hello                      # Output: Hello, world!
geetha-hello --name Geetha        # Output: Hello, Geetha!
```

### 📁 Project Structure

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

### 🔗 Links

* 📆 [View on TestPyPI](https://test.pypi.org/project/geetha-hello/)
* 🔙 [GitHub Repository](https://github.com/geetharuttala/bootcamp/tree/main/days/day0-hello)
* 🎮 [Asciinema Demo](https://asciinema.org/a/SyUQvXPtwQ2JwJaU3qnag2VMC)

---

### 👩‍💻 Author

**Geetha Ruttala**

### 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
