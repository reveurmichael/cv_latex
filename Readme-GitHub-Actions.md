# GitHub Actions for LaTeX CV

This guide explains how to use GitHub Actions to automatically build your LaTeX CV and create releases whenever you push changes.

## Setup

### 1. Configure GitHub Actions

The repository already includes a GitHub Actions workflow at `.github/workflows/build-cv.yml`. This workflow:

- Builds your LaTeX CV using `pdflatex`
- Creates a release branch containing only the PDF
- Generates a GitHub Release with the PDF attached

If you're using this repository as a template, the workflow should work out of the box.

### 2. Customizing the Workflow

If you need to customize the workflow, edit the `.github/workflows/build-cv.yml` file:

```yml
name: Build LaTeX CV

on:
  push:
    branches:
      - main

jobs:
  build-and-release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Set up LaTeX
        uses: xu-cheng/latex-action@v2
        with:
          root_file: main.tex

      - name: Prepare PDF for release branch
        run: |
          mkdir -p /tmp/cv_release
          cp main.pdf /tmp/cv_release/main.pdf

      - name: Create release branch with only PDF
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git checkout --orphan release
          # Remove all files and folders except .git
          find . -mindepth 1 -maxdepth 1 ! -name '.git' ! -name '.' -exec rm -rf {} +
          cp /tmp/cv_release/main.pdf .
          git add main.pdf
          git commit -m "Update CV PDF"
          git push -f origin release

      - name: Create GitHub Release
        id: create_release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: v${{ github.run_number }}
          release_name: Release v${{ github.run_number }}
          body: "Automated CV PDF build."
          draft: false
          prerelease: false

      - name: Upload Release Asset
        uses: actions/upload-release-asset@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          upload_url: ${{ steps.create_release.outputs.upload_url }}
          asset_path: ./main.pdf
          asset_name: main.pdf
          asset_content_type: application/pdf 
```

## Using GitHub Actions

1. Push your changes to the main branch
2. GitHub Actions will automatically:
   - Build your CV
   - Create a release branch with just the PDF
   - Create a new GitHub release
   - Attach the PDF to the release

## Accessing the Latest PDF

You can always access the latest PDF in two ways:

1. From the most recent GitHub Release
2. From the `release` branch of your repository

## Troubleshooting

- Check the GitHub Actions logs for any build errors
- Make sure your LaTeX file can be compiled with `pdflatex`
