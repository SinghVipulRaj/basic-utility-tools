import pyautogui
import time
import threading
import tkinter as tk
from tkinter import messagebox
import os

# Global variable to control screenshot taking
taking_screenshots = False
screenshot_interval = 40  # Time between screenshots in seconds
save_path = r'G:\New_folder'  # Path to save screenshots

def take_screenshots():
    i = 1
    while i <= 240:
        if not taking_screenshots:  # Check if stop is triggered
            break
        try:
            time.sleep(5)
            my_screenshot = pyautogui.screenshot()
            my_screenshot.save(os.path.join(save_path, f"({i}).png"))
            i += 1
            time.sleep(screenshot_interval - 5)  # Adjust for initial 5-second delay
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            break
    if i > 240:
        messagebox.showinfo("Info", "Screenshots completed!")
    root.quit()  # Ensures the application closes after stopping screenshots

def start_screenshots():
    global taking_screenshots
    taking_screenshots = True
    start_button.destroy()  # Hide the start button
    close_button.destroy()  # Hide the close button
    threading.Thread(target=take_screenshots, daemon=True).start()  # Start thread with daemon=True
    root.destroy()
    show_stop_button()  # Show the floating stop button

def stop_screenshots():
    global taking_screenshots
    taking_screenshots = False
    stop_button.destroy()  # Close the floating stop button
    os.startfile(save_path)  # Open the folder where screenshots are saved

def close_app():
    root.destroy()

def show_stop_button():
    global stop_button
    stop_button = tk.Tk()
    stop_button.overrideredirect(True)  # Remove window decorations
    stop_button.geometry("50x20+{}+{}".format(stop_button.winfo_screenwidth()//2 - 10, 2))
    stop_button.attributes("-topmost", True)  # Keep it on top
    tk.Button(stop_button, text="Stop", command=stop_screenshots, fg="white", bg="red", font=("Arial", 12, "bold")).pack(fill=tk.BOTH, expand=True)
    stop_button.mainloop()

# Set up the initial floating "Start" and "Close" buttons
root = tk.Tk()
root.overrideredirect(True)
root.geometry("220x20+{}+{}".format(root.winfo_screenwidth()//2 - 60, 2))
root.attributes("-topmost", True)



# Start button to begin recording
start_button = tk.Button(root, text="Start", command=start_screenshots, fg="white", bg="green", font=("Arial", 12, "bold"), width=10)
start_button.pack(side=tk.LEFT, padx=5)

# Close button to exit the application
close_button = tk.Button(root, text="Close", command=close_app, fg="white", bg="grey", font=("Arial", 12, "bold"), width=10)
close_button.pack(side=tk.RIGHT, padx=5)

# Start the Tkinter event loop
root.mainloop()
