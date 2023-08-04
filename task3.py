import cv2 

img = cv2.imread('color.jpg')

img = cv2.resize(img,(640,480))
# cv2.line(img,(0,0),(640,480),(0,0,0),2)
c1 = 320
c2 = 240
cv2.line(img,(c1,c2),(c1+80,c2),(255,255,255),3)
cv2.line(img,(c1,c2),(c1,c2-60),(0,0,255),3)
cv2.line(img,(c1+80,c2),(c1,c2-60),(0,255,255),3)

cv2.imshow("image",img)

cv2.waitKey(0)