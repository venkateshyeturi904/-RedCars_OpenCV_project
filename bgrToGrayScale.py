import cv2

img = cv2.imread("coffee.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("window_name",img2)
cv2.waitKey(0)