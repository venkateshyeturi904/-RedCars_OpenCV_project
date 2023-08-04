import cv2
import numpy as np
def empty(a):
    pass
img = cv2.imread('color.jpg')
img = cv2.resize(img,(360,200))
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",450,290)
cv2.createTrackbar("h_min","Trackbars",0,179,empty)
cv2.createTrackbar("h_max","Trackbars",179,179,empty)
cv2.createTrackbar("s_min","Trackbars",0,255,empty)
cv2.createTrackbar("s_max","Trackbars",255,255,empty)
cv2.createTrackbar("v_min","Trackbars",0,255,empty)
cv2.createTrackbar("v_max","Trackbars",255,255,empty)
cv2.imshow("hsv_image",img_hsv)
cv2.imshow("image",img)

while True :
    hue_min = cv2.getTrackbarPos("h_min","Trackbars")
    hue_max = cv2.getTrackbarPos("h_max","Trackbars")
    sat_min = cv2.getTrackbarPos("s_min","Trackbars")
    sat_max = cv2.getTrackbarPos("s_max","Trackbars")
    val_min = cv2.getTrackbarPos("v_min","Trackbars")
    val_max = cv2.getTrackbarPos("v_max","Trackbars")

    lower = np.array([hue_min,sat_min,val_min])
    upper = np.array([hue_max,sat_max,val_max])
    # create a mask of which we want to observe and omit rest of all
    mask = cv2.inRange(img_hsv,lower,upper)

    result = cv2.bitwise_and(img,img,mask = mask)
    cv2.imshow("result",result)
    cv2.imshow("mask",mask)
    cv2.waitKey(1)

    

cv2.waitKey(0)