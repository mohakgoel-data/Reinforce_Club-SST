import cv2
import cvzone.HandTrackingModule as htm
import pyautogui as pag

vdo = cv2.VideoCapture(0)
hand_detector = htm.HandDetector(maxHands=1)

while True:
    isTrue, frame = vdo.read()
    if not isTrue:
        break

    hands, img = hand_detector.findHands(frame)

    if hands:
        hand = hands[0]
        fingers = hand_detector.fingersUp(hand)

        # Jump with all fingers
        if fingers == [1,1,1,1,1]:
            pag.press("up")
            cv2.putText(frame, "JUMP", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)

        # Slide with fist
        elif fingers == [0,0,0,0,0]:
            pag.press("down")
            cv2.putText(frame, "SLIDE", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 3)

        # Left = only index finger up
        elif fingers == [0,1,0,0,0]:
            pag.press("left")
            cv2.putText(frame, "LEFT", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)

        # Right = index + middle fingers up
        elif fingers == [0,0,0,0,1]:
            pag.press("right")
            cv2.putText(frame, "RIGHT", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)

    cv2.imshow("Subway Surfers Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

vdo.release()
cv2.destroyAllWindows()
