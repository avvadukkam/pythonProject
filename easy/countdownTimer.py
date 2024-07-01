import tkinter as tk
from tkinter import messagebox
import time
import winsound  # Only available on Windows

def countdown_timer():
    try:
        total_seconds = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for hours, minutes, and seconds.")
        return

    while total_seconds >= 0:
        mins, secs = divmod(total_seconds, 60)
        hrs, mins = divmod(mins, 60)
        time_format = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
        time_label.config(text=time_format)
        root.update()
        time.sleep(1)
        total_seconds -= 1

    messagebox.showinfo("Time's up", "Time's up!")
    winsound.Beep(1000, 1000)  # Beep sound for 1 second

root = tk.Tk()
root.title("Countdown Timer")

tk.Label(root, text="Hours:").grid(row=0, column=0)
tk.Label(root, text="Minutes:").grid(row=1, column=0)
tk.Label(root, text="Seconds:").grid(row=2, column=0)

hours_var = tk.StringVar(value="0")
minutes_var = tk.StringVar(value="0")
seconds_var = tk.StringVar(value="0")

hours = tk.Entry(root, textvariable=hours_var)
minutes = tk.Entry(root, textvariable=minutes_var)
seconds = tk.Entry(root, textvariable=seconds_var)


hours.grid(row=0, column=1)
minutes.grid(row=1, column=1)
seconds.grid(row=2, column=1)

start_button = tk.Button(root, text="Start Countdown", command=countdown_timer)
start_button.grid(row=3, column=1)

time_label = tk.Label(root, font=('Helvetica', 48), text="00:00:00")
time_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
