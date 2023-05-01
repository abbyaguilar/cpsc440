import os
import random

def choose_random_image(cpsc440):
    # Create a list to store image filenames
    image_files = []
    
    # Loop through all files in the directory
    for images in os.listdir(cpsc440):
        # Check if the file is an image file
        if filename.endswith(".png") or filename.endswith(".jpg"):
            # If it is, add the filename to the list
            image_files.append(cpsc440)
    
    # If no image files are found, return None
    if not image_files:
        return None
    
    # Choose a random image from the list
    random_image_filename = random.choice(image_files)
    
    # Return the full path to the random image
    return os.path.join(directory, random_image_filename)

# Choose a random image from the specified directory
random_image_path = choose_random_image("./cpsc440/")

# If an image was found, print its path
if random_image_path:
    print("Random image:", random_image_path)
else:
    print("No image files found.")
