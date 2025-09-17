import config
import sys
import customtkinter as ctk
from PIL import Image
import img_utils as imgs
import files_utils as files
from tkinter import messagebox

prev_window = None # Global variable to store previous window geometry





class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("MarkIt")
        self.grid_columnconfigure(0, weight=1)
        self.protocol("WM_DELETE_WINDOW", sys.exit)
        self.attributes("-alpha", 1.0)


    def create_button(self, row, column, text, command, sticky=None, height=None, width=None, font=None):
        """Create button and set them in grid"""
        
        kwargs = {"text":text, "command":command}
        # Creating and adding dic so default parameters don't become None causing errors.
        if height is not None:
            kwargs["height"] = height
        if width is not None:
            kwargs["width"] = width
        if font is not None:
            kwargs["font"] = font

        button = ctk.CTkButton(self, **kwargs)
        button.grid(row=row, column=column, padx=20, pady=(20, 20), sticky=sticky)


    def next_win_button(self):
        """Saves the current window geometry and closes the window."""
        global prev_window
        root = self.winfo_toplevel()
        prev_window = f"{root.winfo_width()}x{root.winfo_height()}+{root.winfo_x()}+{root.winfo_y()}"
        root.destroy()

    def start_process(self):
        """If all requirements are done then Saves the current window geometry and closes the window."""
        if files.output_folder and files.png_file and files.input_imgs_list:
            self.next_win_button()
        else:
            messagebox.showinfo("Error", "Must select all * options before starting")

def center_window(window, width, height):
    """Centers a Tkinter window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x}+{y}")




def startup_window():
    """Creates and runs the startup window."""
    app = App()
    center_window(app, 600, 600) # Center the window on the screen

    # Created 3 rows and 1 column
    app.grid_rowconfigure(0, weight=4)
    app.grid_rowconfigure((0,1), weight=1)
    app.grid_columnconfigure(0, weight=1)

    # Opened image stored into the label to display in first row and column.
    img = ctk.CTkImage(light_image=Image.open(config.HOME_IMG_PATH), size=(600, 400))
    image_label = ctk.CTkLabel(app, image=img, text="")
    image_label.grid(row=0, column=0, sticky = "nsew")

    # Created Tagline in the Second row.
    tagline = ctk.CTkLabel(app, text="Bulk brand your photos. Protect your creativity.", font=("Arial", 24, "bold"))
    tagline.grid(row=1, column=0)

    # Created Button in Last row to open next Page.
    app.create_button(row=2, column=0, text="Start", font=("Arial", 16, "bold"),
                      command=app.next_win_button, height=50, width=200)

    app.mainloop()


def folder_selector_window():
    """Creates and runs the folder selector and setup's window."""
    app2 = App()
    app2.geometry(prev_window)

    # Created 5rows and 2columns grid system.
    app2.grid_rowconfigure((0,1), weight=1)
    app2.grid_rowconfigure((2,3,4), weight=2)
    app2.grid_rowconfigure((5,6), weight=1)
    app2.grid_columnconfigure((0,1), weight=1)



    # Create and placed First Row
    ctk.CTkLabel(app2, text="Images to Watermark *", font=("Arial", 20, "bold")).grid(row=0, column=0, sticky="w",padx=20)

    app2.create_button(row =0, column=1, text="Select Folder", command=files.img_list,
                       height=35, width=150, font=("Arial", 16, "bold"), sticky="e")


    # Created and placed Second Row
    ctk.CTkLabel(app2, text="Select .png to apply on all *",
                 font=("Arial", 20, "bold")).grid(row=1, column=0, sticky="w",padx=20)

    app2.create_button(row =1, column=1, text="Logo/Watermark", command=files.png_selector, height=35, width=150,
                       font=("Arial", 16, "bold"), sticky="e")


    # Created and placed Third,Fourth,Fifth Rows


    # Created and placed Third Row
    ctk.CTkLabel(app2, text="Set Transparency",
                 font=("Arial", 16, "bold")).grid(row=2, column=0, sticky="w", padx=20)


    ctk.CTkButton(app2, text="TO Build", command=files.png_selector,
                       font=("Arial", 16, "bold")).grid(row=2, column=1, sticky="ew", padx=10)

    # Created and placed Fourth Row
    ctk.CTkLabel(app2, text="Set Size",
                 font=("Arial", 16, "bold")).grid(row=3, column=0, sticky="w", padx=20)

    ctk.CTkButton(app2, text="TO Build", command=files.png_selector,
                  font=("Arial", 16, "bold")).grid(row=3, column=1, sticky="ew", padx=10)

    # Created and placed Fifth Row
    ctk.CTkLabel(app2, text="Select placement",
                 font=("Arial", 16, "bold")).grid(row=4, column=0, sticky="w", padx=20)

    ctk.CTkButton(app2, text="TO Build", command=files.png_selector,
                  font=("Arial", 16, "bold")).grid(row=4, column=1, sticky="ew", padx=10)




    

    # Created and place sixth Row
    ctk.CTkLabel(app2, text="Save Results *",
                 font=("Arial", 20, "bold")).grid(row=5, column=0, sticky="w", padx=20)

    app2.create_button(row=5, column=1, text="Select Folder", command=files.final_folder,
                       height=35, width=150, font=("Arial", 16, "bold"), sticky="e")


    # Created and placed seventh Row

    # ctk.CTkLabel(app2, text="Must setup all * options", font=("Arial", 20, "bold")).grid(row=6, column=0, sticky="w", padx= 20)

    app2.create_button(row=6, column=0, text="Batch Test", height=35, width=150, font=("Arial", 16, "bold"),
                       command=imgs.batch_test, sticky="w")


    app2.create_button(row =6, column=1, text="Start Processing", height=35, width=150, font=("Arial", 16, "bold"),
                       command=app2.start_process, sticky="e")


    app2.mainloop()


def final_window():
    """Creates and runs the final window."""
    app3 = App()
    app3.geometry(prev_window)

    app3.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)
    app3.grid_columnconfigure(0, weight=1)



    imgs.img_processing()

    ctk.CTkLabel(app3, text="Congratulation! All file have been watermarked.",
                 font=("Arial", 20, "bold")).grid(row=3, column=0, padx=20)

    app3.create_button(row =5, column=0, text="Close", command=app3.destroy)

    app3.mainloop()