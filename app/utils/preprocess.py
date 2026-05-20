try:
    from torchvision import transforms
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False

from PIL import Image

def get_transform(img_size=224):
    if not HAS_TORCH:
        return None
    return transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

def preprocess_image(image_path, img_size=224):
    """
    Standardizes image data for Stage 2 & 3 inference.
    
    Processing Steps:
    1. Load image using PIL.
    2. Convert to RGB (removes Alpha channel if present).
    3. Resize to model's input size (default 224x224).
    4. Convert to Tensor.
    5. Normalize using ImageNet statistics (Standard for transfer learning).
    
    Advanced Production Considerations:
    - Background Cleanup: Removing noise/soil from background.
    - Leaf Isolation: Using semantic segmentation to focus only on the leaf.
    """
    if not HAS_TORCH:
        return None
    image = Image.open(image_path).convert('RGB')
    transform = get_transform(img_size)
    image_tensor = transform(image).unsqueeze(0)
    return image_tensor
