import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

def drawHandLanmarks(image, hand_lanmarks):
    if hand_lanmarks:
        for landmarks in hand_lanmarks:
            mp_drawing.draw_landmarks(image,landmarks, mp_hands.HAND_CONECTIONS)

while True:
    success, image = cap.read()
    
    image = cv2.flip(image,1)

    result = hands.process(image)

    hand_lanmarks = result.multi_hand_landmarks

    drawHandLanmarks(image, hand_lanmarks)


    cv2.imshow("Media Controller", image)

    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()

#Traceback (most recent call last):
#File "c:\Users\DELL\Documents\Byjus\Class 121\count_fingers.py", line 25, in <module>
    #drawHandLanmarks(image, hand_lanmarks)
  #File "c:\Users\DELL\Documents\Byjus\Class 121\count_fingers.py", line 14, in drawHandLanmarks
    #mp_drawing.draw_landmarks(image,landmarks, mp_hands.HAND_CONECTIONS)
#AttributeError: module 'mediapipe.python.solutions.hands' has no attribute 'HAND_CONECTIONS'. Did you mean: 'HAND_CONNECTIONS'?
