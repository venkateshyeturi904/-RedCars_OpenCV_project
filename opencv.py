import cv2
from matplotlib import pyplot as plt
img = cv2.imread('coffee.jpg')

# print(img.shape)

# img = cv2.resize(img,(6400,480))

img = cv2.resize(img,(0,0),fx=1,fy=1)

cv2.imshow("coffee",img)
cv2.waitKey(0)

