import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + number)


def button_clear():
    entry.delete(0, tk.END)


def button_equal():
    expression = entry.get()
    entry.delete(0, tk.END)

    try:
        result = eval(expression)  # Evaluate the expression
        entry.insert(0, result)
    except Exception as e:
        entry.insert(0, "Error")  # Display an error message if evaluation fails
        print(f"Error: {e}")


# Define buttons with appropriate text, row, and column positions
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create buttons and place them in the grid with adjusted padding
for (btn_text, row, col) in buttons:
    button = tk.Button(root, text=btn_text, padx=20, pady=10, command=lambda t=btn_text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Adjust column configurations to control spacing
root.columnconfigure((0, 1, 2, 3), weight=1, minsize=50)  # Adjust minsize as needed

# Clear button
clear_button = tk.Button(root, text="Clear", padx=72, pady=10, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Equal button
equal_button = tk.Button(root, text="=", padx=20, pady=10, command=button_equal)
equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
