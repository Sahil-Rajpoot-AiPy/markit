from PIL import Image, ImageDraw, ImageFont
import files_utils as files
import os
import customtkinter as ctk
from tkinter import messagebox



def open_wm_png():
    return Image.open(files.png_file).convert("RGBA")


def def_logo_setting():
    pass

def auto_logo_resizing(logo, img, scale_factor=0.2):

    new_width = int(img.width * scale_factor)
    aspect_ratio = logo.height / logo.width
    new_height = int(new_width * aspect_ratio)

    return logo.resize((new_width, new_height))


def batch_test():
    if files.output_folder and files.png_file and files.input_imgs_list:
        img = Image.open(files.input_imgs_list[0])

        logo = open_wm_png()

        logo = auto_logo_resizing(logo=logo, img=img)


        x = img.width - logo.width - 10
        y = img.height - logo.height - 10

        img.paste(logo, (x, y), logo)

        img.show()
    else:
        messagebox.showinfo("Error", "Must select all * options before Batch Test")



def img_processing():

    logo = open_wm_png()
    os.startfile(files.output_folder)

    for img in files.input_imgs_list:
        image = Image.open(img)
        logo = auto_logo_resizing(logo=logo, img=image)

        x = image.width - logo.width - 10
        y = image.height - logo.height - 10

        image.paste(logo, (x, y), logo)

        filename = os.path.basename(img)
        output_path= os.path.join(files.output_folder, filename)

        image.save(output_path)
