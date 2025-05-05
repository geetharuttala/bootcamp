# Day 0 - Tasks

## Server Setup (ex-tools-1)

A web server with just one page displaying my name and photo. Used Google Cloud VM and Apache to run the server.
Link: [https://geethar.mooo.com/](https://geethar.mooo.com/)

### Tools Used

* Google Cloud Platform (Compute Engine)
* Apache2 Web Server
* afraid.org (FreeDNS)
* ChatGPT and YouTube for support

### Steps Followed

1. Set up VM on GCP (Debian OS) following [this YouTube tutorial](https://youtu.be/6meDCnIW4sU?si=WvKlXC8kp6Z4ZCoU) and [Google Docs](https://cloud.google.com/compute/docs/tutorials/basic-webserver-apache).
2. Installed Apache with:

   ```bash
   sudo apt update
   sudo apt install apache2
   ```
3. Uploaded HTML and image to `/var/www/html` using the SSH file upload option.
4. Set up free subdomain using [afraid.org](https://freedns.afraid.org) and pointed it to my external IP.
5. Configured Apache with:

   ```bash
   sudo nano /etc/apache2/sites-available/000-default.conf
   # Added: ServerName geethar.mooo.com
   sudo systemctl reload apache2
   ```

### Website Live At

* IP: [http://35.184.39.201](http://35.184.39.201)
* Domain: [https://geethar.mooo.com](https://geethar.mooo.com)

### ChatGPT Help

Used ChatGPT for assistance. [ChatGPT Conversation](https://chat.openai.com/share/6815c99d-cfe8-800c-92ca-581a786a6baf)

---

## Python Module Packaging (ex-basics-1, ex-basics-2, ex-basics-3)

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
day0/
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
cd days/day0
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
