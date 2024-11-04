# Screenshot Automation Tool

A simple screenshot automation tool that captures screenshots at regular intervals. This application uses `pyautogui` for taking screenshots and `tkinter` for the graphical user interface.

## Features

- Automatically takes screenshots at specified intervals.
- Simple GUI to start and stop the screenshot process.
- Saves screenshots in a specified directory.

## Libraries Required

This project requires the following Python libraries:

- [pyautogui](https://pyautogui.readthedocs.io/en/latest/) - A Python module that allows you to programmatically control the mouse and keyboard.
- [tkinter](https://wiki.python.org/moin/TkInter) - The standard Python interface to the Tk GUI toolkit.
- [threading](https://docs.python.org/3/library/threading.html) - A built-in Python library for concurrent execution.
- [os](https://docs.python.org/3/library/os.html) - A built-in Python library for interacting with the operating system.

## Installation

To get started, follow these steps to install the required libraries:

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required libraries using pip. Open your terminal or command prompt and run the following commands:

   ```bash
   pip install pyautogui
   ```


To create a standalone executable file, use `PyInstaller`. Make sure `PyInstaller` is installed:
```bash
pip install pyinstaller
```

Then, navigate to your project directory and use the following command:
```bash
pyinstaller --onefile --windowed --icon=../ss.ico screenshot.py
```

### Explanation:
- `--onefile`: Packages everything into a single executable file.
- `--windowed`: Hides the terminal window (useful for GUI applications).
- `--icon=ss.ico`: Sets the application icon (make sure `ss.ico` is in the same directory or specify the correct path).

After running this command, the executable can be found in the `dist` folder created within your project directory.
