PIPE DETECTOR - BACKEND RELEASE (STAGING VERSION)
--------------------------------------------------

![Pipe Detection](https://github.com/shaunak2110/Pipe-Counter/raw/main/WhatsApp%20Image%202025-07-27%20at%2023.04.01_f6605c88.jpg)


📦 Overview:
This release contains the **Pipe Object Detection Backend** using a **custom YOLOv8 model** trained to detect and count pipes in images. The backend provides a REST API to upload an image, process it using the trained model, and return the pipe count along with an annotated result image.

--------------------------------------------------
📚 Technical Stack:

- Language: Python 3.11
- Framework: Flask (API backend)
- Model: YOLOv8 (Trained via Ultralytics YOLOv8 library)
- Model Accuracy: ~95% precision on validation set (30 images, 1 class: 'pipe')
- Deployment: Run via Flask or Waitress (production server optional)

--------------------------------------------------

![Pipe Detection](https://github.com/shaunak2110/Pipe-Counter/blob/0255607a2a831d2e2afb75bdb89c97d92fba55b7/WhatsApp%20Image%202025-07-27%20at%2023.04.27_0d66740b.jpg)

📁 Folder Structure:

pipe_detector_release/
├── backend/                    ← Backend server code
│   ├── app.py                  ← Main Flask app with API logic
│   ├── run.py                  ← Entry point to run backend with Waitress
│   ├── requirements.txt        ← Python dependencies
│   ├── uploads/                ← Uploaded images are temporarily stored here
│   ├── results/                ← Annotated images with pipe counts
│
├── runs/
│   └── train/
│       └── pipe_detector/
│           └── weights/
│               └── best.pt     ← 🔥 Trained YOLOv8 model file
│
├── venv/                       ← Python virtual environment
└── README.txt                  ← You are here :)

--------------------------------------------------
⚙️ SETUP & USAGE (Step-by-step for Staging Server)

1. [Optional] Remove the current virtual environment (if needed)
   Command:
   > Remove-Item -Recurse -Force .\venv\

2. Create a new virtual environment
   Command:
   > python -m venv venv

3. Activate the virtual environment
   Command:
   > .\venv\Scripts\Activate.ps1       [Windows PowerShell]

4. Install all required Python dependencies
   Command:
   > pip install -r backend/requirements.txt

5. Start the backend server (runs on port 5000)
   Command:
   > python backend/run.py

   ➤ You will see:
   [INFO] Model loaded successfully!
   [INFO] Running on http://127.0.0.1:5000 and http://<server-ip>:5000

--------------------------------------------------
🔁 USING THE API - TEST INSTRUCTIONS

1. POST an Image for Pipe Detection

   URL: 
   > http://127.0.0.1:5000/upload

   Method:
   > POST (form-data)

   Key: image  |  Value: [Select an image file]

   Response:
   ```json
   {
     "count": 100,
     "result_image_url": "/results/<filename>.jpg"
   }


![Pipe Detection](https://github.com/shaunak2110/Pipe-Counter/blob/52d27d9b7b6d232506383ef3198a5318e98cfcb1/WhatsApp%20Image%202025-07-27%20at%2023.04.55_652a2f45.jpg)



APIs Accessible Through POSTMAN :-

![Pipe Detection](https://github.com/shaunak2110/Pipe-Counter/blob/ee81cd561a50e7fd7dc31706e958022cfdf590ac/WhatsApp%20Image%202025-07-29%20at%2016.24.34_886e0fb4.jpg)
![Pipe Detection](https://github.com/shaunak2110/Pipe-Counter/blob/00347b2e0ace85b90e633dc4b26d9aff4ef0eb42/WhatsApp%20Image%202025-07-29%20at%2016.25.01_4548b29d.jpg)
