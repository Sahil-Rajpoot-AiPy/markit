import config
import sys
import customtkinter as ctk
from PIL import Image
from tkinter import filedialog

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
    app.grid_columnconfigure(0, weight =1)

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
    """Creates and runs the folder selector window."""
    app2 = App()
    app2.geometry(prev_window)

    def folder_selector():
        folder_path = filedialog.askdirectory()
        print(f"Selected folder: {folder_path}")

    app2.create_button(row =0, column=0, text="Select Folder", command=folder_selector, sticky="ew")

    app2.create_button(row =0, column=0, text="Start Processing", command=app2.next_win_button, sticky="n")
    app2.mainloop()


def final_window():
    """Creates and runs the final window."""
    app3 = App()
    app3.geometry(prev_window)


    app3.create_button(row =2, column=0, text="Close", command=app3.destroy, sticky="ew")
    app3.mainloop()