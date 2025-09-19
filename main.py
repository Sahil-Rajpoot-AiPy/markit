import gui

import files_utils as files

def main():

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

