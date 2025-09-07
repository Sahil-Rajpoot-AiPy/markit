from PIL import Image, ImageDraw, ImageFont
from gui import App

def main():

    pass
    # This is the main function to run the project.
    # First Learn GUI with Tkinter.
    # Maybe design a structure with Canva or maybe other more effective free website available for it.
    # Make the logical structure and decide which functions to add.
    # Draw programs logic and structure on paper or tool.
    # Make prtotypes of those functions and classes with notes.
    # Finally make full sudo code design of the program.
    # Make the final code.
    # Make unit tests accordingly.
    # Make the documentation for it and comments too.
    # Test it and Submit it as Final Project of CS50P.

    app = App()

    def button_working():
        print("Button is working!")
    app.create_button(text="Working?", command=button_working)

    def button_new():
        print("New Button is working!")
    app.create_button(text="New button?", command=button_new)






    app.mainloop()


if __name__ == "__main__":
    main()    # Initialize the main window

