### Reading an image nd displaying it
#  import library
import cv2 as cv

img=cv.imread("resourses/usman.jpg")

cv.imshow("first image",img)
cv.waitKey(0)