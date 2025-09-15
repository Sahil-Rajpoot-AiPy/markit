from PIL import Image, ImageDraw, ImageFont
import files_utils as files
import customtkinter as ctk
from tkinter import messagebox



def open_wm_png(master):
    wm_png = Image.open(files.png_file).convert("RGBA")
    ctk_png = ctk.CTkImage(wm_png)
    label = ctk.CTkLabel(master=master, image=ctk_png, text="")
    label.img = ctk_png
    return label.img

def def_logo_setting():
    pass

def batch_test():
    if files.output_folder and files.png_file and files.input_imgs_list:
        print("Function is in building process")
    else:
        messagebox.showinfo("Error", "Must select all * options before Batch Test")



def img_processing():
    pass