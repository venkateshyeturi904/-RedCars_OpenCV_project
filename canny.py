import cv2 
import numpy as np

img = cv2.imread('coffee.jpg')
img = cv2.resize(img,(640,480))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(img_gray,100,505)
cv2.imshow("image",img_canny)

cv2.waitKey(0)