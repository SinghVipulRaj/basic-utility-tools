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

✨ Features & Modules
1. Interval Screenshot (Interval_screenshot/)
Automatically captures full-screen or window screenshots at customizable time intervals.

Useful for tracking progress, automated logging, monitoring workflows, or creating visual time-lapses.

Typically utilizes libraries such as pyautogui, pillow, or opencv.

2. Optical Character Recognition (OCR/)
Extracts machine-encoded text directly from images, scans, and documents.

Ideal for digitizing printed text, extracting snippets from captured screenshots, and quick batch text recognition.

Built using Python OCR frameworks (such as pytesseract / Tesseract OCR or easyocr).

3. Media Downloader (yt_dl/)
Automates video and audio extraction from supported video platforms.

Handles standard and high-resolution streams with direct output storage.

Built using tools like yt-dlp or pytube.

🚀 Getting Started
Prerequisites
Python 3.8+ installed on your system.

Tesseract OCR engine (if using Tesseract-based OCR):

Windows: Download and install via the official UB-Mannheim Tesseract installer and add it to your system PATH.

macOS: brew install tesseract

Linux (Debian/Ubuntu): sudo apt-get install tesseract-ocr

Installation
Clone the repository:

Bash
git clone [https://github.com/SinghVipulRaj/basic-utility-tools.git](https://github.com/SinghVipulRaj/basic-utility-tools.git)
cd basic-utility-tools
Set up a virtual environment (recommended):

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install common dependencies:

Bash
pip install pillow pyautogui pytesseract easyocr yt-dlp opencv-python jupyterlab
🛠️ Usage
Navigate into the individual tool directory or launch Jupyter Notebook:

Bash
jupyter lab
Running the Screenshot Tool
Navigate to Interval_screenshot/ and execute the corresponding Python script or open the notebook to configure capture intervals and save paths.

Running OCR
Navigate to OCR/, specify the target image path in the script/notebook, and run the cells to output extracted text into the console or a .txt file.

Running Media Downloader
Navigate to yt_dl/, supply the target URL in the script/notebook, and run to download the highest-quality stream available.

🤝 Contributing
Contributions, bug fixes, and feature additions are welcome:

Fork the Project.

Create your Feature Branch (git checkout -b feature/NewUtility).

Commit your Changes (git commit -m 'Add new utility tool').

Push to the Branch (git push origin feature/NewUtility).

Open a Pull Request.
