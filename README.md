# CropAI: Production-Grade Disease Detection

CropAI is an advanced agricultural diagnostic platform that uses a multi-stage AI pipeline to identify crops and detect diseases with high precision. Unlike generic classifiers, CropAI validates images and uses crop-specific models to prevent false diagnoses.

## 🚀 Key Features
- **Multi-Stage AI Pipeline**: Validation → Identification → Detection → Recommendation.
- **High Confidence Threshold**: Rejects predictions with < 85% confidence to ensure reliability.
- **Agricultural Recommendation Engine**: Provides symptoms, causes, and both organic/chemical treatments.
- **Futuristic UI**: Responsive dashboard with GSAP animations and dark mode support.
- **Production Ready**: Optimized for Render deployment with Gunicorn and Flask.

## 🏗️ Architecture
1. **Stage 1 (Validation)**: OpenCV-based quality checks + Plant/Non-plant verification.
2. **Stage 2 (Crop ID)**: Identifies the crop type (Tomato, Cassava, Maize, etc.).
3. **Stage 3 (Disease Detection)**: Loads a specialized model for the identified crop.
4. **Stage 4 (Confidence)**: Filters out uncertain predictions.
5. **Stage 5 (Recommendation)**: Fetches expert-curated treatment plans.

## 🛠️ Tech Stack
- **Backend**: Flask, PyTorch, OpenCV, torchvision, timm.
- **Frontend**: HTML5, Tailwind CSS, GSAP, Chart.js.
- **Deployment**: Render, Gunicorn.

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd crop-disease-ai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app/app.py
   ```

## 🧠 Training New Models
Training scripts are provided in the `training/` directory. 
Example for training the crop classifier:
```bash
python training/train_crop_classifier.py
```

## ☁️ Deployment on Render
This project is pre-configured for Render.
1. Connect your GitHub repository to Render.
2. Choose **Web Service**.
3. Render will automatically detect `render.yaml` and configure the environment.

## 📄 License
MIT License
