import cv2
from pymongo import MongoClient
import numpy as np




def getImage(collection,object):
    # Retrieve the binary image from MongoDB
    retrieved_doc = collection.find_one({"name": object})

    # Convert binary data back to NumPy array
    if("image" in retrieved_doc.keys()):
        # image_array = cv2.imdecode(np.frombuffer(retrieved_doc["image"], np.uint8), cv2.IMREAD_COLOR)
        return retrieved_doc["image"]
        # Save the retrieved image
        # cv2.imwrite("retrieved_test.jpg", image_array)

        # print("Image retrieved and saved successfully!")
    else:
        return 0

