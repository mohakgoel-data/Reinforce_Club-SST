import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=0.5, maxHands=1)

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

while True:
    success, img = cam.read()
    # img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    
    # if hands and hands[0]['type'] == "Left":
    #     fingers = detector.fingersUp(hands[0])
    #     totalFingers = fingers.count(1)
    #     print(type(totalFingers))

    #     cv2.putText(img, f'Fingers: {totalFingers}', (50, 50),
    #                 cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    #     if totalFingers == 5:
    #         pyautogui.keyDown('right')
    #         pyautogui.keyUp('left')
    #         pyautogui.keyUp('space')
    #     if totalFingers == 3 :
    #         pyautogui.keyUp('left')
    #         pyautogui.keyUp('right')
    #         pyautogui.keyDown('space')
    #     if totalFingers == 2:
    #         pyautogui.keyDown('left')
    #         pyautogui.keyUp('right')
    #         pyautogui.keyUp('space')
    #     if totalFingers == 0:
    #         pyautogui.keyUp('left')
    #         pyautogui.keyUp('right')
    #         pyautogui.keyUp('space')

    if hands and hands[0]['type'] == "Right":
        fingers = detector.fingersUp(hands[0])
        totalFingers = fingers.count(1)

        cv2.putText(img, f'Fingers: {totalFingers}', (50, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        if totalFingers == 5:
            pyautogui.keyDown('right')
            pyautogui.keyUp('left')
            pyautogui.keyUp('space')
        if totalFingers == 3:
            pyautogui.keyUp('left')
            pyautogui.keyUp('right')
            pyautogui.keyDown('space')
        if totalFingers == 2:
            pyautogui.keyDown('left')
            pyautogui.keyUp('right')
            pyautogui.keyUp('space')
        if totalFingers == 0:
            pyautogui.keyUp('left')
            pyautogui.keyUp('right')
            pyautogui.keyUp('space')

    cv2.imshow('Livefeed', img)
    cv2.waitKey(1)
