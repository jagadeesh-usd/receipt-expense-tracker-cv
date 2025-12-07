"""
This module contains functions for preprocessing images, including loading,
converting to grayscale, denoising, enhancing contrast, deskewing, applying
adaptive thresholding, and saving the processed image.
"""

import cv2
import numpy as np
from pathlib import Path

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(path)
    return img

def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def light_preprocess(gray):
    # Light denoise
    gray = cv2.bilateralFilter(gray, 7, 75, 75)

    # Light contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)

    return gray

def heavy_preprocess(gray):
    # Stronger normalization
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adaptive threshold for shadow removal / clarity
    thr = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31, 5
    )
    return thr

def should_use_heavy(gray):
    # Compute grayscale contrast
    std = np.std(gray)
    mean = np.mean(gray)

    # Low contrast images benefit from heavy preprocessing
    if std < 35:  # empirically works well for SROIE
        return True

    # Very bright washed-out images also get heavy
    if mean > 200:
        return True

    return False

def preprocess_image(path):
    img = load_image(path)
    gray = to_gray(img)

    if should_use_heavy(gray):
        return heavy_preprocess(gray)
    else:
        return light_preprocess(gray)

def save_preprocessed(src, dest):
    proc = preprocess_image(src)
    Path(dest).parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(dest, proc)
