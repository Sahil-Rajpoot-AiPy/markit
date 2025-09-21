# main.py
# Entry point for the MarkIt watermarking application.
# Initializes and runs the GUI workflow.

import gui

def main():
    """
    Runs the main GUI workflow:
    1. Startup window
    2. Folder selector/setup window
    3. Final window after processing
    """

    gui.startup_window() #Run startup window from gui.py
    gui.folder_selector_window() #Run folder selector window from gui.py
    gui.final_window() #Run final window from gui.py


if __name__ == "__main__":
    main()    # Initialize the main window

