import os
import random

# Create a list to store image filenames
image_files = []

path = "/Users/abigailaguilar/cpsc440"

# Loop through all files in the directory
for filename in os.listdir(path):
    # Check if the file is an image file
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # If it is, add the filename to the list
        image_files.append(filename)
    
# If no image files are found, return None
if not image_files:
    print("No image files found.")
else:
    # Choose a random image from the list
    random_image_filename = random.choice(image_files)
    print(random_image_filename)
