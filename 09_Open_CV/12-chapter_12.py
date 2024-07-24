# setting of camera or video

import  cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

cap.set(10,100) # 10 is the key to set brightness
cap.set(3,1920) # width normal 640,480
cap.set(4,1080) # height # for HD 1920,1080
while(True):
    (ret,frame)=cap.read()
    if ret==True:
    
        cv.imshow("frame",frame)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break    

cap.release()
cv.destroyAllWindows()           