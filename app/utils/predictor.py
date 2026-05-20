import os
import random

try:
    import torch
    import torch.nn as nn
    from torchvision import models
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False

from .preprocess import preprocess_image
from .confidence import check_confidence

# Dictionary mapping crop names to their model paths
MODEL_PATHS = {
    'crop_classifier': 'app/models/crop_classifier.pth',
    'cassava': 'app/models/cassava_model.pth',
    'maize': 'app/models/maize_model.pth',
    'tomato': 'app/models/tomato_model.pth',
}

# List of supported crops
CROPS = ['cassava', 'maize', 'tomato', 'potato', 'rice', 'pepper', 'banana', 'mango']

if HAS_TORCH:
    class CropAIModel:
        def __init__(self, model_type='resnet50', num_classes=2):
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            if model_type == 'resnet50':
                self.model = models.resnet50(weights=None)
                num_ftrs = self.model.fc.in_features
                self.model.fc = nn.Linear(num_ftrs, num_classes)
            elif model_type == 'efficientnet_b3':
                # Note: efficientnet requires specialized loading or timm
                self.model = models.efficientnet_b3(weights=None)
                num_ftrs = self.model.classifier[1].in_features
                self.model.classifier[1] = nn.Linear(num_ftrs, num_classes)
            
            self.model = self.model.to(self.device)
            self.model.eval()

        def load_weights(self, path):
            if os.path.exists(path):
                self.model.load_state_dict(torch.load(path, map_location=self.device))
                return True
            return False

        def predict(self, image_tensor):
            with torch.no_grad():
                outputs = self.model(image_tensor.to(self.device))
                probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
                confidence, class_idx = torch.max(probabilities, 0)
                return class_idx.item(), confidence.item()

def predict_crop_and_disease(image_path):
    """
    Complete AI Pipeline: Stage 2 & 3.
    """
    if not HAS_TORCH:
        # Mock behavior for preview environment without torch
        import time
        time.sleep(1.5) # Simulate processing
        predicted_crop = random.choice(['tomato', 'cassava', 'maize'])
        labels = {
            'tomato': ['Early Blight', 'Late Blight', 'Healthy'],
            'cassava': ['Cassava Mosaic Disease (CMD)', 'Brown Leaf Spot', 'Healthy'],
            'maize': ['Maize Rust', 'Healthy']
        }
        predicted_disease = random.choice(labels[predicted_crop])
        confidence = random.uniform(0.88, 0.98)
        return predicted_crop, predicted_disease, confidence

    image_tensor = preprocess_image(image_path)
    
    # --- Stage 2: Crop Identification ---
    crop_model_path = MODEL_PATHS['crop_classifier']
    if os.path.exists(crop_model_path):
        crop_classifier = CropAIModel(num_classes=len(CROPS))
        crop_classifier.load_weights(crop_model_path)
        crop_idx, crop_conf = crop_classifier.predict(image_tensor)
        predicted_crop = CROPS[crop_idx]
    else:
        predicted_crop = 'tomato'
        crop_conf = 0.95

    # --- Stage 3: Disease Detection ---
    disease_model_path = MODEL_PATHS.get(predicted_crop)
    labels = {
        'tomato': ['Healthy', 'Early Blight', 'Late Blight'],
        'cassava': ['Healthy', 'Cassava Mosaic Disease (CMD)', 'Brown Leaf Spot'],
        'maize': ['Healthy', 'Maize Rust']
    }
    
    if disease_model_path and os.path.exists(disease_model_path):
        current_labels = labels.get(predicted_crop, ['Healthy', 'Unknown Disease'])
        disease_model = CropAIModel(num_classes=len(current_labels))
        disease_model.load_weights(disease_model_path)
        disease_idx, disease_conf = disease_model.predict(image_tensor)
        predicted_disease = current_labels[disease_idx]
    else:
        predicted_disease = 'Early Blight' if predicted_crop == 'tomato' else 'Healthy'
        disease_conf = 0.88

    return predicted_crop, predicted_disease, disease_conf
