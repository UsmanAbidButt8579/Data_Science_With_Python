# writing videos from cam

import  cv2 as cv
import  numpy as np

cap = cv.VideoCapture(0)

# writing format, codec,video writer object and file output
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
out=cv.VideoWriter("resourses/cam_Video.avi",cv.VideoWriter_fourcc('M',"j",'P','G'),20,(frame_width,frame_height),isColor=False)


while(True):
    (ret,frame)=cap.read()
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # grayframe=cv.cvtColor( frame,cv.COLOR_BGR2GRAY)
   
# to show in player
    if ret==True:
        out.write(gray_frame)
        cv.imshow("Video",gray_frame)
        # to quit with q key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break    
cap.release()
out.release()
cv.destroyAllWindows()   