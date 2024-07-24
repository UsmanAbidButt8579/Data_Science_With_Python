#  image saving an image writing images
import cv2 as cv
from cv2 import imwrite
from matplotlib import image

img=cv.imread("resourses/usman.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh, binary)=cv.threshold(gray,127,255,cv.THRESH_BINARY)

binary=cv.resize(binary,(100,500))

imwrite('resourses/image_gray.jpg',gray)
imwrite('resourses/image_bw.jpg',binary)

# cv.waitKey(0)
# cv.destroyAllWindows()