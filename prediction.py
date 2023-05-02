import os
import random
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
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Define the colors for the dots and text
color = (0, 255, 0) # Green
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2

# Define the folder path for the images
folder_path = "/home/pi/Pictures"

# Capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Grab the raw NumPy array representing the image
    image = frame.array

    # Increase the size of the image
    image = cv2.resize(image, (800, 600))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

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

    # If a face is detected, choose a random image file from the folder and display it
    if len(faces) > 0:
        file_list = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]
        if len(file_list) > 0:
            file_path = os.path.join(folder_path, random.choice(file_list))

            # Load the image using OpenCV
            random_image = cv2.imread(file_path)

            # Resize the image to half its size
            height, width = random_image.shape[:2]
            resized_image = cv2.resize(random_image, (width // 2, height // 2))

            # Display the resized image
            cv2.imshow("Random Image", resized_image)

        else:
            print("No .jpg files found in the specified folder path.")

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # Clear the stream for the next frame
    rawCapture.truncate(0)

    
