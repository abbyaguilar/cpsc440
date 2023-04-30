import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

# Initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Allow the camera to warmup
time.sleep(0.1)

# Load the face detection classifier
face_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

# Define the colors for the dots
color = (0, 255, 0) # Green

# Capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    # Grab the raw NumPy array representing the image
    image = frame.array

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw dots on the faces
    for (x, y, w, h) in faces:
        dot1 = (x + w//4, y + h//4)
        dot2 = (x + 3*w//4, y + h//4)
        dot3 = (x + w//2, y + h//2)
        dot4 = (x + w//4, y + 3*h//4)
        dot5 = (x + 3*w//4, y + 3*h//4)
        cv2.circle(image, dot1, 2, color, -1)
        cv2.circle(image, dot2, 2, color, -1)
        cv2.circle(image, dot3, 2, color, -1)
        cv2.circle(image, dot4, 2, color, -1)
        cv2.circle(image, dot5, 2, color, -1)

    # Display the resulting image
    cv2.imshow("Faces", image)
    key = cv2.waitKey(1) & 0xFF

    # Clear the stream for the next frame
    rawCapture.truncate(0)

    # If the 'q' key was pressed, break from the loop
    if key == ord("q"):
        break

# Cleanup
cv2.destroyAllWindows()
