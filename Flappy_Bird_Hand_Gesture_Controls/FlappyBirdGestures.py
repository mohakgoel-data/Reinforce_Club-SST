import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard
import time

detector = HandDetector(detectionCon=0.7, maxHands=1)

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

last_jump = 0
cooldown = 0.25 

while True:
    success, frame = cam.read()
    if not success:
        break

    img = cv2.flip(frame, 1)
    hands, img = detector.findHands(img)

    if hands:
        fingers = detector.fingersUp(hands[0]) 
        totalFingers = fingers.count(1)

        cv2.putText(img, f'Fingers: {totalFingers}', (50, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        if totalFingers == 5 and (time.time() - last_jump) > cooldown:
            keyboard.press_and_release("space")
            last_jump = time.time()

    cv2.imshow("Flappy Bird Controller", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()
