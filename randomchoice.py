import os
import random
import cv2

folder_path = "/home/abbys/smartmirror/cpsc440"
file_list = [f for f in os.listdir(folder_path) if f.endswith(".png")]

if len(file_list) > 0:
    # Choose a random image file from the folder
    file_path = os.path.join(folder_path, random.choice(file_list))

    # Load the image using OpenCV
    image = cv2.imread(file_path)

    # Resize the image to half its size
    height, width = image.shape[:2]
    resized_image = cv2.resize(image, (width // 2, height // 2))

    # Display the resized image
    cv2.imshow("Random Image", resized_image)
    cv2.waitKey(0)

    # Clean up
    cv2.destroyAllWindows()

else:
    print("No .png files found in the specified folder path.")
