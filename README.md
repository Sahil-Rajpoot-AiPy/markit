# MarkIt

**Batch watermarking for businesses, creators, and photographers.**

MarkIt is a lightweight desktop application for applying a consistent logo or watermark to many images at once. It was built to make repetitive image branding faster, visual, and easier for non-technical users.

## Why MarkIt

Adding a logo manually to dozens or hundreds of images is repetitive and easy to get wrong. MarkIt turns that workflow into a few simple steps:

1. Choose a folder of images
2. Select a watermark/logo
3. Choose placement, size, and transparency
4. Preview the result
5. Process the entire batch

Processed copies are saved to an output folder you choose, so your source images can remain untouched when you use a separate destination folder.

## Key features

- Batch watermarking for multiple images
- PNG/JPG/JPEG/WEBP/BMP/TIFF support
- Nine watermark placement positions
- Adjustable watermark size
- Adjustable transparency
- Preview before bulk processing
- User-selected output folder
- Desktop GUI built for non-technical users
- Windows executable option for users without Python

## Demo

[Watch the video walkthrough on YouTube](https://youtu.be/wek7LdY5kps)

## Tech stack

- Python
- CustomTkinter
- Pillow
- PyInstaller
- pytest

## Project structure

```text
markit/
├── main.py          # Application entry point
├── gui.py           # Desktop interface
├── img_utils.py     # Image-processing logic
├── files_utils.py   # File and folder helpers
├── config.py        # Application configuration
├── test_main.py     # Automated tests
├── data/            # Icons and application assets
└── requirements.txt
```

## Run from source

### 1. Clone the repository

```bash
git clone https://github.com/Sahil-Rajpoot-AiPy/markit.git
cd markit
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run MarkIt

```bash
python main.py
```

## Using the app

1. Launch MarkIt and click **Start**.
2. Select the folder containing the images you want to process.
3. Choose a PNG watermark or logo. Transparent PNGs work best.
4. Select an output folder. For maximum safety, use a different folder from the source images.
5. Adjust watermark size, transparency, and placement.
6. Use **Batch Test** to preview the settings on one image.
7. If the result looks right, run **Bulk Processing**.

## Windows executable

A standalone Windows build can be produced with PyInstaller:

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --add-data "data;data" --icon=data\markit_icon.ico --name MarkIt main.py
```

The generated executable will be placed in the `dist` directory.

Users downloading an unsigned executable may see a Windows SmartScreen warning. Only run binaries downloaded from a source you trust.

## Tests

```bash
pip install pytest
pytest -q
```

## What this project demonstrates

MarkIt was built as a complete CS50P final project and demonstrates:

- Desktop GUI development
- Image manipulation and compositing
- File-system workflows
- Input validation and user feedback
- Separation of GUI and processing logic
- Testing
- Packaging a Python application for end users

## Future improvements

Potential next steps include:

- Drag-and-drop image selection
- More flexible positioning controls
- Saved watermark presets
- Progress reporting for large batches
- Improved cross-platform packaging
- A more polished release workflow

## License

MarkIt is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. See [LICENSE](LICENSE) for the full license text.

## Author

Created by **Saaleh Ijaz**.

For questions or feedback, open a GitHub issue or contact: [aipyfusion@gmail.com](mailto:aipyfusion@gmail.com)
