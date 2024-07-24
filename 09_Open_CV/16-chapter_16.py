# saving HD recording of cam streaming

import  cv2 as cv
import numpy as np


cap=cv.VideoCapture(0)

# resolution HD (1280 x 720)
# cap.set(3,1280)
# cap.set(4,720)

def  hd_resolution():
     cap.set(3,1280)
     cap.set(4,720)

def  sd_resolution():
     cap.set(3,640)
     cap.set(4,480)

def  fhd_resolution():
     cap.set(3,1920)
     cap.set(4,1080)     

hd_resolution()    
# sd_resolution()  
# fhd_resolution()   
    

# writing format, codec,video writer object and file output
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
out=cv.VideoWriter("resourses/cam_Video.avi",cv.VideoWriter_fourcc('M',"j",'P','G'),30,(frame_width,frame_height))


while(True):
    (ret,frame)=cap.read()
  
    # grayframe=cv.cvtColor( frame,cv.COLOR_BGR2GRAY)
   
# to show in player
    if ret==True:
        out.write(frame)
        cv.imshow("Video",frame)
        # to quit with q key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break    
cap.release()
out.release()
cv.destroyAllWindows()   
           
        