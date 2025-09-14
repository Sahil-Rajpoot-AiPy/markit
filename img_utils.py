from PIL import Image, ImageDraw, ImageFont
import files_utils as files
import customtkinter as ctk



def open_wm_png(master):
    wm_png = Image.open(files.png_file).convert("RGBA")
    ctk_png = ctk.CTkImage(wm_png)
    label = ctk.CTkLabel(master=master, image=ctk_png, text="")
    label.img = ctk_png

def open_bg(master):
    bg = Image.open(files.input_imgs_list[0])
    ctk_png = ctk.CTkImage(wm_png)
    ctk.CTkLabel(master=master, image=bg, text="")

