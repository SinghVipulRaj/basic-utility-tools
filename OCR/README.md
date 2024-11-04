
# Image to Text Extractor

This project uses `Tkinter`, `Pillow`, and `pytesseract` to extract text from images. Follow the steps below to set up the required libraries on your computer.

## Prerequisites

1. **Python**: Ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/).
   - **Note**: Make sure to check the box to add Python to your PATH during installation.

2. **Tesseract OCR**: This project uses Tesseract, an open-source OCR engine, for text extraction.
   - Download Tesseract from the [official Tesseract GitHub page](https://github.com/tesseract-ocr/tesseract).
   - During installation, note the installation path, which will be needed for configuration in your code (typically `C:\Program Files\Tesseract-OCR\tesseract.exe` on Windows).
   - After installation, add Tesseract to your system’s PATH to make it accessible.

## Installing Python Libraries

1. **Tkinter**: `Tkinter` is often included with Python installations. To verify its installation, you can run the following command in Python:
   ```python
   import tkinter
   ```
   If no error appears, `Tkinter` is already installed. If not, follow the installation instructions below.

   - **Linux/Ubuntu**: Run:
     ```bash
     sudo apt-get install python3-tk
     ```

   - **Windows**: Tkinter should be included with Python installations by default.

2. **Pillow (PIL)**: This library is used for image handling and manipulation.
   - Install using `pip`:
     ```bash
     pip install pillow
     ```

3. **pytesseract**: This is the Python wrapper for Tesseract OCR.
   - Install using `pip`:
     ```bash
     pip install pytesseract
     ```

### Configuration Example

In your code, specify the path to the Tesseract executable (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`) as follows:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

Now you're ready to run the application!


## Creating an Executable

To create a standalone executable file, use `PyInstaller`. Make sure `PyInstaller` is installed:
```bash
pip install pyinstaller
```

Then, navigate to your project directory and use the following command:
```bash
pyinstaller --onefile --windowed --icon=../ocr.ico new_ocr.py
```

### Explanation:
- `--onefile`: Packages everything into a single executable file.
- `--windowed`: Hides the terminal window (useful for GUI applications).
- `--icon=ocr.ico`: Sets the application icon (make sure `ocr.ico` is in the same directory or specify the correct path).

After running this command, the executable can be found in the `dist` folder created within your project directory.
