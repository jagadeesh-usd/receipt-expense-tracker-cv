"""
image_processing_module.py

This module contains functions for preprocessing images, including loading,
converting to grayscale, denoising, enhancing contrast, deskewing, applying
adaptive thresholding, and saving the processed image.
"""

import cv2   
import numpy as np   
from pathlib import Path   

def load_image(path: str):
    """Load image from file."""
    img = cv2.imread(path) 
    if img is None:
        raise FileNotFoundError(f"Could not load image: {path}")   
    return img  

def to_gray(img):
    """Convert to grayscale."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   

def denoise(img):
    """Denoise using Non-local Means."""
    return cv2.fastNlMeansDenoising(img, None, 10, 7, 21)   

def enhance_contrast(img_gray):
    """Improve contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)."""
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))   
    return clahe.apply(img_gray)   

def deskew(img_gray):
    """Auto-deskew receipt image."""
    coords = np.column_stack(np.where(img_gray > 0))  
    angle = cv2.minAreaRect(coords)[-1]   
    
    # Correct the angle based on the calculated value
    if angle < -45:
        angle = -(90 + angle)   
    else:
        angle = -angle

    # Get the height and width of the image
    (h, w) = img_gray.shape  
    # Compute the rotation matrix
    M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)  
    return cv2.warpAffine(img_gray, M, (w, h), 
                          flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)  # Rotate the image

def threshold(img_gray):
    """Adaptive threshold for clean text."""
    return cv2.adaptiveThreshold(
        img_gray, 255,   
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # Gaussian mean for adaptive thresholding
        cv2.THRESH_BINARY,  # Apply binary thresholding
        11, 2  # Block size and constant subtracted from mean
    )

def preprocess_image(path):
    """Full preprocessing pipeline."""
    img = load_image(path)   
    
    # Convert the image to grayscale
    gray = to_gray(img)  
    # Denoise the grayscale image
    den = denoise(gray)  
    # Deskew the denoised image
    desk = deskew(den)  
    # Enhance the contrast of the deskewed image
    contrast = enhance_contrast(desk)  
    # Apply thresholding to get a binary image
    thresh = threshold(contrast)  
    return thresh  

def save_preprocessed(src_path, dest_path):
    """Save processed image."""
    p = preprocess_image(src_path)   
    Path(dest_path).parent.mkdir(parents=True, exist_ok=True)   
    cv2.imwrite(dest_path, p)  
