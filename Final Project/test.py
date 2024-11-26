import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
 
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2) 

while True :
    success,img = cap.read()
    #Find the hand and its landmarks
    hands,img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print(sum(fingers))

        if sum(fingers) == 0:  # Rock
            print("Detected: Rock")
        elif sum(fingers) == 5:  # Paper
            print("Detected: Paper")
        elif sum(fingers) == 2:  # Scissors
            print("Detected: Scissors")
        else:
            print(sum(fingers))

    cv2.imshow("Image",img)
    cv2.waitKey(1)


