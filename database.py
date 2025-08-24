from pymongo import MongoClient
from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2
from collections import defaultdict


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["miniproject"]
collection=db["collections"]
print("database connected")

#yolo model
model=YOLO("best.pt")
print("model is loaded")

#objects dictionary
obj_dict={0: 'bag', 1: 'bottle', 2: 'human', 3: 'laptop', 4: 'mobile', 5: 'spectacles', 6: 'suitcase'}


def extract_frames(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # No more frames

        if(frame_count%30==0):
            test(frame)
            print(f"frame {frame_count} is tested")
        frame_count+=1

    cap.release()





def test(img):
    results=model(img)

    #separating objects
    objects=defaultdict(list)
    for i in range(len(results[0].boxes.cls)):
        objects[int(results[0].boxes.cls[i])].append(results[0].boxes.xyxy[i])

    for cls,boxes in objects.items():
        image=img.copy()
        for box in boxes:
            x1,y1,x2,y2=box
            cv2.rectangle(image,(int(x1),int(y1)),(int(x2),int(y2)),(0,255.0),3)
        _, binary_data = cv2.imencode(".jpg", image)
        binary_image = binary_data.tobytes()

        collection.update_one({"name":obj_dict[cls]},{"$set":{"image":binary_image}})  
extract_frames("test_video.mp4")