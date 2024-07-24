# joining the images

import cv2 as cv
import numpy as np


img=cv.imread("resourses/usman.jpg")

# stacking same image

# 1- Horizantal stack
hor_img=np.hstack((img,img))

# 2- Verticle stack

ver_img=np.vstack((img,img))





# cv.imshow("horizental img",hor_img)
cv.imshow("vertical img",ver_img)


cv.waitKey(0)
cv.destroyAllWindows()

# you can only stack the same images with same shape (width, height,color channel)
# we cannat resize the stack image(function)
# same number of channel  to use np function
(600,500,3)
# you have to define a function to stack multiples images of different size and tunes
