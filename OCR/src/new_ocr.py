import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageGrab
import pytesseract

# Set the tesseract executable path (Update this path to your actual installation)
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Create the main application window
root = tk.Tk()
root.title("Image to Text Extractor")
root.geometry("500x300")

# Variables to store the selection coordinates
start_x = start_y = end_x = end_y = 0
rect_id = None  # To hold the rectangle ID for visual feedback

def start_selection(event):
    """Record the starting coordinates of the selection."""
    global start_x, start_y
    start_x, start_y = event.x, event.y  # Local (canvas) coordinates
    # Create a new rectangle as visual feedback
    global rect_id
    rect_id = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline='red', width=2)

def update_selection(event):
    """Update the selection rectangle as the user drags the mouse."""
    global rect_id
    # Adjust the rectangle's size based on the current mouse position
    canvas.coords(rect_id, start_x, start_y, event.x, event.y)

def stop_selection(event):
    """Record the ending coordinates and capture the region."""
    global end_x, end_y
    end_x, end_y = event.x, event.y  # Local (canvas) coordinates

    # Convert to screen coordinates to capture the correct region
    x1, y1 = canvas.winfo_rootx() + start_x, canvas.winfo_rooty() + start_y
    x2, y2 = canvas.winfo_rootx() + end_x, canvas.winfo_rooty() + end_y

    # Capture the selected area
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    screenshot.save("captured_area.png")  # Save the captured image

    # Set the path of the captured image in the entry field
    image_entry.delete(0, tk.END)
    image_entry.insert(0, "captured_area.png")

    # Destroy the selection window after capturing
    selection_window.destroy()

    # Show the main window again
    root.deiconify()

def capture_screen_area():
    """Create a fullscreen selection window with a canvas for feedback."""
    global selection_window, canvas

    # Hide the main window to avoid interference
    root.withdraw()

    # Create a fullscreen window for selection
    selection_window = tk.Toplevel(root)
    selection_window.attributes("-fullscreen", True)
    selection_window.attributes("-alpha", 0.3)  # Transparent overlay
    selection_window.config(bg='black')

    # Create a canvas to draw the selection rectangle
    canvas = tk.Canvas(selection_window, bg='black', highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Bind mouse events to the canvas for selecting an area
    canvas.bind("<ButtonPress-1>", start_selection)  # Start selection
    canvas.bind("<B1-Motion>", update_selection)  # Update rectangle during drag
    canvas.bind("<ButtonRelease-1>", stop_selection)  # Finalize selection

def extract_text():
    """Extract text from the selected image."""
    image_path = image_entry.get()
    if not image_path:
        messagebox.showerror("Error", "Please capture an image.")
        return

    try:
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img)

        # Display the extracted text in a new window
        result_window = tk.Toplevel(root)
        result_window.title("Extracted Text")
        text_box = tk.Text(result_window, wrap=tk.WORD)
        text_box.pack(expand=True, fill=tk.BOTH)
        text_box.insert(tk.END, extracted_text)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract text. Error: {str(e)}")

# Create labels and buttons for the UI
tk.Label(root, text="Image Path:").pack(pady=10)
image_entry = tk.Entry(root, width=50)
image_entry.pack()

tk.Button(root, text="Capture Image", command=capture_screen_area).pack(pady=5)
tk.Button(root, text="Extract Text", command=extract_text).pack(pady=20)

# Start the GUI event loop
root.mainloop()
