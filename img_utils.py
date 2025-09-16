from PIL import Image, ImageDraw, ImageFont
import files_utils as files
import customtkinter as ctk
from tkinter import messagebox



def open_wm_png():
    return Image.open(files.png_file).convert("RGBA")

    # ctk_png = ctk.CTkImage(wm_png)
    # label = ctk.CTkLabel(master=master, image=ctk_png, text="")
    # label.img = ctk_png
    # return label.img

def def_logo_setting():
    pass

def auto_logo_resizing(logo, img, scale_factor=0.2):
    # scale_factor = 0.2
    new_width = int(img.width * scale_factor)
    aspect_ratio = logo.height / logo.width
    new_height = int(new_width * aspect_ratio)

    return logo.resize((new_width, new_height))


def batch_test():
    if files.output_folder and files.png_file and files.input_imgs_list:
        img = Image.open(files.input_imgs_list[0])

        logo = open_wm_png()
        # logo = logo.resize((100, 100))
        logo = auto_logo_resizing(logo=logo, img=img)


        x = img.width - logo.width - 10
        y = img.height - logo.height - 10

        img.paste(logo, (x, y), logo)

        img.show()
    else:
        messagebox.showinfo("Error", "Must select all * options before Batch Test")



def img_processing():
    pass