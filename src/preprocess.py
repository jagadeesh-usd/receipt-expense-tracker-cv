import cv2
import numpy as np
from pathlib import Path

# -------------------------
# Core Helpers
# -------------------------

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(path)
    return img

def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -------------------------
# Preprocessing Variants
# -------------------------

def preprocess_light(gray):
    # Small denoise
    gray = cv2.bilateralFilter(gray, 5, 50, 50)

    # Light contrast
    clahe = cv2.createCLAHE(clipLimit=1.8, tileGridSize=(8, 8))
    return clahe.apply(gray)

def preprocess_medium(gray):
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    eq = clahe.apply(gray)

    return eq

def preprocess_heavy(gray):
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    thr = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31, 5
    )
    return thr

# -------------------------
# Classification Logic
# -------------------------

def classify_receipt(gray):
    std = np.std(gray)
    mean = np.mean(gray)

    # Very faint → light processing
    if std < 30:
        return "light"

    # Mid-quality → medium processing
    if 30 <= std <= 55:
        return "medium"

    # Strong-shadow or colored → heavy
    return "heavy"

# -------------------------
# Main Preprocessing Controller
# -------------------------

def preprocess_image(path):
    img = load_image(path)
    gray = to_gray(img)

    receipt_type = classify_receipt(gray)

    if receipt_type == "light":
        return preprocess_light(gray)

    if receipt_type == "medium":
        return preprocess_medium(gray)

    return preprocess_heavy(gray)

# -------------------------
# Save Function
# -------------------------

def save_preprocessed(src, dest):
    proc = preprocess_image(src)
    Path(dest).parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(dest, proc)