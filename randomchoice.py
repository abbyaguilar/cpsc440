import os
import random
import cv2

folder_path = "/home/abbys/cpsc440/cpsc440"
file_list = [f for f in os.listdir(folder_path) if f.endswith(".png")]

if len(file_list) > 0:
    # Choose a random image file from the folder
    file_path = os.path.join(folder_path, random.choice(file_list))

    # Load the image using OpenCV
    image = cv2.imread(file_path)

    # Display the image
    cv2.imshow("Random Image", image)
    cv2.waitKey(0)

    # Clean up
    cv2.destroyAllWindows()

else:
    print("No .png files found in the specified folder path.")
