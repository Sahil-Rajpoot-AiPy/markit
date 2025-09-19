# files_utils.py
# Utility functions for file selection and image list management in the watermarking app.

import config
from tkinter import filedialog
import os

# Global variables to store user selections
output_folder = ""      # Path to output folder for processed images
png_file = ""           # Path to selected PNG logo/watermark
input_imgs_list = []    # List of input image file path

def png_selector():
    """
    Open filemanager and help user select png file to
    use as logo/watermark and save it in the global variable.
    """

    global png_file

    png_file = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])


def final_folder():
    """
    Open filemanager to help user select the folder to save images after
    bulk processing and save that path in global variable.
    """

    global output_folder

    output_folder = filedialog.askdirectory()


def img_list():
    """
    Prompts the user to select a folder, validates supported image files,
    and stores their paths in the global input_imgs_list.
    Only continues if at least one valid image is found.
    """

    global input_imgs_list

    while True:
        folder = filedialog.askdirectory()  # Ask user to select input folder
        input_imgs_list.clear()  # Clear previous selections

        # Iterate over files in the selected folder
        for file in os.listdir(folder):
            # Check if file extension is allowed
            if file.lower().endswith(config.ALLOWED_EXTENSIONS):
                input_imgs_list.append(os.path.join(folder, file))

        # If at least one image is found, print count and exit loop
        if len(input_imgs_list) >= 1:
            print(f"{len(input_imgs_list)} images found")
            break
