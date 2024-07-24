
# how to draw line and shape in python
import  cv2 as cv
import numpy as np

# Draw a canvas
img=np.zeros((600,600))
img1=np.ones((600,600))

# print size
print("the size of our canvas is:",img.shape)
# print(img)

# adding colors to the canvas

coloured_img=np.zeros((600,600,3),np.uint8) # color channel addition

coloured_img[:]=255,0,255 # complete colored image
coloured_img[150:230,100:207]=255,0,0 # part of image to be  color

# adding line

cv.line(coloured_img,(0,0),(coloured_img.shape[0],coloured_img.shape[1]),(255,0,0),3) # croos line
cv.line(coloured_img,(100,100),(300,300),(255,255,50),3) # part line

# adding rectangle

cv.rectangle(coloured_img,(50,100),(300,400),(255,255,255),cv.FILLED) # filled

cv.circle(coloured_img,(300,300),50,(255,10,100),5)
cv.circle(coloured_img,(300,300),50,(255,10,100),cv.FILLED)


# adding text
cv.putText(coloured_img,"python ka chilla",(200,500),cv.FONT_HERSHEY_PLAIN,1,(255,255,0),1)



# cv.imshow("black",img)
# # cv.imshow("white",img1)
cv.imshow("colored",coloured_img)
cv.waitKey(0)
cv.destroyAllWindows()