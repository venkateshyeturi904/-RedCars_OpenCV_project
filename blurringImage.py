import cv2
import numpy as np
img = cv2.imread('color.jpg')
blur_img = cv2.GaussianBlur(img,(5,5),0)
img2 = img[100:400,200:400]
cv2.imshow("image",img2)

cv2.waitKey(0)