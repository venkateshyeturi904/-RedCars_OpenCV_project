import cv2
cap = cv2.VideoCapture(0)
cv2.waitKey(0)

while cap.isOpened():
    success , frame = cap.read()
    if not success : 
        break
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    

    cv2.imshow('window_name',frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break