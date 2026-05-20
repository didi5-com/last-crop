import os
from flask import Blueprint, render_template, request, jsonify, current_app, session, redirect, url_for
from werkzeug.utils import secure_filename
from app.utils.validator import validate_image
from app.utils.predictor import predict_crop_and_disease
from app.utils.confidence import check_confidence
from app.utils.treatments import get_treatment_plan

main_bp = Blueprint('main', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)
        
        is_valid, message = validate_image(upload_path)
        if not is_valid:
            return jsonify({'error': message}), 400
        
        try:
            crop, disease, confidence = predict_crop_and_disease(upload_path)
            
            is_confident, conf_message = check_confidence(confidence)
            if not is_confident:
                return jsonify({
                    'error': conf_message,
                    'crop': crop,
                    'confidence': round(confidence * 100, 2)
                }), 400
            
            treatment_plan = get_treatment_plan(crop, disease)
            
            # Store result in session for the result page
            session['last_result'] = {
                'crop': crop,
                'disease': disease,
                'confidence': round(confidence * 100, 2),
                'treatment': treatment_plan,
                'image_url': f'/static/uploads/{filename}'
            }
            
            return jsonify({'success': True, 'redirect': url_for('main.result')})
            
        except Exception as e:
            return jsonify({'error': f'Prediction failed: {str(e)}'}), 500
            
    return jsonify({'error': 'Invalid file type'}), 400

@main_bp.route('/result')
def result():
    result_data = session.get('last_result')
    if not result_data:
        return redirect(url_for('main.index'))
    return render_template('result.html', **result_data)

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
