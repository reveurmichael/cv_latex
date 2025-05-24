# Local LaTeX Build with VSCode/Cursor

This guide explains how to set up and build your LaTeX CV directly on your local machine using VSCode or Cursor.

## Setup

### 1. Install LaTeX Workshop Extension

Install the **LaTeX Workshop** extension for VSCode/Cursor.

### 2. Install TexLive

Follow the installation guide: https://github.com/James-Yu/LaTeX-Workshop/wiki/Install

#### On MacOS:

```bash
brew install texlive
```

#### On Windows:
- Install TexLive 
- Install Perl 

### 3. Configure VSCode

You can either manually add the settings below to your VSCode configuration, or use our setup script:

```bash
python vscode_config.py
```

Or use the main setup scripts:

```bash
python cli_setup.py --vscode
```

```bash
python interactive_setup.py
# Then select option 1
```

#### Manual Configuration

If you prefer manual configuration, add the following to VS Code settings.json:

```json
"latex-workshop.latex.tools": [
    {
        "name": "pdflatex",
        "command": "pdflatex",
        "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOC%"
        ]
    }
],
"latex-workshop.latex.recipes": [
    {
        "name": "pdflatex",
        "tools": [
            "pdflatex"
        ]
    }
],
"latex-workshop.latex.autoBuild.run": "onSave",
"latex-workshop.view.pdf.viewer": "tab",
"latex-workshop.latex.magic.args": [
    "-synctex=1",
    "-interaction=nonstopmode",
    "-file-line-error",
    "%DOC%"
],
"latex-workshop.message.error.show": true,
"latex-workshop.message.warning.show": true
```

## Building the CV

1. Open your `.tex` file in VSCode/Cursor
2. Click the "Build LaTeX" button (green play button)
3. PDF output will be generated automatically

Or, even better, on saving the file, the PDF will be generated automatically.

## Troubleshooting

- If you encounter compilation errors, check the LaTeX Workshop output panel for details
- Make sure all required LaTeX packages are installed
- Verify your VS Code settings match the recommended configuration 