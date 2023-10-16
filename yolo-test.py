from ultralytics import YOLO
import cv2

# モデル読み込み
model = YOLO("yolov8n.pt")

# 入力画像
results = model('bus.jpg',save=True) 
