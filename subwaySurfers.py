from cvzone.FaceDetectionModule import FaceDetector
import cvzone
import cv2
import pyautogui

detector = FaceDetector(minDetectionCon=0.5, modelSelection=0)
cap = cv2.VideoCapture(0)

cap.set(3, 320) 
cap.set(4, 230)  

frame_center_x = cap.get(3) // 2
frame_center_y = cap.get(4) // 2

last_direction = None 

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1) 

    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:

        for bbox in bboxs:
            center = bbox["center"]
            x, y, w, h = bbox['bbox']
            score = int(bbox['score'][0] * 100)

            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

            if center[0] < frame_center_x - 20:
                cvzone.putTextRect(img, "Looking Left", (x, y - 30))
                direction = "Left"
            elif center[0] > frame_center_x + 30:
                cvzone.putTextRect(img, "Looking Right", (x, y - 30))
                direction = "Right"
            elif center[1] < frame_center_y - 25:
                cvzone.putTextRect(img, "Looking Up", (x, y - 30))
                direction = "Up"
            elif center[1] > frame_center_y + 25:
                cvzone.putTextRect(img, "Looking Down", (x, y - 30))
                direction = "Down"
            else:
                cvzone.putTextRect(img, "Looking Forward", (x, y - 30))
                direction = "Forward"

            if direction != last_direction:
                if direction == "Left":
                    pyautogui.press('left')
                elif direction == "Right":
                    pyautogui.press('right')
                elif direction == "Up":
                    pyautogui.press('up')
                elif direction == "Down":
                    pyautogui.press('down')

                last_direction = direction

    cv2.imshow("Image", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        print("Exiting...")
        break
