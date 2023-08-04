import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()

    if not ret : 
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame,1.1,4)
    

    for (x,y,w,h) in faces :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)
       
    cv2.imshow('videoScene',frame)

    key = cv2.waitKey(30)&0xff

    if(key==27):
        break
cap.release()