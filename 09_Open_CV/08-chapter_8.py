# converting video to gray or black nd white and saving

import  cv2 as cv

cap = cv.VideoCapture('resourses/sunnn.mp4')

# writing format, codec,video writer object and file output
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
out=cv.VideoWriter("resourses/Out_Video.avi",cv.VideoWriter_fourcc('M',"j",'P','G'),10,(frame_width,frame_height),isColor=False)


while(True):
    (ret,frame)=cap.read()
    grayframe=cv.cvtColor( frame,cv.COLOR_BGR2GRAY)
   
# to show in player
    if ret==True:
        out.write(grayframe)
        cv.imshow("Video",grayframe)
        # to quit with q key
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break    
cap.release()
out.release()
cv.destroyAllWindows()    