import os
from tkinter import filedialog
import config


output_folder = ""
png_file = ""
input_imgs_list = []


def png_selector():
    global png_file
    png_file = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])


def final_folder():
    global output_folder
    output_folder = filedialog.askdirectory()


def img_list():
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


