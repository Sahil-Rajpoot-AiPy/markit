import sys, os

def resource_path(relative_path: str) -> str:
    """Get absolute path to resource, works for dev and PyInstaller onefile"""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Paths
ICON_PATH = resource_path("data/markit_icon.ico")
LOGO_PATH = resource_path("data/markit_logo.png")
CONFIG_FILE = resource_path("data/config.json")
HOME_IMG_PATH = resource_path("data/mark_it_start_page.png")

ALLOWED_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".bm", ".bitmap", ".tiff", ".tif")
APP_TITLE = "MarkIt"
