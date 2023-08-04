import cv2
img = cv2.imread('color.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,150,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img,contours,-1,(0,255,0),2)
print("number of contours :",len(contours))
cv2.imshow('contours',img)

cv2.waitKey(0)