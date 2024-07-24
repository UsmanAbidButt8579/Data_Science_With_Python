# how to change the perspective of an image

from tkinter import W
from turtle import width
import cv2 as cv
import numpy as np


img=cv.imread("resourses/usman.jpg")
print(img.shape)
# defining points
point1=np.float32([[233,196],[82,471],[522,169],[712,482]])

width=490
height=490
# we can also write as
width,height=490,490

point2=np.float32([[0,0],[490,0],[0,height],[width,height]])


matrix=cv.getPerspectiveTransform(point1,point2)

out_img=cv.warpPerspective(img,matrix,(width,height))
cv.imwrite('resourses/warp_perspective.jpg',out_img)
 # out_img=cv.resize

# cv.imshow("original",img)
cv.imshow("transformed",out_img)
cv.waitKey(0)
cv.destroyAllWindows()