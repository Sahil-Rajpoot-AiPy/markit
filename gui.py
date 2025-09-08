import sys
import customtkinter as ctk
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


    def create_button(self, row, column, text, command, sticky):
        """Create button and set them in grid"""
        button = ctk.CTkButton(self, text=text, command=command)
        button.grid(row=row, column=column, padx=20, pady=(20, 20), sticky=sticky)


    def next_win_button(self):
        """Saves the current window geometry and closes the window."""
        global prev_window
        prev_window = f"{self.winfo_width()}x{self.winfo_height()}+{self.winfo_x()}+{self.winfo_y()}"
        self.destroy()



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

    app.create_button(row =2, column=0, text="Close", command=app.next_win_button, sticky="ew")
    app.mainloop()


def folder_selector_window():
    """Creates and runs the folder selector window."""
    app2 = App()
    app2.geometry(prev_window)

    def folder_selector():
        folder_path = filedialog.askdirectory()
        print(f"Selected folder: {folder_path}")

    app2.create_button(row =2, column=0, text="Select Folder", command=folder_selector, sticky="ew")

    app2.create_button(row =5, column=0, text="Close", command=app2.next_win_button, sticky="n")
    app2.mainloop()


def final_window():
    """Creates and runs the final window."""
    app3 = App()
    app3.geometry(prev_window)


    app3.create_button(row =2, column=0, text="Close", command=app3.destroy, sticky="ew")
    app3.mainloop()