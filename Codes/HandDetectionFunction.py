import cv2
import mediapipe as mp
import time
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

mpHands = mp. solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
#print(volRange)
minVol = volRange[0]
maxVol = volRange[1]

def findHands(img):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLs in results.multi_hand_landmarks:
            
            mpDraw.draw_landmarks(img, handLs, mpHands.HAND_CONNECTIONS)
    return img

def findPos(img, handNo = 0):
    xList = []
    yList = []
    bbox = []
    lmList = []
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        myHand = results.multi_hand_landmarks[handNo]
        for id, lm in enumerate(myHand.landmark):
                    #print(id, lm)
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            xList.append(cx)
            yList.append(cy)
            #print(id, cx, cy)
            lmList.append([id, cx, cy])
        xmin, xmax = min(xList), max(xList)
        ymin, ymax = min(yList), max(yList)
        bbox = xmin, ymin, xmax, ymax
        cv2.rectangle(img, (bbox[0]-20, bbox[1]-20), (bbox[2]+20, bbox[3]+20), (0, 255, 0), 2)
    return lmList, bbox


def gestVol():
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0

    while True:
        success, img = cap.read()
        img = findHands(img)
        lmList, bbox = findPos(img)
        if len(lmList) != 0:
            #print(lmList[4], lmList[8])
            #print(bbox)
            area = ((bbox[2] - bbox[0]) * (bbox[3] - bbox[1])) // 100
            #print(area)
            if 650 < area < 1300:
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]
                cx, cy = (x1+x2)//2, (y1+y2)//2

                cv2.circle(img, (x1, y1), 15, (255, 0, 255,), cv2.FILLED)
                cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

                length = math.hypot(x2-x1, y2-y1)
                #print(length)

                if length < 50:
                    cv2.circle(img, (cx, cy), 15, (0, 255, 0,), cv2.FILLED)
                
                vol = np.interp(length, [50, 220], [minVol, maxVol])
                #print(length, vol)
                volume.SetMasterVolumeLevel(vol, None)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)

gestVol()