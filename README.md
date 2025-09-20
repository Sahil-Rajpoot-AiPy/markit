# MarkIt

MarkIt is a simple and efficient software to add watermarks or company logos to images in bulk. It provides a user-friendly GUI for selecting images, choosing a watermark, and customizing its placement, size, and transparency.

## Features
- Bulk watermarking of images
- Custom logo placement (corners, center, sides)
- Adjustable logo size and transparency
- Supports multiple image formats: PNG, JPG, JPEG, WEBP, BMP, TIFF
- Easy-to-use graphical interface

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/markit.git
   cd markit
   ```
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Linux/Mac
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python main.py
   ```
2. Follow the GUI prompts:
   - Select the folder containing images to watermark
   - Choose your PNG logo/watermark
   - Adjust transparency, size, and placement as desired
   - Select the output folder for processed images
   - Optionally, run a batch test before processing all images

## Requirements
- Python 3.8+
- See `requirements.txt` for required packages (e.g., Pillow, customtkinter)

## Folder Structure
```
markit/
├── config.py
├── files_utils.py
├── gui.py
├── img_utils.py
├── main.py
├── requirements.txt
├── README.md
├── data/
│   ├── markit_icon.ico
│   ├── markit_logo.png
│   └── mark_it_start_page.png
```

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## License
MIT License
Copyright (c) 2025 Saaleh Ijaz

Permission is hereby granted...

---

This project is licensed under the GNU General Public License v3.0 (GPLv3).

- You are free to use, modify, and share this software.
- If you distribute it (modified or not), you must also make the source code available under the same license.
- Proper credit must always be given.

See the full license text in the [LICENSE](LICENSE) file.

## Contact
For questions or support, contact [aipyfusion@gmail.com](mailto:aipyfusion@gmail.com)
