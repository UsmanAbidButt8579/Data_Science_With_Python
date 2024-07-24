### grayscale conversion
#  import library
import cv2 as cv
from cv2 import cvtColor

img=cv.imread("resourses/usman.jpg")
img=cv.resize(img,(800,600))

# conversion
gray_img=cvtColor(img,cv.COLOR_BGR2GRAY)

# display code
cv.imshow("first image",img)
cv.imshow("Gray  image",gray_img)

# delay code
cv.waitKey(0)
cv.destroyAllWindows()