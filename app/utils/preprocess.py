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
    Loads and preprocesses an image for inference.
    Includes normalization and resizing. 
    Note: For production 'background cleanup' or 'leaf isolation', 
    additional GrabCut or Mask R-CNN stages could be added here.
    """
    if not HAS_TORCH:
        return None
    image = Image.open(image_path).convert('RGB')
    transform = get_transform(img_size)
    image_tensor = transform(image).unsqueeze(0)
    return image_tensor
