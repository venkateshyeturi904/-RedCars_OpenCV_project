import cv2
cap = cv2.VideoCapture('video.mp4')
cv2.waitKey(0)

while cap.isOpened():
    success , frame = cap.read()
    if not success : 
        break
    cv2.imshow('window_name',frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break