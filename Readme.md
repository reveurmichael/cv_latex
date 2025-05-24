# LaTeX CV Builder

This repository contains a LaTeX CV template with multiple build options.

## Quick Setup

The easiest way to get started is to use our interactive setup tool:

```bash
python cv_setup.py
```

Alternatively, you can use the command-line setup tool:

```bash
# Set up everything at once
python setup.py --all

# Or choose specific components
python setup.py --vscode      # Set up VSCode configuration
python setup.py --devcontainer # Set up DevContainer
python setup.py --docker      # Build using Docker
```

## Build Options

Choose the build method that works best for your workflow:

1. **[Local Build](./Readme-Local.md)** - Build directly on your machine using VSCode/Cursor and LaTeX Workshop
2. **[Docker Build](./Readme-Docker.md)** - Build using Docker without installing LaTeX locally
3. **[GitHub Actions](./Readme-GitHub-Actions.md)** - Automated builds and releases with GitHub Actions

## Sample CV

This repository includes a sample CV for demonstration purposes.

## Template Sources

You can also explore other templates:
- https://www.overleaf.com/gallery/tagged/cv

## Demo Repository

This project is based on: https://github.com/reveurmichael/cv_latex

## Setup Scripts

This repository includes several Python scripts to help you set up your environment:

- `cv_setup.py` - Interactive menu-driven setup tool (recommended for beginners)
- `setup.py` - Command-line setup tool for advanced users
- `setup_vscode.py` - Creates `.vscode/settings.json` with LaTeX Workshop configuration
- `setup_devcontainer.py` - Creates `.devcontainer/devcontainer.json` for containerized development
- `docker_build.py` - Cross-platform script to build with Docker

These scripts work on Windows, macOS, and Linux, ensuring a consistent experience across platforms.

## LaTeX Workshop extension for VSCode/Cursor

Install the **LaTeX Workshop** extension for VSCode/Cursor.

Then, install TexLive:

- https://github.com/James-Yu/LaTeX-Workshop/wiki/Install

On MacOS:

```bash
brew install texlive
```

On Windows:
- Install TexLive 
- Install Perl 

After installation, run our setup script to configure VSCode:

```bash
python setup.py --vscode
```

## Compilation of Tex file

1. Open your `.tex` file in VSCode/Cursor
2. Click the "Build LaTeX" button (green play button)
3. PDF output will be generated automatically

Or, even better, on saving the file, the PDF will be generated automatically.

## `.gitignore`

```
~*
~*.pptx
~*.docx
~*.pdf
*/_build/**
__pycache__
**/__pycache__/**
.pytest_cache
.vscode
.idea
/cmake-build-debug/
/out/
/experiments/
~$*
*~
*.swp
*.swo
.ipynb_checkpoints
*.pyc
/venv/
*.py[cod]
*.DS_Store
*/tmp/*
/tmp/
*/tmp/**
*/**/node_modules/*
*/node_modules/*
*/.python-version
.python-version
*.aux
*.lof
*.log
*.lot
*.fls
*.out
*.toc
*.fmt
*.fot
*.cb
*.cb2
*.ptc
.*.lb
*.bbl
*.bcf
*.blg
*-blx.aux
*-blx.bib
*.run.xml
*.fdb_latexmk
*.synctex
*.synctex(busy)
*.synctex.gz
*.synctex.gz(busy)
*.pdfsync
latex.out/
# algorithms
*.alg
*.loa
*.pdf
```

## GitHub Actions 

For automated builds and releases with GitHub Actions, see [GitHub Actions README](./Readme-GitHub-Actions.md).

