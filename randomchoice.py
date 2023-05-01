import cv2
import os

def load_images_from_folder(cpsc440):
    images = []
    for filename in os.listdir(cpscc440):
        img = cv2.imread(os.path.join(cpsc440,filename))
        if img is not None:
            images.append(img)
    return images
