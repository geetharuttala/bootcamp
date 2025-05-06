# Day 1 - Developer Documentation: Tools & Best Practices

## Overview

This day focused on building foundational skills in developer documentation, including Markdown writing, visual diagrams, and MkDocs site setup.

---

## What I Worked On

### Markdown Practice
- Created a **Markdown cheatsheet** with headings, links, lists, code blocks, tables, and images.
- Wrote a guide on **README authoring**: purpose, install steps, usage examples, troubleshooting.

### Daily Log
- Maintained a `daily-log.md` journal noting what I learned and what confused me.

### Visual Documentation
- **Login Flow**: Created a sequence diagram (PNG) showing user interactions with frontend, backend, and database.
- **Block Diagram**: Built a system architecture layout using Draw.io.
- **Mind Map**: Used XMind to outline design document structure.

### MkDocs Setupmv
- Installed MkDocs and the Material theme:
  ```bash
  pip install mkdocs
  pip install mkdocs-material
  ````

* Created a `mkdocs.yml` configuration file at the project root.
* Organized documentation inside the `docs/` folder.
* Exported visual diagrams as `.png` and stored them in `docs/assets/`.
* Edited `mkdocs.yml` to define the navigation menu:

  ```yaml
  nav:
    - Home: index.md
    - README: readme.md
    - Sequence Diagram: sequence.md
    - Block Diagram: block-diagram.md
    - Design: design.md
    - Architecture: architecture.md
  ```
* Served the site locally:

  ```bash
  mkdocs serve
  ```

  * In case of port conflict:

    ```bash
    mkdocs serve -a localhost:8001
    ```
* Mermaid diagrams didn't render due to plugin issues, so I used exported images instead. 
* Docs site previewed locally at: http://127.0.0.1:8000/

---

## Folder Structure

```text
day1/
├── README.md               
├── docs/
│   ├── assets/
│   │   ├── sequence.png
│   │   ├── block-diagram.png
│   │   └── passchecker-mindmap.png
│   ├── architecture.md
│   ├── block-diagram.md
│   ├── design.md
│   ├── sequence.md
│   └── index.md
├── markdown/
│   ├── markdown-cheatsheet.md
│   └── readme-authoring.md
├── mkdocs.yml
├── daily-log.md
```

---