import customtkinter as ctk
from tkinter import filedialog

prev_window = None # Global variable to store previous window geometry

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.grid_columnconfigure(0, weight=1)


    def button_callbck(self):
        print("button clicked")

    def create_button(self, row, column, text, command, sticky):
        button = ctk.CTkButton(self, text=text, command=command)
        button.grid(row=row, column=column, padx=20, pady=(20, 20), sticky=sticky)



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

    app.title("CS50P Final Project GUI")

    def button_end():
        global prev_window
        prev_window = f"{app.winfo_width()}x{app.winfo_height()}+{app.winfo_x()}+{app.winfo_y()}"
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", button_end)
    app.create_button(row =2, column=0, text="Close", command=button_end, sticky="ew")

    app.mainloop()

def folder_selector_window():
    app2 = App()
    app2.geometry(prev_window)
    app2.title("Select Folder")
    def button_end():
        global prev_window
        prev_window = f"{app2.winfo_width()}x{app2.winfo_height()}+{app2.winfo_x()}+{app2.winfo_y()}"
        app2.destroy()
    def folder_selector():
        folder_path = filedialog.askdirectory()
        print(f"Selected folder: {folder_path}")

    app2.protocol("WM_DELETE_WINDOW", button_end)
    app2.create_button(row =2, column=0, text="Select Folder", command=folder_selector, sticky="ew")
    app2.create_button(row =5, column=0, text="Close", command=button_end, sticky="n")

    app2.mainloop()

def final_window():
    app3 = App()
    app3.geometry(prev_window)
    app3.title("Process Completed")
    def button_end():
        global prev_window
        prev_window = f"{app3.winfo_width()}x{app3.winfo_height()}+{app3.winfo_x()}+{app3.winfo_y()}"
        app3.destroy()

    app3.protocol("WM_DELETE_WINDOW", button_end)
    app3.create_button(row =2, column=0, text="Close", command=button_end, sticky="ew")

    app3.mainloop()