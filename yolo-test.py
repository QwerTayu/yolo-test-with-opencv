from ultralytics import YOLO
import cv2

# モデル読み込み
model = YOLO("yolov8n.pt")

# 入力画像
# results = model('IMG_3448.JPG',save=True) 
results = model(2, show=True)
for i in enumerate(results):
    print(i)