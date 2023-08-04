import cv2
import numpy as np
cap = cv2.VideoCapture('cars.mp4')

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

ret, frame1 = cap.read()
ret, frame2 = cap.read()

car_count = 0
cars = {}  # dictionary to keep track of unique cars
count_frames = 0
while cap.isOpened():
    count_frames = count_frames+1
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 15, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=4)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        # Only process contours with area greater than 2000
        if cv2.contourArea(contour) < 2000 or x+w>frame_width/2:
            continue

        # Extract region of interest (ROI) corresponding to the contour
        roi = frame1[y:y + h, x:x + w]

        # Convert ROI to HSV color space
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # Define lower and upper bounds for red color in HSV
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red = np.array([170, 50, 50])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        # Combine the masks to get the final mask
        mask = mask1 + mask2

        # Count the number of white pixels in the mask
        num_white_pixels = np.sum(mask == 255)

        # If the number of white pixels exceeds a threshold, assume it's a red car
        if num_white_pixels > 500 : # assuming 60 frames per second and each car under observation for 1 sec .
            if (w, h) not in cars and count_frames>80 and w*h>7000 and w*h<10000:  # if this car has not been detected before
                cars[(w, h)] = 1  # mark this car as detected
                car_count += 1  # increment the car count
                print(w,h,w*h)
                count_frames = 0

            # Draw bounding box around the car
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
    cv2.putText(frame1, "Red_cars: {}".format(car_count), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)
    image = cv2.resize(frame1, (1280, 720))
    cv2.imshow("Counting red cars in the left plane", image)
    
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

print("Total number of red cars detected:", car_count)

cv2.destroyAllWindows()
cap.release()
