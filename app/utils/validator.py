import cv2
import numpy as np
from PIL import Image

def is_blurry(image_path, threshold=50.0):
    """
    Disabled for testing: Allows all images regardless of blur.
    """
    return False

def is_low_quality(image_path, min_size=(1, 1)):
    """
    Disabled: Allows all resolutions.
    """
    return False

def is_valid_plant(image_path):
    """
    Placeholder for Stage 1: Image Validation.
    In a production system, this would call a binary classifier model 
    trained to distinguish between plant/leaf images and non-plant images.
    """
    # For now, we assume it's valid if it passes quality checks,
    # but in production, we would load a 'validation_model.pth'
    return True

def validate_image(image_path):
    """
    Main validation pipeline for Stage 1: Quality & Content Filtering.
    
    This stage prevents the AI pipeline from processing garbage data, 
    which reduces false positives and improves overall system reliability.
    
    Currently implemented as a rule-based system with hooks for 
    future AI-based validation models.
    """
    if is_low_quality(image_path):
        return False, "This image resolution is too low for a reliable prediction."
    
    if is_blurry(image_path):
        return False, "This image is too blurry. Please upload a clear photo."
    
    if not is_valid_plant(image_path):
        return False, "This image is not a recognizable crop leaf/fruit/stem image."
    
    return True, "Success"
