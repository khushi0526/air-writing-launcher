# ✨ Air Writing Launcher

Air Writing Launcher is a computer-vision project that allows users to write letters in the air using hand movements.  
The webcam tracks the hand landmarks using **MediaPipe** and draws the trajectory in real-time.

## 🚀 Features
- Real-time hand tracking  
- Displays dots & lines for all 21 hand landmarks  
- Tracks index finger to draw in the air  
- Clears drawing automatically when hand is lowered  
- Lightweight and works on any webcam  

## 🗂 Project Structure
air-writing-launcher/
 camera_test.py # Test your webcam
 hand_tracking.py # Shows hand landmarks (dots + lines)
 air_write_launcher.py # Main air-writing application
README.md # Project documentation

## 🛠 Requirements

Install Python packages:

pip install opencv-python mediapipe numpy

## ▶️ How to Run

### 1️⃣ Test Camera

python camera_test.py

### 2️⃣ See Hand Dots + Lines (Landmarks)

python hand_tracking.py

### 3️⃣ Run Air Writing

python air_write_launcher.py

## 🎥 Demo (Recommended)
You can later add:
- screenshots  
- demo video  
- GIF of your hand writing  

## 👩‍💻 Developer
**Khushi B S**  
Final Year — ECE  
India  

## ⭐ Support
If you like this project, star the repo on GitHub!