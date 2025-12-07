# Phase 1 Complete Setup Guide
## Receipt Expense Tracker - AAI-521 Project

---

## Table of Contents
1. [Quick Start](#quick-start)
2. [Complete Instructions](#complete-instructions)
3. [pyproject.toml Content](#pyprojecttoml-content)
4. [setup_directories.sh Content](#setup_directoriessh-content)
5. [.gitignore Content](#gitignore-content)
6. [Project Structure](#project-structure)

---

## Quick Start

### Copy and paste these commands:

```bash
# 1. Navigate to your project
cd ~/ai_projects/receipt-expense-tracker-cv

# 2. Create directories
mkdir -p data/raw/{train/{images,annotations},test/{images,annotations}} \
         data/processed \
         src tests results/{metrics,visualizations,errors} \
         docs notebooks && \
touch src/__init__.py tests/__init__.py

# 3. Install Poetry (if not installed)
curl -sSL https://install.python-poetry.org | python3 -

# 4. Create pyproject.toml (copy content below)
# Create the file and paste the pyproject.toml content

# 5. Create setup_directories.sh (copy content below)
# Create the file and paste the setup script

# 6. Make script executable
chmod +x setup_directories.sh

# 7. Install dependencies
poetry install

# 8. Activate environment
poetry shell

# 9. Download SROIE dataset
# Visit: https://rrc.cvc.uab.es/?ch=13
# Extract to: data/raw/

# 10. Start data exploration
jupyter notebook notebooks/01_data_exploration.ipynb
```

---

## Complete Instructions

### Step 1: Create Project Structure

```bash
cd ~/ai_projects/receipt-expense-tracker-cv

# Create all directories at once
mkdir -p \
  data/raw/train/{images,annotations} \
  data/raw/test/{images,annotations} \
  data/processed \
  src \
  notebooks \
  results/{metrics,visualizations,errors} \
  tests \
  docs

# Create __init__.py files
touch src/__init__.py
touch tests/__init__.py
```

### Step 2: Create pyproject.toml

Create a file named `pyproject.toml` in your project root with the content below (see pyproject.toml Content section).

### Step 3: Install Poetry

If you don't have Poetry installed:

```bash
curl -sSL https://install.python-poetry.org | python3 -

# Add to PATH
export PATH="$HOME/.local/bin:$PATH"

# Verify
poetry --version
```

### Step 4: Install Dependencies

```bash
cd ~/ai_projects/receipt-expense-tracker-cv
poetry install
```

This will create a virtual environment and install all packages (takes ~10-15 minutes due to PyTorch).

### Step 5: Activate Virtual Environment

```bash
poetry shell
```

### Step 6: Download Dataset

1. Visit: https://rrc.cvc.uab.es/?ch=13
2. Download SROIE dataset
3. Extract to: `data/raw/`

Expected structure:
```
data/raw/
├── train/
│   └── images/ (626 receipt images)
└── test/
    └── images/ (347 receipt images)
```

### Step 7: Verify Installation

```bash
# Test imports
python -c "import cv2; print('✓ OpenCV')"
python -c "import torch; print('✓ PyTorch')"
python -c "import easyocr; print('✓ EasyOCR')"

# Start Jupyter
jupyter notebook notebooks/01_data_exploration.ipynb
```

---

## pyproject.toml Content

Create a file named `pyproject.toml` and copy this content:

```toml
[tool.poetry]
name = "receipt-expense-tracker"
version = "0.1.0"
description = "Automated Expense Extraction: Receipt Parsing Using Computer Vision and OCR"
authors = ["Jagadeesh Kumar Sellappan <email@example.com>"]
readme = "README.md"
packages = [{include = "src"}]

[tool.poetry.dependencies]
python = "^3.9"
opencv-python = "^4.8.0"
easyocr = "^1.7.0"
pillow = "^10.0.0"
numpy = "^1.24.0"
pandas = "^2.0.0"
matplotlib = "^3.7.0"
seaborn = "^0.12.0"
scikit-learn = "^1.3.0"
torch = "^2.0.0"
torchvision = "^0.15.0"
regex = "^2023.10.0"
python-dateutil = "^2.8.2"
pyyaml = "^6.0"
tqdm = "^4.66.0"
jupyter = "^1.0.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
pytest-cov = "^4.1.0"
black = "^23.9.0"
flake8 = "^6.1.0"
mypy = "^1.5.0"
isort = "^5.12.0"
ipython = "^8.14.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

## setup_directories.sh Content

Create a file named `setup_directories.sh` and copy this content:

```bash
#!/bin/bash
# setup_directories.sh - Initialize project directory structure

echo "Creating project directory structure..."

# Create main directories
mkdir -p data/{raw/{train/{images,annotations},test/{images,annotations}},processed,annotations}
mkdir -p src
mkdir -p notebooks
mkdir -p results/{metrics,visualizations,errors}
mkdir -p tests
mkdir -p docs

# Create __init__.py files
touch src/__init__.py
touch tests/__init__.py

echo "Creating placeholder files..."

# Create empty placeholder Python files
touch src/preprocessing.py
touch src/ocr.py
touch src/extraction.py
touch src/evaluation.py
touch src/utils.py

echo "Project structure created successfully!"
echo ""
echo "Directory structure:"
find . -type d | head -20

echo ""
echo "Next steps:"
echo "1. poetry install"
echo "2. Download SROIE dataset to data/raw/"
echo "3. poetry shell"
echo "4. jupyter notebook notebooks/01_data_exploration.ipynb"
```

---

## .gitignore Content

Create a file named `.gitignore` and copy this content:

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Jupyter Notebook
.ipynb_checkpoints
*.ipynb

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Poetry
poetry.lock
dist/

# Data
data/raw/
data/processed/
*.zip
*.tar.gz

# Results
results/
*.pkl
*.pth
*.h5
*.pt
*.onnx

# Logs
logs/
*.log

# OS
.DS_Store
Thumbs.db

# Project specific
*.csv
*.xlsx
output/
temp/
```

---

## Project Structure

After setup, your project should look like this:

```
receipt-expense-tracker-cv/
├── pyproject.toml                    # Poetry configuration
├── .gitignore                        # Git ignore file
├── setup_directories.sh              # Setup script
├── README.md                         # Project documentation
├── data/
│   ├── raw/
│   │   ├── train/
│   │   │   └── images/              # 626 training images
│   │   └── test/
│   │       └── images/              # 347 test images
│   ├── processed/                   # Preprocessed data
│   └── annotations/
├── src/
│   ├── __init__.py
│   ├── preprocessing.py             # Image preprocessing
│   ├── ocr.py                       # OCR implementation
│   ├── extraction.py                # Information extraction
│   ├── evaluation.py                # Metrics & evaluation
│   └── utils.py                     # Helper functions
├── notebooks/
│   ├── 01_data_exploration.ipynb    # Dataset exploration
│   ├── 02_preprocessing_analysis.ipynb
│   ├── 03_ocr_testing.ipynb
│   └── 04_evaluation.ipynb
├── results/
│   ├── metrics/                     # Performance results
│   ├── visualizations/              # Output images
│   └── errors/                      # Error analysis
├── tests/
│   └── test_*.py
└── docs/
    ├── SETUP.md                     # Setup guide
    ├── METHODOLOGY.md               # Approach documentation
    └── RESULTS.md                   # Results documentation
```

---

## Important Notes

### Essential Files
- **pyproject.toml** - Do NOT modify unless adding dependencies
- **setup_directories.sh** - Run with chmod +x first
- **.gitignore** - Keep as-is for proper git configuration

### Before Running Setup
- Python 3.9 or higher installed
- Git initialized in project
- ~500MB disk space available (for dependencies + dataset)

### Common Issues

**Issue: Poetry not found**
```bash
export PATH="$HOME/.local/bin:$PATH"
```

**Issue: PyTorch installation slow**
- Normal - can take 5-10 minutes
- Only happens on first install

**Issue: Dataset not found**
```bash
# Check structure
ls data/raw/train/images/ | head -5
ls data/raw/test/images/ | head -5
```

**Issue: Import errors**
```bash
# Make sure poetry shell is activated
poetry shell
# Then test
python -c "import cv2; import torch; print('OK')"
```

---

## Quick Commands Reference

```bash
# Activate environment
poetry shell

# Add new dependency
poetry add package-name

# Update dependencies
poetry update

# Show installed packages
poetry show

# Run tests
poetry run pytest

# Format code
poetry run black src/

# Check linting
poetry run flake8 src/

# Start Jupyter
jupyter notebook

# Deactivate environment
exit
```

---

## Phase 1 Completion Checklist

- [ ] Create project directory structure
- [ ] Create pyproject.toml
- [ ] Create setup_directories.sh
- [ ] Create .gitignore
- [ ] Install Poetry
- [ ] Run poetry install
- [ ] Run poetry shell
- [ ] Download SROIE dataset
- [ ] Extract dataset to data/raw/
- [ ] Verify imports work
- [ ] Run Jupyter notebook
- [ ] Complete data exploration

Once all items are checked: **Phase 1 Complete!** 🎉

---

## Next: Phase 2

After Phase 1 is complete, proceed to Phase 2:
- Create preprocessing.py module
- Implement image preprocessing functions
- Create 02_preprocessing_analysis.ipynb
- Test preprocessing pipeline
- Document results

---

## Resources

- Poetry Docs: https://python-poetry.org/docs/
- OpenCV: https://docs.opencv.org/
- EasyOCR: https://github.com/JaidedAI/EasyOCR
- PyTorch: https://pytorch.org/
- SROIE Dataset: https://rrc.cvc.uab.es/?ch=13
- Jupyter: https://jupyter.org/

---

## Contact

- **Course**: AAI-521 Advanced AI Applications
- **University**: University of San Diego
- **Team**: Group 11
- **Lead**: Jagadeesh Kumar Sellappan
- **Project**: Receipt Expense Tracker with Computer Vision & OCR

---

## Summary

This single file contains everything you need for Phase 1:
1. Quick start commands
2. Complete step-by-step instructions
3. All configuration files (ready to copy-paste)
4. Project structure
5. Troubleshooting guide
6. Commands reference

**Follow the Quick Start section above to get started immediately!**

Good luck with your project! 🚀
