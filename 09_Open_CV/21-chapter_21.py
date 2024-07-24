#  how to detect specific colors inside python
import cv2 as cv
import numpy as np


# img=cv.imread("resourses/usman.jpg")

# convert in hsc (hue,saturation,value)
# hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)

# sliders
def slider():
    pass
path="resourses/usman.jpg"

cv.namedwindow("Bars")
cv.resizewindow("Bars",900,300)

cv.createTrackbar("Hue min","Bars",0,179,slider)
cv.createTrackbar("Hue max","Bars",179,179,slider)
cv.createTrackbar("sat min","Bars",0,255,slider)
cv.createTrackbar("sat max","Bars",255,255,slider)
cv.createTrackbar("val min","Bars",0,255,slider)
cv.createTrackbar("val max","Bars",255,255,slider)

img=cv.imread(path)
hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)

# hue_min=cv.getTrackbarPos("Hue min","Bars",)
# print(hue_min)

while (True):
    img=cv.imread(path)
    hsv_img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hue_min=cv.getTrackbarPos("Hue min","Bars")
    hue_max=cv.getTrackbarPos("Hue max","Bars")
    sat_min=cv.getTrackbarPos("sat min","Bars")
    sat_max=cv.getTrackbarPos("sat max","Bars")
    val_min=cv.getTrackbarPos("val min","Bars")
    val_max=cv.getTrackbarPos("val max","Bars")
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)

    # to see these changes inside an image
    lower=np.array([hue_min,sat_min,val_min])
    upper=np.array([hue_max,sat_max,val_max])
    mask_img=cv.inRange(hsv_img,lower,upper)
    out_img=cv.bitwise_and(img,img,mask=mask_img)



    cv.imshow("first image",img)
    cv.imshow("HSV",hsv_img) 
    cv.imshow("mask",mask_img)   
    cv.imshow("final output",out_img)
    if cv.waitKey(1) & 0xFF==ord('q'):
            break
cv.waitKey(0)
cv.destroyAllWindows()    



# cv.imshow("first image",img)
# cv.imshow("HSV",hsv_img)
# cv.waitKey(0)
# cv.destroyAllWindows()