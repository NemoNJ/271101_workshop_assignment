#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h) #lm คือตำแหน่ง
                if id == 20:
                    id20 = int(id)
                    cx20 = cy
                if id == 18:
                    id18 = int(id)
                    cx18 = cy
                if id == 16:
                    id16 = int(id)
                    cx16 = cy
                if id == 14:
                    id14 = int(id)
                    cx14 = cy
                if id == 12:
                    id12 = int(id)
                    cx12 = cy
                if id == 10:
                    id10 = int(id)
                    cx10 = cy
                if id == 8:
                    id8 = int(id)
                    cx8 = cy
                if id == 6:
                    id6 = int(id)
                    cx6 = cy
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
            
            finger = ["THUMB", "Index finger","Middle finger","Ring finger","Pinky Finger"]   
            if cx20 < cx18 :
                cv2.putText(img, str(finger[4]),(10, 250), cv2.FONT_HERSHEY_PLAIN, 2,
                (135, 206, 250), 3)
            if cx16 < cx14:
                cv2.putText(img, str(finger[3]),(10, 300 ), cv2.FONT_HERSHEY_PLAIN,2,
                (135, 206, 250), 3)
            if cx12 < cx10 :
                cv2.putText(img, str(finger[2]),(10, 350), cv2.FONT_HERSHEY_PLAIN, 2,
                (135, 206, 250), 3)
            if cx8 < cx6 :
                cv2.putText(img, str(finger[1]),(10, 400), cv2.FONT_HERSHEY_PLAIN, 2,
                (135, 206, 250), 3)
            if cx4 > cx3:
                cv2.putText(img, str(finger[0]),(10, 450), cv2.FONT_HERSHEY_PLAIN, 2,
                (135, 206, 250), 3)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()