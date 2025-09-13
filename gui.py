import config
import sys
import customtkinter as ctk
from PIL import Image
# from files_utils import folder_selector, png_selector
import files_utils as files

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
    app2.grid_rowconfigure(2, weight=6)
    app2.grid_rowconfigure((3,4), weight=1)
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


    # Created and placed Third Row

    # Making a Frame inside main window, row 3, column 1/left side.
    left_frame_3 = ctk.CTkFrame(app2, bg_color="transparent")
    left_frame_3.grid(row=2, column=0, sticky="nsew")

    # Making a Frame inside main window, row 3, column 2/right side.
    right_frame_3 = ctk.CTkFrame(app2, fg_color="grey", corner_radius=25)
    right_frame_3.grid(row=2, column=1, sticky="nsew")

    # Make Grid in left_frame_3 of 3 rows and 2 columns.
    left_frame_3.grid_rowconfigure((0, 1, 2), weight=1)
    left_frame_3.grid_columnconfigure((0,1),weight=1)

    # Inside 3rd row left frame created and placed first row.
    ctk.CTkLabel(left_frame_3, text="Set Transparency",
                 font=("Arial", 16, "bold")).grid(row=0, column=0, sticky="w", padx=20)


    ctk.CTkButton(left_frame_3, text="TO Build", command=files.png_selector,
                       font=("Arial", 16, "bold")).grid(row=0, column=1, sticky="ew", padx=10)

    # Inside 3rd row left frame created and placed second row.
    ctk.CTkLabel(left_frame_3, text="Set Size",
                 font=("Arial", 16, "bold")).grid(row=1, column=0, sticky="w", padx=20)

    ctk.CTkButton(left_frame_3, text="TO Build", command=files.png_selector,
                  font=("Arial", 16, "bold")).grid(row=1, column=1, sticky="ew", padx=10)

    # Inside 3rd row left frame created and placed third row.
    ctk.CTkLabel(left_frame_3, text="Select placement",
                 font=("Arial", 16, "bold")).grid(row=2, column=0, sticky="w", padx=20)

    ctk.CTkButton(left_frame_3, text="TO Build", command=files.png_selector,
                  font=("Arial", 16, "bold")).grid(row=2, column=1, sticky="ew", padx=10)

    # Inside 3rd row right frame create and place a preview to see setting applied live.




    

    # Created and place Fourth Row
    ctk.CTkLabel(app2, text="Save Results *",
                 font=("Arial", 20, "bold")).grid(row=3, column=0, sticky="w", padx=20)

    app2.create_button(row=3, column=1, text="Select Folder", command=files.final_folder,
                       height=35, width=150, font=("Arial", 16, "bold"), sticky="e")


    # Created and placed Fifth Row
    ctk.CTkLabel(app2, text="Must setup all * options", font=("Arial", 20, "bold")).grid(row=4, column=0, sticky="w", padx= 20)

    app2.create_button(row =4, column=1, text="Start Processing", height=35, width=150, font=("Arial", 16, "bold"),
                       command=app2.next_win_button, sticky="e")
    app2.mainloop()


def final_window():
    """Creates and runs the final window."""
    app3 = App()
    app3.geometry(prev_window)


    app3.create_button(row =2, column=0, text="Close", command=app3.destroy, sticky="ew")
    app3.mainloop()