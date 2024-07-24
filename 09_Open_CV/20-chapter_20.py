# split ur video into frame or image sequenceq

import cv2 as cv
import numpy as np

cap = cv.VideoCapture('resourses/sunnn.mp4')

frameNr=0

while (True):
    success,frame=cap.read()
    if success:
        cv.imwrite(f"resourses/frame_{frameNr}.jpg",frame)
    else:
        break
    frameNr=frameNr+1
cap.release()        
