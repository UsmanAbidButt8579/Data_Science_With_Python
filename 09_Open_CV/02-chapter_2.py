### Resizing
#  import library
import cv2 as cv

img=cv.imread("resourses/usman.jpg")
img1=cv.resize(img,(800,600))

cv.imshow("first image",img)
cv.imshow("second image",img1)
cv.waitKey(0)
cv.destroyAllWindows()