# pip install opencv-python
# pip install cvzone
# pip install pyautogui

import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import time

# Initialize hand detector
detector = HandDetector(detectionCon=0.5, maxHands=1)

# Start video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

print("Starting camera... Press 'q' to quit.")
time.sleep(2)  # Allow camera to initialize

while True:
    success, img = cap.read()

    img = cv2.flip(img, 1)  # Flip horizontally
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        totalFingers = fingers.count(1)

        # Display finger count
        cv2.putText(img, f'Fingers Up: {totalFingers}', (10, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Only flap when exactly 1 finger is up (index finger)
        if totalFingers == 1:
            pyautogui.press('space')  # Simulate spacebar press
            cv2.putText(img, "FLAP!", (200, 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            time.sleep(0.15)  # Small delay to avoid rapid flapping

    # Show the image
    cv2.imshow("Flappy Bird Controller", img)

    # Exit on pressing 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()