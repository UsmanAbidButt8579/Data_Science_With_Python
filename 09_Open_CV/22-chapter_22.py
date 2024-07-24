# face detection  in images

from matplotlib.pyplot import gray
from scipy.misc import face
import cv2 as cv

face_cascade=cv.CascadeClassifier('resourses/haarcascade_frontalface_default.xml')

img=cv.imread("resourses/usman.jpg")

img=cv.resize(img,(886,591))

gray_img=cvtColor(img,cv.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,1.1,4)

# draw a rectangle

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv.imshow("first image",img)
cv.waitKey(0)
cv.destroyAllWindows()