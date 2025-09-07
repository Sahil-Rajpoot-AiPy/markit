import customtkinter as ctk
from tkinter import filedialog


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")


    def button_callbck(self):
        print("button clicked")

    def create_button(self, text, command):
        button = ctk.CTkButton(self, text=text, command=command)
        button.pack(padx=20, pady=20)
