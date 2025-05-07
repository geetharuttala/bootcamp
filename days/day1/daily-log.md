# Bootcamp Daily Log

## Table of Contents

* [Day 1 (doctools)](#day-1)
* [Day 2 (pythonic drills & packaging)](#day-2)

---

## Day 1

### What I Learned

* Basics of Markdown syntax: headings, lists, links, code blocks, tables, and images.
* How to structure a README with purpose, install, usage, and troubleshooting.
* Git best practices: committing only necessary files (daily log), skipping others.
* Visual thinking tools help in design clarity (Mermaid.js, Draw.io, XMind).
* MkDocs and Material theme for documentation sites.
* How to organize project structure to support MkDocs and GitHub.
* Difference between practice tasks and capstone goals.
* How to embed diagrams as exported images if live rendering fails.
* How to build a CLI app using `typer` and style output using `rich`.
* How to install and run CLI tools using `-e .` and custom commands in `pyproject.toml`.
* Importance of marking `src/` as source root in PyCharm to resolve red underlines.
* How to handle shell errors like `!` in passwords and interpreter issues in remote dev.

### What Confused Me

* PyCharm’s Markdown code linting.
* Mermaid plugin setup issues in MkDocs.
* PyCharm red underlines despite working CLI (resolved by marking `src/` as source root).

### Notes

* Use `-e .` to install a package in editable mode when developing locally.
* Ignore false errors in Markdown blocks.
* If Mermaid diagrams don’t render, fall back to exporting and embedding as images.
* If `mkdocs serve` throws an error saying default port (8000) might be busy — use `mkdocs serve -a localhost:8001`.
* Keep `mkdocs.yml` outside `docs/`, ensure filenames in `nav` match exactly.
* Always install any new packages inside the venv.
* Use relative links in Markdown for internal navigation.
* In CLI tools, use single quotes for passwords with special characters in Bash.
* In PyCharm remote dev, ensure correct interpreter and mark `src/` as Sources Root.

### Summary of Work

* Created `index.md`, `login-flow.md`, `block-diagram.md`, and `design-mindmap.md` with clear captions.
* Embedded Draw.io and XMind exports as images in respective pages.
* Set up working `mkdocs.yml` and navigation.
* Restructured repo with clean `docs/`, `README.md`, and root-level `daily-log.md`.
* Ran `mkdocs serve` to preview site locally.
* Used static diagrams instead of Mermaid rendering due to plugin conflict.
* Built a Password Strength Checker CLI tool using `typer` and `rich`.
  * Set up project with `src/` layout, `pyproject.toml`, and CLI entry point.
  * Wrote detailed `README.md` and created `tests/` folder with test guide.
  * Fixed PyCharm environment sync and shell quoting issues.

---

## Day 2

### What I Learned

* Pythonic idioms: unpacking, list comprehensions, dictionary merges.
* Functional tools: lambdas, closures, decorators, `functools`, `itertools`.
* Standard library usage: `collections`, `pathlib`, `tempfile`, `os`, `shutil`.
* YAML config loading with fallback logic (current dir → ENV → default file).
* Used `logging` module and learned how to toggle logs globally and selectively.

### What Confused Me

* Caching issue when running an outdated installed package.
* Debugging why config values didn't apply — turned out to be a install issue.
* Remembering to bump version before republishing.

### Summary of Work

* Built `many-hellos` CLI app that depends on the package `geetha-hello`.
* Added `_config.yaml` fallback logic and verified with:
  * Current directory
  * `CONFIG_PATH` env variable
  * Default file inside module
* Added logging to both config loader and hello module.
* Tested logging toggles:
  * All logs ON
  * Logs OFF
  * Selective logs for just config loader
* Validated results via CLI tests.
