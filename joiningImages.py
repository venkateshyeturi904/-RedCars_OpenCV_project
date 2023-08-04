import cv2
import numpy as np

def stackImages(scale,imageArray):
    rows = len(imageArray)
    cols = len(imageArray[0])
    width = imageArray[0][0].shape[1]
    height = imageArray[0][1].shape[0]
    for x in range(0,rows):
        for y in range(0,cols):
            if len(imageArray[x][y].shape)==2:
                imageArray[x][y] = cv2.cvtColor(imageArray[x][y],cv2.COLOR_GRAY2BGR)
            imageArray[x][y] = cv2.resize(imageArray[x][y],(width,height))
    verticalBlank = np.zeros((height,width*cols,3),np.uint8)
    horizontalBlank = [verticalBlank]*rows

    for x in range(0,rows):
        horizontalBlank[x] = np.hstack(imageArray[x])
    
    vertical = np.vstack(horizontalBlank)
    vertical = cv2.resize(vertical,(0,0),fx=scale,fy=scale)

    return vertical

img = cv2.imread('color.jpg')
img = cv2.resize(img,(480,360))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
print(img.shape)
print(gray.shape)
imgstack = stackImages(0.2,([img,img,img],[img,img,img]))

# horizontal = np.hstack((img,gray))
# vertical = np.vstack((vertical,(0,0),None,))


# cv2.imshow("image",img)
cv2.imshow("hor-stack",imgstack)
# cv2.imshow("ver-stack",vertical)
cv2.waitKey(0)