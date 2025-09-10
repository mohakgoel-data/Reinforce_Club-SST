import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
import pyautogui

cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cam.set(cv2.CAP_PROP_FPS, 30)

fdetector = FaceMeshDetector(minDetectionCon=0.4)

_key = "space"
blink_cooldown = 3
counter = 0

def is_blinking(face, threshold=0.5):
    # factor in the distance of face from camera
    face_height = faces[0][152][1] - faces[0][10][1]
    threshold = 1 - threshold
    threshold *= face_height / 320
    if face_height > 400:
        threshold *= 1.2

    # compare coordinates of certain eyelid points to detect blink
    left_blink = (face[163][1] - face[160][1] <= threshold * 20) and (face[144][1] - face[159][1] <= threshold * 24) and (face[153][1] - face[158][1] <= threshold * 24)
    right_blink = (face[380][1] - face[386][1] <= threshold * 22) and (face[374][1] - face[388][1] <= threshold * 20) and (face[373][1] - face[387][1] <= threshold * 22)

    return left_blink and right_blink

while True:
    success, frame = cam.read()

    frame = cv2.flip(frame, 1)
    frame, faces = fdetector.findFaceMesh(frame, True)

    if faces and counter > blink_cooldown:
        if is_blinking(faces[0], threshold=0.4):
            pyautogui.keyDown(_key)
            counter = 0
        else:
            pyautogui.keyUp(_key)
    # cv2.imshow("Livefeed", frame)  # Only enable if you want face display
    counter += 1

    key = cv2.waitKey(1)

    if key == ord("q"):
        break