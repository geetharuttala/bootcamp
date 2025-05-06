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
* Docs site previewed locally at: http://localhost:8000/

---

## Deployment to GCP Server

To host my MkDocs site at [https://geethar.mooo.com/docs](https://geethar.mooo.com/docs), I followed these steps:

### Build the static site:

```bash
mkdocs build
````

This created a `site/` directory with all the HTML files.

### Transfer the site to my GCP VM:

Used PyCharm’s built-in deployment (via SSH interpreter) to upload the `site/` folder contents to `/home/bootcamp/docs`.

### Move files to Apache’s web root:

SSH into the GCP VM as the `geetharuttala0106` user (who has sudo privileges):

```bash
ssh geetharuttala0106@geethar.mooo.com
```

Move uploaded files to `/var/www/html/docs/`:

```bash
sudo mv /home/bootcamp/docs /var/www/html/docs
```

### Update Home Page:

* Added a styled HTML landing page with my photo and name.
* Included a link to the docs in homepage:
 [View Documentation →](https://geethar.mooo.com/docs)

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