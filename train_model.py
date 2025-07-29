from ultralytics import YOLO

model = YOLO('yolov8n.pt')  


results = model.train(
    data='dataset/data.yaml',  # path to data.yaml
    epochs=50,                 # increase for better accuracy
    imgsz=640,                 # image size (default 640)
    batch=8,                   # depending on your GPU/CPU RAM
    name='pipe_detector',      # name of the run folder inside runs/
    project='runs/train',      # where to save training logs
    save=True,                 # save weights
    save_period=10,            # save every 10 epochs
    verbose=True               # log everything
)


print("Training complete. Best model saved at:")
print(model.ckpt_path if hasattr(model, 'ckpt_path') else "Check runs/train/pipe_detector/weights/")
