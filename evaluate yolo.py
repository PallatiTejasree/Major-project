import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model (make sure the correct path is used)
model = YOLO("app_data/model/best.pt")  # Or "best.pt" if you have a trained model

# Run detection on your video
results = model.predict(source="3371152-uhd_3840_2160_30fps.mp4")

# Extract confidence scores
confidences = [det.conf for det in results[0].boxes]  # Confidence scores for all detections

# Calculate average confidence
avg_confidence = np.mean(confidences) * 100 if len(confidences) > 0 else 0

print(f"✅ Estimated YOLOv8 Confidence: {avg_confidence:.2f}%")
