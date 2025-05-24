# LaTeX CV Builder

This repository contains a LaTeX CV template with multiple build options to accommodate different user preferences and environments.

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

## Utility Scripts

This repository includes several utility scripts:

- `config_vscode_local.py` - Creates `.vscode/settings.json` with LaTeX Workshop configuration for local builds
- `config_vscode_devcontainer.py` - Creates `.devcontainer/devcontainer.json` for containerized development
- `docker_build.py` - Cross-platform script to build with Docker
- `docker_build.sh` - Shell script alternative for Docker builds (Unix-based systems)

Each configuration script can be run directly:

```bash
# Configure VSCode for local builds
python config_vscode_local.py

# Configure VSCode DevContainer
python config_vscode_devcontainer.py

# Build with Docker (Python script)
python docker_build.py

# Build with Docker (Shell script)
./docker_build.sh
```

These scripts work on Windows, macOS, and Linux, providing consistent experiences and redundancy across platforms.

## Sample CV

This repository includes a sample CV for demonstration purposes.

## Template Sources

You can also explore other templates:
- https://www.overleaf.com/gallery/tagged/cv

## Project Origin

This project is based on: https://github.com/reveurmichael/cv_latex

