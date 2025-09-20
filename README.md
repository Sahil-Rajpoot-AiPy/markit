# MarkIt

Contact & support: [aipyfusion@gmail.com](mailto:aipyfusion@gmail.com)

MarkIt is a lightweight desktop application that helps you add a consistent watermark or brand logo to many photos at once. It's built for small businesses, content creators, and photographers who need a fast, visual, and predictable way to protect or brand images in bulk without manually editing each file. MarkIt focuses on:

- simplicity: a straight-forward GUI for choosing images, a logo, and settings
- control: pick placement, size, and transparency of the watermark
- safety: the original images are not overwritten; processed copies are saved to a folder you choose

What MarkIt does (short)
- Input: a folder of images (PNG/JPG/WEBP/BMP/TIFF)
- Watermark: a PNG logo (transparent PNGs recommended)
- Output: processed copies saved to a folder you choose
- Controls: placement (corners/center/sides), scale, and transparency; plus a preview before bulk processing

---

This README targets two audiences:

1) Non-technical users — download a ready-to-run ZIP and run the `.exe` (fast start)
2) Developers / Contributors — fork, run from source, or build releases

Both sets of instructions are below; non-technical guidance is first for convenience.

---

## Quick facts
- Supported image formats: PNG, JPG, JPEG, WEBP, BMP, TIFF
- Platform: 
  - Windows desktop app for non-technical users.
  - Runs on any system with Python 3.8+ for technical users.

## Features
- Bulk watermarking of images
- Custom logo placement (corners, center, sides)
- Adjustable logo size and transparency
- Preview before applying
- Save processed images to a chosen output folder

---

## Video tutorial & Step-by-step GUI guide

### **Video tutorial**

[Click here](https://youtube.com) for full video walkthrough — Recommended to watch video for 
    both non-technical and technical users can quickly understand the workflow.

### **Step-by-step GUI guide with Screenshots:**
1. Welcome: When you run the application, a welcome window appears. Click the **Start** button to begin.
2. Settings: A new window opens with settings. Titles marked with \* are **required**:
   - \*Select source folder: Choose the folder containing images you want to watermark.
   - \*Select watermark/logo: Pick a PNG file to use as your watermark or logo.
   - \*Select output folder: Choose where processed images will be saved. **Do not use the same folder as your originals, or they will be overwritten.**
3. Optional settings (default values provided, can be changed):
   - Logo size (relative to each image)
   - Logo transparency
   - Logo placement
4. Batch test: Click **Batch Test** to process the first image with your settings. The result opens in your default image viewer.
5. Bulk processing: If you like the test result, click **Bulk Processing**. The app saves all processed images to your chosen output folder.
6. Completion: After processing, a congratulatory window appears.

---

## For non-technical users — download, what to expect, and how to run the MarkIt.exe
This section explains exactly what you will get from a GitHub Release ZIP and how to handle common first-run issues.

### What the ZIP contains
- `MarkIt.exe` — a single executable you can run (no Python installation required)
- `README.md` — this file
- `LICENSE` — the project license

### System requirements and size expectations
- Windows 10/11 (64-bit recommended)
- The executable is standalone but may require the Microsoft Visual C++ Redistributable (2015-2022) on some machines.
- Typical download size: depends on build, but expect under ~50 MB for a onefile PyInstaller build.

### How to download and run
1. Open the Releases page: https://github.com/Sahil-Rajpoot-AiPy/markit/releases
2. Download the latest release ZIP (e.g., `MarkIt-x.y.z-win.zip`).
3. Extract the ZIP: Right-click → "Extract All..." or use File Explorer to copy the folder to somewhere convenient (e.g., `C:\Users\<you>\Downloads\MarkIt`).
4. Double-click `MarkIt.exe` to run.

### First-run Windows warnings and Defender guidance
- Windows SmartScreen or Defender may show a warning for unsigned apps. If you downloaded the file from this repository and trust it:
  - "Windows protected your PC" → click "More info" → "Run anyway".
- Unblock the file: right-click `MarkIt.exe` → Properties → check "Unblock" if present → Apply.
- If Defender quarantines the file, restore it and create an exclusion in Windows Security → Virus & threat protection → Manage settings → Exclusions. (Only do this for binaries you trust.)

### If the app doesn't start — quick checks
- Make sure you extracted the ZIP before running (don't run from inside the compressed archive).
- Install the Visual C++ Redistributable (2015-2022) from Microsoft if there's a missing DLL error.
- Try right-click → Run as administrator once to see if permissions were the issue.

### Common problems and how to resolve them
- SmartScreen / Defender warnings: use "More info" → "Run anyway" or unblock via Properties.
- Antivirus false positive: upload the `.exe` to VirusTotal; if it's a false positive, file a report with the vendor and restore/white-list locally.
- App crashes immediately: extract before running; check Event Viewer → Windows Logs → Application for error details.
- GUI freezes on processing certain files: try a small sample set to isolate problematic files. Re-save problem images (e.g., re-export from an editor) and try again.
- Corrupted download: delete the ZIP, re-download from Releases and extract again.

### Need help? Support & contact (non-technical users)
- Open an issue on GitHub: https://github.com/Sahil-Rajpoot-AiPy/markit/issues
- Or email: [aipyfusion@gmail.com](mailto:aipyfusion@gmail.com) — include OS version, the exact steps you took, and any error text or screenshots.

---

## For developers / contributors — clone, run, test, and package
This section explains how to run and tinker with the project from source.

### Clone and run (Windows examples)

```cmd
git https://github.com/Sahil-Rajpoot-AiPy/markit.git
cd markit
```

### Create and activate a virtual environment

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### Install dependencies

```cmd
pip install -r requirements.txt
```

### Run the app

```cmd
python main.py
```

### Run tests (project includes `test_main.py` / `test.py`)

```cmd
pip install pytest
pytest -q
```

### Project layout and important files
- `main.py` — application entry point
- `gui.py` — GUI code
- `img_utils.py` — image-processing helpers
- `files_utils.py` — folder/file helpers
- `config.py` — app configuration
- `data/` — icons and example images

Packaging an executable (PyInstaller example)
If you want to produce the Windows `.exe` used in Releases, PyInstaller is a common choice. Example command (run inside your virtual environment on Windows):

```cmd
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --add-data "data;data" --icon=data\markit_icon.ico MarkIt.py
```

### Notes:
- `--onefile` creates a single `.exe`; `--windowed` hides the Console window.
- `--add-data "data;data"` copies the `data` folder into the app bundle (Windows uses `;` separator).
- After PyInstaller finishes, pick the `.exe` from `dist\` folder and use it as you want without touching code.

---

## Requirements
- Python 3.8+
- See `requirements.txt` for exact packages (e.g., Pillow, customtkinter)

## Troubleshooting (detailed)
- Windows SmartScreen: choose "More info" → "Run anyway".
- Missing DLL errors: install the Visual C++ Redistributable (2015-2022).
- Antivirus quarantine: restore and add an exclusion locally if you trust the binary; report false positive to vendor.
- GUI hang or crash: isolate the image(s) causing the issue and include stack trace when opening an issue.

---

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.
- Open issues for bugs or feature requests.
- Submit pull requests for fixes and enhancements. Please include tests for behavior you add or change.



## License
GNU GPLv3 License
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