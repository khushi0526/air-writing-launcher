import cv2
import mediapipe as mp
import subprocess
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Create hand tracker
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Canvas to draw air-writing
canvas = None

# To store drawing points
points = []

def launch_app(letter):
    apps = {
        'A': "calc.exe",        # Opens Calculator
        'B': "notepad.exe",     # Opens Notepad
        'C': "mspaint.exe",     # Opens Paint
    }

    if letter in apps:
        subprocess.Popen(apps[letter])
        print(f"Opened {apps[letter]}")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)

    # Initialize canvas with SAME size as camera frame
    if canvas is None:
        canvas = np.zeros_like(img)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Get index fingertip
            h, w, _ = img.shape
            x = int(handLms.landmark[8].x * w)
            y = int(handLms.landmark[8].y * h)
            points.append((x, y))

    # Draw points on canvas
    for p in points:
        cv2.circle(canvas, p, 5, (255, 255, 255), -1)

    # Merge canvas & camera
    combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    cv2.imshow("Air Writing Launcher", combined)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        # Clear canvas
        points = []
        canvas = None
        print("Canvas cleared")

    if key == ord('a'):
        launch_app('A')

    if key == ord('b'):
        launch_app('B')

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
