import tkinter as tk
import pyautogui
from datetime import datetime

def take_screenshot():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{current_time}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    status_label.config(text=f"Screenshot saved as {filename}")

# Create the main window
root = tk.Tk()
root.title("Screenshot App")

# Create a button to take screenshot
take_screenshot_btn = tk.Button(root, text="Take Screenshot", command=take_screenshot)
take_screenshot_btn.pack(pady=20)

# Label to show status
status_label = tk.Label(root, text="")
status_label.pack()

# Run the main loop
root.mainloop()
