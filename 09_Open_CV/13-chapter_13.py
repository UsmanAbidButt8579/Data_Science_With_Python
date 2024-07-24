# basics functions or manipulation in open cv

import cv2 as cv
import numpy as np
from matplotlib.pyplot import gray
from numpy import mat
img=cv.imread("resourses/usman.jpg")

# resize
resized_img=cv.resize(img,(500,700))

# gray
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# blurred image
blurr_img=cv.GaussianBlur(img,(7,7),0)

# edge detection
edge_img=cv.Canny(img,53,53)

# thickness of lines
mat_kernel=np.ones((3,3),np.uint8)
dilated_img=cv.dilate(edge_img,(mat_kernel),iterations=1)
# dilated_img=cv.dilate(edge_img,(7,7),iterations=1)

# make thinner outline
ero_img=cv.erode(dilated_img,mat_kernel,iterations=1)

# cropping we will use numpy library not opencv
print("the size of our image is:",img.shape)
croped_img=img[0:500,150:400]






cv.imshow("original",img)
# cv.imshow("resized",resized_img)
# cv.imshow("gray",gray_img)
# cv.imshow("blurr",blurr_img)
# cv.imshow("Edge",edge_img)
# cv.imshow("Dilate",dilated_img)
# cv.imshow("erosion",ero_img)
cv.imshow("crroped",croped_img)
cv.waitKey(0)

cv.destroyAllWindows()