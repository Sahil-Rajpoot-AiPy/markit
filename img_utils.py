import files_utils as files
from PIL import Image, ImageEnhance
from tkinter import messagebox
import os

# Placement options for watermark/logo on images
placement_opts = ["top-left", "top-center", "top-right",
           "middle-left", "center", "middle-right",
           "bottom-left", "bottom-center", "bottom-right"]

# Default logo size percentage, placement, and opacity
logo_size = 20  # Logo will be resized to 20% of image width
placement = "bottom-right"  # Default placement of logo
opacity = 100  # Default opacity (100% visible)


def open_wm_png():
    """Returns the logo/watermark image as PIL object"""

    return Image.open(files.png_file).convert("RGBA")


def auto_logo_resizing(logo, img):
    """Take Logo and Image object as arguments and resize logo according to the pic's ratio and return it.
    Can also turn take adjust the size percentage according to user's input.
    By default, resize logo to 20% size of image"""

    scale_factor = logo_size / 100
    new_width = int(img.width * scale_factor)
    aspect_ratio = logo.height / logo.width
    new_height = int(new_width * aspect_ratio)

    return logo.resize((new_width, new_height))


def auto_logo_placement(logo, img):
    """Place the logo on image according to the option user pic from drop down menu.
    By default, it will place the image to Bottom-Right"""

    padding = 10 # Padding from the edges
    place = placement

    # Determine coordinates based on placement option
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
    """Make the logo transparent according to user input.
    By default, logo is 100% visible."""

    transparency = opacity / 100

    # Extract alpha channel and scale its brightness
    alpha = logo.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(transparency)

    # Put the adjusted alpha channel back
    logo.putalpha(alpha)


def batch_test():
    """Take first image from the input folder that user selected and
        give place the logo on it on default settings if user didn't
        select custom settings and open that image after processing it in
        the default pic viewer of user's computer."""

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
    """One by one edit all image from input folder that user selected and process it by putting
        logo on in with default settings if user didn't set any and save them in output folder
        user selected one by one."""

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
