# Basic Utility Tools

A collection of lightweight, practical Python scripts and Jupyter Notebook workflows designed to automate everyday utility tasks, including interval-based automated screen capture, OCR (Optical Character Recognition) text extraction, and media downloading.

---

## 📁 Repository Overview

```text
basic-utility-tools/
│
├── Interval_screenshot/   # Automated interval-based screenshot capture utilities
├── OCR/                   # Optical character recognition scripts to extract text from images
└── yt_dl/                 # Video and audio download helper scripts
```

# Basic Utility Tools

A collection of Python-based utilities for screenshot automation, Optical Character Recognition (OCR), and media downloading.

## ✨ Features & Modules

### 1. Interval Screenshot (`Interval_screenshot/`)

Automatically captures full-screen or window screenshots at customizable time intervals.

**Use cases:**
- Tracking progress and documenting workflows.
- Automated visual logging.
- Creating visual time-lapses.
- Capturing screenshots at regular intervals.

**Technologies:** `PyAutoGUI`, `Pillow`, `OpenCV`

### 2. Optical Character Recognition (OCR) (`OCR/`)

Extracts machine-readable text from images, scanned documents, and screenshots.

**Use cases:**
- Digitizing printed text.
- Extracting text from captured screenshots.
- Batch text recognition.
- Exporting extracted text to `.txt` files.

**Technologies:** `pytesseract`, `Tesseract OCR`, `EasyOCR`

### 3. Media Downloader (`yt_dl/`)

Downloads video and audio from supported media platforms, with options for selecting available formats and quality.

**Features:**
- Downloads supported video and audio streams.
- Supports high-resolution media when available.
- Saves downloaded files locally.
- Uses `yt-dlp` or `pytube` for media extraction.

**Technologies:** `yt-dlp`, `pytube`

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or later.
- Git.
- Tesseract OCR, if using the Tesseract-based OCR implementation.

### Installing Tesseract OCR

If your OCR implementation uses Tesseract, install the OCR engine for your operating system.

**Windows**

Download and install Tesseract OCR using the [UB Mannheim Tesseract installer](https://github.com/UB-Mannheim/tesseract/wiki). Ensure that the installation directory is added to your system's `PATH`.

**macOS**

```bash
brew install tesseract
```

**Linux (Debian/Ubuntu)**

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/SinghVipulRaj/basic-utility-tools.git
cd basic-utility-tools
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

**4. Install the dependencies**

```bash
pip install pillow pyautogui pytesseract easyocr yt-dlp opencv-python jupyterlab
```

Install `pytube` separately if required by your media downloader:

```bash
pip install pytube
```

> **Note:** Install only the dependencies required by the tools you intend to use. Some packages, such as EasyOCR, may require additional system resources.

## 🛠️ Usage

You can run individual utilities from their respective directories or use JupyterLab to work with the available notebooks.

### Launch JupyterLab

From the repository root, run:

```bash
jupyter lab
```

### Running the Screenshot Tool

1. Navigate to `Interval_screenshot/`.
2. Open the relevant Python script or Jupyter notebook.
3. Configure the screenshot interval and output directory.
4. Execute the script or notebook to start capturing screenshots.

### Running OCR

1. Navigate to `OCR/`.
2. Specify the input image or document path.
3. Run the relevant Python script or notebook.
4. View the extracted text in the console or save it to a `.txt` file.

### Running the Media Downloader

1. Navigate to `yt_dl/`.
2. Open the relevant Python script or notebook.
3. Provide the URL of the supported media.
4. Configure the desired output format or quality, if supported.
5. Run the tool to download the media to the configured output directory.

> **Important:** Download media only when you have the necessary rights or permission and comply with the applicable platform terms and copyright laws.

## 📁 Project Structure

```text
basic-utility-tools/
├── Interval_screenshot/
│   └── Screenshot automation scripts/notebooks
├── OCR/
│   └── OCR scripts/notebooks
├── yt_dl/
│   └── Media downloader scripts/notebooks
└── README.md
```

*The directory contents shown above are illustrative. Actual filenames and subdirectories may differ.*

## 🤝 Contributing

Contributions, bug fixes, and feature enhancements are welcome!

To contribute:

1. **Fork** the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/NewUtility
   ```

3. Implement your changes and test them.
4. Commit your changes:

   ```bash
   git commit -m "Add new utility tool"
   ```

5. Push your branch:

   ```bash
   git push origin feature/NewUtility
   ```

6. Open a Pull Request describing your changes.
---

**Built with Python** 🐍
