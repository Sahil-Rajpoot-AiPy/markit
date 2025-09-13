from PIL import Image, ImageDraw, ImageFont
import gui
import files_utils as files

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

    gui.startup_window()

    gui.folder_selector_window()
    # print(f"Selected folder: {files.input_folder}")
    print(f"{len(files.input_imgs_list)} images total.")
    print(f"Files list from folder selected: {files.input_imgs_list}")
    print(f"PNG Image Path: {files.png_file}")
    print(f"Final folder to save images: {files.output_folder}")

    gui.final_window()



if __name__ == "__main__":
    main()    # Initialize the main window

