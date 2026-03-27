"""
Preprocessing Module for Classical CV Segmentation Project

This module provides standardized preprocessing functions
to ensure fair comparison across all segmentation methods.
"""

import numpy as np
import cv2

def preprocess_image(image, target_size=(512, 512), apply_denoising=False):
    """
    Standardized preprocessing for all segmentation methods.
    Must be identical across all methods for fair comparison.

    Args:
        image: Input RGB image (H x W x 3)
        target_size: Target dimensions (width, height)
        apply_denoising: Whether to apply bilateral filter

    Returns:
        preprocessed: Preprocessed image ready for segmentation
    """
    # Resize to standard dimensions
    preprocessed = cv2.resize(image, target_size, interpolation=cv2.INTER_LINEAR)

    # Optional: Denoise while preserving edges
    if apply_denoising:
        preprocessed = cv2.bilateralFilter(
            preprocessed, 
            d=9, 
            sigmaColor=75, 
            sigmaSpace=75
        )

    # Normalize to [0, 255] range
    preprocessed = cv2.normalize(
        preprocessed, 
        None, 
        0, 
        255, 
        cv2.NORM_MINMAX
    ).astype(np.uint8)

    return preprocessed

def load_image_pair(img_path, mask_path):
    """
    Load image and mask pair

    Args:
        img_path: Path to image file
        mask_path: Path to mask file

    Returns:
        image: RGB image
        mask: Binary mask
    """
    # Load image (BGR -> RGB)
    image = cv2.imread(str(img_path))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Load mask (grayscale)
    mask = cv2.imread(str(mask_path), cv2.IMREAD_GRAYSCALE)

    return image, mask
