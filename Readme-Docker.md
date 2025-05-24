# Docker Setup for LaTeX CV Builder

This repository includes Docker configuration to build a LaTeX CV without needing to install LaTeX locally.

## Building the CV

### Using the Python script (easiest)

Run the provided Python build script:

```bash
python docker_build.py
```

Or use the main setup script:

```bash
python setup.py --docker
```

This will output the PDF to the current directory as `main.pdf`

### Using Docker Compose manually

```bash
# Build the Docker image
docker compose build

# Run the container to generate the PDF
docker compose run --rm cv-builder
```

### Using Docker directly

```bash
# Build the Docker image
docker build -t latex-cv-builder .

# Run the container to generate the PDF
docker run --rm -v $(pwd):/latex latex-cv-builder
```

## VSCode Integration with DevContainer

This repository includes scripts to configure VSCode's DevContainer extension and LaTeX Workshop.

### Setup Instructions

1. Run the setup script to create the DevContainer configuration:
   ```bash
   python setup.py --devcontainer
   ```

2. Install the "Dev Containers" extension in VSCode
3. Install the "LaTeX Workshop" extension in VSCode
4. Open this repository in VSCode
5. Click the green button in the bottom-left corner of VSCode
6. Select "Reopen in Container"

VSCode will build the Docker container and connect to it. You can then:

- Edit LaTeX files in VSCode
- Save changes to automatically build the PDF (using LaTeX Workshop)
- View the PDF preview directly in VSCode

## Customization

To modify the CV, edit the `main.tex` file and rebuild using one of the methods above.

## Troubleshooting

### Docker Issues
- Make sure Docker is installed and running
- On Windows, ensure Docker Desktop is running with WSL 2 integration
- On macOS, ensure Docker Desktop is running

### Package Issues
If you encounter any package-related errors, you may need to add additional packages to the Dockerfile. Add them to the `tlmgr install` line in the Dockerfile, then rebuild the Docker image. 