🏠 Home Surveillance Assistant: An AI-Based Monitoring System

An intelligent AI-powered home surveillance system that combines object detection, fall detection, and fire/smoke detection with a chatbot interface for real-time monitoring and alerts. This project enhances home safety by providing smart, automated, and affordable security using computer vision and deep learning.

📖 About

The Home Surveillance Assistant is designed to go beyond traditional CCTV systems by not just recording but also analyzing video feeds in real time. It detects objects, tracks misplaced household items, monitors elderly falls, and identifies fire or smoke hazards.

Key highlights include:

YOLOv8-based Object Detection for tracking household items (laptops, bags, suitcases, etc.)

Fall Detection using motion and inactivity analysis for elderly safety

Fire & Smoke Detection for early warnings and prevention of hazards

Chatbot Interface (Flask-based) for user queries like “Where is my laptop?” or “When was the mobile last seen?”

MongoDB Integration for metadata storage and retrieval

Email Alerts for emergencies like falls or fire detection

This project offers a cost-effective, intelligent, and interactive surveillance solution for modern homes.

🛠️ Tech Stack

Programming Language: Python 3.8+

Libraries & Frameworks: YOLOv8, OpenCV, Flask, Roboflow, SMTP

Database: MongoDB

Deployment: Google Colab / Local System

Hardware: Webcam/IP Camera, 4GB+ RAM, optional GPU for faster inference

📂 Features

✅ Real-time object detection & tracking

✅ Elderly fall detection with emergency alerts

✅ Fire and smoke detection with high accuracy

✅ Chatbot assistant for interaction and queries

✅ Email notifications during critical events

✅ MongoDB logging of objects and events

✅ Works with standard webcams or CCTV feeds

📊 Results

Object Detection (YOLOv8): Precision 86.2%, Recall 84.7%, F1-score 85.5%

Fall Detection: mAP 89.6%

Fire & Smoke Detection: Accuracy 90.3%

Response Time: ~1 second per frame, chatbot ~1.2 seconds

The system successfully demonstrated real-time performance across all modules.

⚡ System Workflow

Capture live video feed

Perform object detection (YOLOv8) and log to MongoDB

Monitor human activity for falls (motion + inactivity detection)

Detect fire/smoke using image analysis

Respond to user queries via chatbot (Flask → MongoDB)

Trigger email alerts in case of emergencies

📂 Project Structure
home-surveillance-assistant/
│── data/                  # Datasets and annotations
│── models/                # YOLOv8 trained models
│── app.py                 # Flask chatbot + backend
│── detection.py           # Object/Fire/Smoke detection
│── fall_detection.py      # Fall detection logic
│── database.py            # MongoDB connection
│── requirements.txt       # Dependencies
│── README.md              # Documentation

🚀 Future Scope

🔊 Integration of audio & thermal sensors for better accuracy

🧠 Smarter chatbot with NLP and voice recognition

📱 Mobile app for remote monitoring and notifications

🌐 IoT integration for home automation

🎥 Multi-camera support with distributed monitoring

👨‍💻 Contributors

P. Jayanth

V. Mohith Kumar

N. Sai Siva Prakash

R. Sri Lakshmi Chakra Teja

N. Mohan Purushotham Naga Sai

Under the guidance of Dr. Sadu Chiranjeevi, RGUKT-Nuzvid.

📜 License

This project is licensed under the MIT License.
