# LaTeX CV Builder

This repository contains a LaTeX CV template with multiple build options to accommodate different user preferences and environments.

## Quick Setup

The easiest way to get started is to use our interactive setup tool:

```bash
python interactive_setup.py
```

Alternatively, you can use the command-line setup tool:

```bash
python cli_setup.py --all
```

## Build Methods Comparison

This repository demonstrates multiple approaches to building LaTeX documents, each with different advantages:

| Build Method | Advantages | Disadvantages | Best For |
|--------------|------------|--------------|----------|
| **Local** | - Fast builds<br>- No internet required<br>- Full editor integration | - Requires LaTeX installation<br>- Environment setup needed | Daily development, frequent edits |
| **Docker** | - Consistent environment<br>- No local LaTeX install needed<br>- Works across platforms | - Requires Docker<br>- Slower initial setup | Team projects, complex documents |
| **GitHub Actions** | - Fully automated<br>- Builds on push<br>- PDF release management | - Requires internet<br>- Not for frequent iteration | Production builds, public sharing |

Having multiple build methods provides redundancy and flexibility across different platforms and scenarios.

## Build Options Documentation

Detailed instructions for each build method:

1. **[Local Build](./Readme-Local.md)** - Build directly on your machine using VSCode/Cursor and LaTeX Workshop
2. **[Docker Build](./Readme-Docker.md)** - Build using Docker without installing LaTeX locally
3. **[GitHub Actions](./Readme-GitHub-Actions.md)** - Automated builds and releases with GitHub Actions

## Setup Tools

This repository includes several Python scripts to help you set up your environment:

- `interactive_setup.py` - Interactive menu-driven setup tool (recommended for beginners)
- `cli_setup.py` - Command-line setup tool for advanced users
- `vscode_config.py` - Creates `.vscode/settings.json` with LaTeX Workshop configuration
- `devcontainer_config.py` - Creates `.devcontainer/devcontainer.json` for containerized development
- `docker_build.py` - Cross-platform script to build with Docker
- `docker_build.sh` - Shell script alternative for Docker builds (Unix-based systems)

These scripts work on Windows, macOS, and Linux, providing consistent experiences and redundancy across platforms.

## Backwards Compatibility

For compatibility with existing scripts or documentation, you can run:

```bash
python create_symlinks.py
```

This will create symbolic links (or script redirects on Windows) from the old file names to the new ones:

- `setup.py` → `cli_setup.py`
- `cv_setup.py` → `interactive_setup.py`
- `setup_vscode.py` → `vscode_config.py`
- `setup_devcontainer.py` → `devcontainer_config.py`
- `docker-build.sh` → `docker_build.sh`

## Sample CV

This repository includes a sample CV for demonstration purposes.

## Template Sources

You can also explore other templates:
- https://www.overleaf.com/gallery/tagged/cv

## Project Origin

This project is based on: https://github.com/reveurmichael/cv_latex

