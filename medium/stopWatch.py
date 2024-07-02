import tkinter as Tkinter
from datetime import datetime, timedelta

counter = 0
running = False


def counter_label(label):
    def count():
        if running:
            global counter

            # Calculate hours, minutes, seconds, and milliseconds
            ms = counter % 1000
            seconds = (counter // 1000) % 60
            minutes = (counter // (1000 * 60)) % 60
            hours = (counter // (1000 * 60 * 60)) % 24

            # Format the time as HH:MM:SS:mmm
            display = '{:02}:{:02}:{:02}:{:03}'.format(hours, minutes, seconds, ms)
            label['text'] = display

            # Update counter and call count() again after 1 millisecond
            label.after(1, count)
            counter += 1

    # Start the counter function
    count()


# Function to start or stop the stopwatch
def StartStop(label):
    global running
    if running:
        running = False
        start_stop_btn.config(text='Start')
        stop_watch_btn.config(state='normal')
    else:
        running = True
        start_stop_btn.config(text='Stop')
        stop_watch_btn.config(state='disabled')
        counter_label(label)


# Function to reset the stopwatch
def Reset(label):
    global counter, running
    counter = 0
    label['text'] = '00:00:00:000'
    running = False
    start_stop_btn.config(text='Start')
    stop_watch_btn.config(state='normal')


root = Tkinter.Tk()
root.title("Stopwatch")

# Fixing the window size.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text='00:00:00:000', fg='black', font='Verdana 30 bold')
label.pack()
f = Tkinter.Frame(root)
start_stop_btn = Tkinter.Button(f, text='Start', width=6, command=lambda: StartStop(label))
stop_watch_btn = Tkinter.Button(f, text='Reset', width=6, command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start_stop_btn.pack(side='left')
stop_watch_btn.pack(side='left')
root.mainloop()
