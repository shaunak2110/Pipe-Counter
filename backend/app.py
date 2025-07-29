import os
import uuid
import cv2  # Annotated images Saving
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ultralytics import YOLO

# === Base Paths ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'runs', 'train', 'pipe_detector', 'weights', 'best.pt')

# === Verification of Model Path ===
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"[ERROR] Model not found at: {MODEL_PATH}")

# === Loading of YOLOv8 Custom Model ===
print(f"[INFO] Loading custom YOLOv8 model from: {MODEL_PATH}")
model = YOLO(MODEL_PATH)
print("[INFO] Model loaded successfully!")

# === Flask App Setup ===
app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'backend', 'uploads')
RESULT_FOLDER = os.path.join(BASE_DIR, 'backend', 'results')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# === Upload Route ===
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    filename = f"{uuid.uuid4().hex}.jpg"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    print(f"[INFO] Received image: {filename}")

    # Inference
    results = model(filepath)
    pipe_count = len(results[0].boxes)

    # Annotate and save image manually
    annotated_img = results[0].plot()
    result_path = os.path.join(RESULT_FOLDER, filename)
    cv2.imwrite(result_path, annotated_img)
    print(f"[INFO] Count: {pipe_count} | Annotated image saved: {result_path}")

    return jsonify({
        'count': pipe_count,
        'result_image_url': f"/results/{filename}"
    })


@app.route('/results/<filename>')
def get_result_image(filename):
    return send_from_directory(RESULT_FOLDER, filename)

# === Run Server ===
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
