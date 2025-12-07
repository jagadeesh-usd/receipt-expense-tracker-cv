# Phase 1: Foundation & Setup Guide

This guide walks you through setting up your receipt expense tracker project with Poetry.

## Step 1: Verify Your Environment

### Check Python Version
```bash
python3 --version
# Should be Python 3.9 or higher
```

### Check Git
```bash
git --version
```

## Step 2: Install Poetry

If you don't have Poetry installed:

```bash
# macOS/Linux
curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH (macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"

# Verify installation
poetry --version
```

For Windows or other installation methods, see: https://python-poetry.org/docs/#installation

## Step 3: Initialize Project Structure

In your project directory (`receipt-expense-tracker-cv`):

```bash
cd ~/ai_projects/receipt-expense-tracker-cv

# Make setup script executable
chmod +x setup_directories.sh

# Run setup script
./setup_directories.sh
```

This creates:
```
receipt-expense-tracker-cv/
├── data/
│   ├── raw/
│   │   ├── train/
│   │   │   ├── images/
│   │   │   └── annotations/
│   │   └── test/
│   │       ├── images/
│   │       └── annotations/
│   ├── processed/
│   └── annotations/
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── ocr.py
│   ├── extraction.py
│   ├── evaluation.py
│   └── utils.py
├── notebooks/
├── results/
│   ├── metrics/
│   ├── visualizations/
│   └── errors/
├── tests/
├── docs/
├── pyproject.toml
├── README.md
└── .gitignore
```

## Step 4: Install Dependencies with Poetry

```bash
cd ~/ai_projects/receipt-expense-tracker-cv

# Install all dependencies from pyproject.toml
poetry install

# This creates a virtual environment and installs:
# - Core: OpenCV, EasyOCR, PyTorch, Pillow, NumPy, Pandas
# - Dev: Pytest, Black, Flake8, Jupyter, etc.
```

**Note on PyTorch**: The installation might take a few minutes. If you have issues with torch, you can modify `pyproject.toml` to use CPU-only or GPU versions.

## Step 5: Activate Poetry Virtual Environment

```bash
poetry shell
```

You should see your prompt change to indicate you're in the Poetry environment.

Alternatively, run commands with `poetry run`:
```bash
poetry run python --version
poetry run jupyter notebook
```

## Step 6: Download SROIE Dataset

1. Visit: https://rrc.cvc.uab.es/?ch=13
2. Click on **Task 4: SROIE (Scanned Receipts OCR and Information Extraction)**
3. Download the dataset (you may need to create an account)
4. Extract the downloaded file to `data/raw/`

Expected structure after extraction:
```
data/raw/
├── train/
│   └── (626 training receipt images)
└── test/
    └── (347 test receipt images)
```

### Alternative: Download via Script

If you prefer, you can create a download script:

```bash
# Create data/download_dataset.sh
cat > data/download_dataset.sh << 'EOF'
#!/bin/bash
echo "Please download SROIE dataset manually from:"
echo "https://rrc.cvc.uab.es/?ch=13"
echo ""
echo "Extract the files to:"
echo "data/raw/train/ and data/raw/test/"
EOF

chmod +x data/download_dataset.sh
```

## Step 7: Verify Installation

Test that everything is working:

```bash
# Test Python
poetry run python --version

# Test imports
poetry run python -c "import cv2; print('OpenCV:', cv2.__version__)"
poetry run python -c "import torch; print('PyTorch:', torch.__version__)"
poetry run python -c "import easyocr; print('EasyOCR imported successfully')"

# Test Jupyter
poetry run jupyter --version
```

## Step 8: Create Data Exploration Notebook

You're ready to start the first notebook! Follow these steps:

```bash
# Activate Poetry environment
poetry shell

# Start Jupyter
jupyter notebook

# Navigate to notebooks/ and create/open 01_data_exploration.ipynb
```

## Common Poetry Commands

```bash
# Add a new dependency
poetry add package-name

# Add a dev dependency
poetry add --group dev package-name

# Update dependencies
poetry update

# Show installed packages
poetry show

# Deactivate virtual environment
exit

# Run a script with Poetry
poetry run python script.py

# Run tests
poetry run pytest
```

## Troubleshooting

### Issue: PyTorch Installation Takes Too Long
**Solution**: You can use CPU-only version. Edit `pyproject.toml`:
```toml
torch = { version = "^2.0.0", markers = "platform_system != 'Darwin'" }
```

### Issue: `poetry: command not found`
**Solution**: Add Poetry to PATH:
```bash
# Add to ~/.zshrc or ~/.bash_profile
export PATH="$HOME/.local/bin:$PATH"
source ~/.zshrc  # or ~/.bash_profile
```

### Issue: Virtual Environment Issues
**Solution**: Clear and reinstall:
```bash
poetry env remove $(poetry env info -p)
poetry install
```

### Issue: CUDA/GPU Support
If you have CUDA and want GPU support:
```bash
# Modify pyproject.toml to use GPU-enabled torch
# Or manually install after Poetry setup
poetry run pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

## Next Steps

Once Phase 1 is complete:

1. ✅ Poetry environment set up
2. ✅ Project structure created
3. ✅ Dependencies installed
4. ✅ Dataset downloaded
5. 📓 Start Phase 2: **Create Data Exploration Notebook**

Move to `Phase 2: Preprocessing Pipeline`

## Useful Resources

- Poetry Docs: https://python-poetry.org/docs/
- OpenCV Docs: https://docs.opencv.org/
- EasyOCR: https://github.com/JaidedAI/EasyOCR
- PyTorch: https://pytorch.org/docs/stable/index.html
- SROIE Dataset: https://rrc.cvc.uab.es/?ch=13

---

**Need help?** Check the README.md or create an issue on GitHub.