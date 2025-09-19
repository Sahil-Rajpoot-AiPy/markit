from PIL import Image, ImageEnhance
import files_utils as files
import os
import customtkinter as ctk
from tkinter import messagebox

placement_opts = ["top-left", "top-center", "top-right",
           "middle-left", "center", "middle-right",
           "bottom-left", "bottom-center", "bottom-right"]

logo_size = 20
placement = "bottom-right"
opacity = 100



def open_wm_png():

    return Image.open(files.png_file).convert("RGBA")


def auto_logo_resizing(logo, img):

    scale_factor = logo_size / 100
    new_width = int(img.width * scale_factor)
    aspect_ratio = logo.height / logo.width
    new_height = int(new_width * aspect_ratio)

    return logo.resize((new_width, new_height))


def auto_logo_placement(logo, img):

    padding = 10
    place = placement

    if place == "top-right":
        x = img.width - logo.width - padding
        y = padding

    elif place == "top-center":
        x = (img.width - logo.width) // 2
        y = padding

    elif place == "top-left":
        x = padding
        y = padding

    elif place == "middle-right":
        x = img.width - logo.width - padding
        y = (img.height - logo.height) // 2

    elif place == "center":
        x = (img.width - logo.width) // 2
        y = (img.height - logo.height) // 2

    elif place == "middle-left":
        x = padding
        y = (img.height - logo.height) // 2

    elif place == "bottom-right":
        x = img.width - logo.width - padding
        y = img.height - logo.height - padding

    elif place == "bottom-center":
        x = (img.width - logo.width) // 2
        y = img.height - logo.height - padding

    elif place == "bottom-left":
        x = padding
        y = img.height - logo.height - padding

    else:
        raise ValueError("Invalid position value")

    return x, y


def auto_logo_transparency(logo):

    transparency = opacity / 100

    # Extract alpha channel and scale its brightness
    alpha = logo.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(transparency)

    # Put the adjusted alpha channel back
    logo.putalpha(alpha)


def batch_test():

    if files.output_folder and files.png_file and files.input_imgs_list:

        img = Image.open(files.input_imgs_list[0])
        logo = open_wm_png()
        logo = auto_logo_resizing(logo=logo, img=img)
        auto_logo_transparency(logo=logo)
        x, y = auto_logo_placement(logo=logo, img=img)

        img.paste(logo, (x, y), logo)
        img.show()
    else:
        messagebox.showinfo("Error", "Must select all * options before Batch Test")


def img_processing():

    logo = open_wm_png()
    os.startfile(files.output_folder)
    auto_logo_transparency(logo=logo)

    for img in files.input_imgs_list:
        image = Image.open(img)
        logo = auto_logo_resizing(logo=logo, img=image)

        x, y = auto_logo_placement(logo=logo, img=image)

        image.paste(logo, (x, y), logo)

        filename = os.path.basename(img)
        output_path= os.path.join(files.output_folder, filename)

        image.save(output_path)
