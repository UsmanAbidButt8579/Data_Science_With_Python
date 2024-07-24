# how to capture a webcam inside python

# step-1 import libraries
import  cv2 as cv
import numpy as np

# step-2 read the frames from the camera
cap=cv.VideoCapture(0) # webcam no.1
if (cap.isOpened()==False):
    print("There is an error")
# read untill the end 
# step-3 display the cam frame by frame 
while(cap.isOpened()):
    # capture frame by frame
    ret,frame=cap.read()
    if ret==True:
        # to display frame
        cv.imshow("Frame",frame)
        # to quit with q key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break    
# step-4 release and close window easily
cap.release()
cv.destroyAllWindows()        
    