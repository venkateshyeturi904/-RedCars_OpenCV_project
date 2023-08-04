import cv2
import numpy as np
img = cv2.imread('color.jpg')
img = cv2.resize(img,(640,480))
# cv2.line(img,(0,0),(640,480),(0,0,0),2)
# cv2.line(img,(640,0),(0,480),(0,0,0),5)
# cv2.rectangle(img,(100,100),(400,400),(255,255,0),5)
# cv2.circle(img,(320,240),250,(0,255,0),5)
image = cv2.namedWindow("New window",cv2.WINDOW_NORMAL)
image = cv2.resizeWindow("image",640,200)
cv2.putText(img,"Text Print",(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(250,0,0),1)
cv2.imshow("image",image)

cv2.waitKey(0)