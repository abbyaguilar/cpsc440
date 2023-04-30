import os
import cv2
xml_path = 'haarcascade_frontalface_default.xml'
if os.path.isfile(xml_path):
    face_cascade = cv2.CascadeClassifier(xml_path)
else:
    print(f"Could not find XML file: {xml_path}")
