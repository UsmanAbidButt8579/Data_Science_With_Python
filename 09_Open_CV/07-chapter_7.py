# converting video to gray or black nd white

import  cv2 as cv

cap = cv.VideoCapture('resourses/sunnn.mp4')



# reading and playing
while(True):
    (ret,frame)=cap.read()
    grayframe=cv.cvtColor( frame,cv.COLOR_BGR2GRAY)
    (thresh, binary)=cv.threshold(grayframe,127,255,cv.THRESH_BINARY)
# to show in player
    if ret==True:
        cv.imshow("Video",binary)
        # to quit with q key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break    
cap.release()
cv.destroyAllWindows()    