#!/usr/bin/env python3
import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=0.8, maxHands=2) #detection confidence and max hands



cam = cv2.VideoCapture(0) # fallback to default webcam if phone camera is not found

#cam = cv2.VideoCapture(0) #this is for the first webcam selection

cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
cam.set(10, 200) # set brightness

while True:
    success, img = cam.read() #read the image from the webcam
    img = cv2.flip(img, 1) #flip the image horizontally(1 means horizontally, 0 means vertically)
    hands, img = detector.findHands(img) #find the hands in the image and return the hand object and the image
    
    if hands:
        hand = hands[0]
        if hand['type'] == "Right": #if there is a hand and it is the right hand
            fingers = detector.fingersUp(hand) #get the fingers that are up
            print(fingers) #for debugging
            cv2.putText(img, f'Fingers: {fingers.count(1)}',(50,50),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2) #put the text on the image showing the fingers that are up
            
            if fingers == [1, 1, 1, 1, 1]: #if all fingers are up
                pyautogui.keyDown('right') #press the right arrow key
                pyautogui.keyUp('left') #release the left arrow key
            if fingers == [0, 0, 0, 0, 0]: #if no fingers are up
                pyautogui.keyDown('left') #press the left arrow key
                pyautogui.keyUp('right') #release the right arrow key

    cv2.imshow("Webcam", img) #show the image in a window named Webcam
    
    if cv2.waitKey(1) & 0xFF == ord('q'): #wait for 1 millisecond before moving to the next frame, and quit if 'q' is pressed
        break

cam.release()
cv2.destroyAllWindows()