import os
from tkinter import filedialog
import config


output_folder = ""
png_file = ""
input_imgs_list = []


def png_selector():
    """Open filemanager and help user select png file to
        use as logo/watermark and save it in the global variable."""

    global png_file

    png_file = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])


def final_folder():
    """Open filemanager to help user select the folder to save images after
        bulk processing and save that path in global variable."""

    global output_folder

    output_folder = filedialog.askdirectory()


def img_list():
    """Validate all the supported images and save them in the global variable list."""

    global input_imgs_list
    
    while True:
        folder = filedialog.askdirectory()
        input_imgs_list.clear()

        for file in os.listdir(folder):
            if file.lower().endswith(config.ALLOWED_EXTENSIONS):
                input_imgs_list.append(os.path.join(folder, file))

        if len(input_imgs_list) >= 1:
            print(f"{len(input_imgs_list)} images found")
            break


