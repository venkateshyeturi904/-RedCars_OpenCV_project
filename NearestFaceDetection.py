import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()

    if not ret : 
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame,1.1,4)
    
    focal_length = 0.35            # in meters
    face_width_in_real_world = 1.6 # in meters

    min_distance = float("inf")
    nearest_face = None
    w_min = float("inf")
    h_min = float("inf")

    for (x,y,w,h) in faces :
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)
        # cv2.putText(frame,str(w))
        # cv2.putText(frame, str(w), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        distance = (focal_length * face_width_in_real_world ) / (w)
        if distance < min_distance :
            nearest_face = (x,y,w,h)
            w_min = w
            h_min = h
            min_distance = distance
    if nearest_face is not None :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10)
        cv2.putText(frame, str(round(w_min*h_min,3)), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('videoScene',frame)

    key = cv2.waitKey(30)&0xff

    if(key==27):
        break
cap.release()