import os
from ultralytics import YOLO
import uuid


model = YOLO('runs/train/pipe_detector/weights/best.pt')  


RESULT_FOLDER = 'results'
os.makedirs(RESULT_FOLDER, exist_ok=True)

image_path = 'test_image.jpg'  


results = model(image_path)

pipe_count = len(results[0].boxes)

result_filename = f"{uuid.uuid4().hex}.jpg"
result_path = os.path.join(RESULT_FOLDER, result_filename)
results[0].save(save_dir=RESULT_FOLDER)

print(f"Pipes detected: {pipe_count}")
print(f"Annotated image saved to: {result_path}")
