from flask import Flask, Response,jsonify, request
import retrieve_image as r
from flask_cors import CORS
import cv2
import base64
from pymongo import MongoClient
import numpy as np
app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["miniproject"]
collection=db["collections"]
print("success")

@app.route('/object',methods=["post"])  # Capture 'name' from the URL
def get():
    print("entered get")
    user_message = request.json.get("message", "").lower()
    response = "I didn't understand that. Please try again."
    
    if "mobile" in user_message:
        name="mobile"
    elif "spectacles" in user_message:
        name="spectacles"
    elif "bag" in user_message:
        name="bag"
    elif "laptop" in user_message:
        name="laptop"
    elif "suitcase" in user_message:
        name="suitcase"
    elif "bottle" in user_message:
        name="bottle"
    elif "human" in user_message:
        name="human"
    else:
        return jsonify({"response":response})
    img=r.getImage(collection,name)
    if(img==0):
        return jsonify({"response":"image not found"})
    else:
        image_base64 = base64.b64encode(img).decode('utf-8')
        return jsonify({"response":"image found","image":image_base64})  
    


    


if __name__ == '__main__':
    app.run(debug=True)
