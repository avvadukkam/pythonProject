import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

translator = Translator()

# Function to handle translation
def translate_text():
    text = text_entry.get("1.0", "end-1c").strip()
    dest_lang = destination_var.get()

    try:
        translated = translator.translate(text, dest=dest_lang)

        if translated and translated.text:
            translated_text.delete("1.0", "end")
            translated_text.insert("1.0", translated.text)

            if translated.pronunciation:
                pronunciation_label.config(text=f"Pronunciation: {translated.pronunciation}")
            else:
                pronunciation_label.config(text="")

            # Detect source language and update label
            source_lang = translated.src
            source_name = LANGUAGES.get(source_lang, source_lang)
            source_label.config(text=f"Translated from: {source_name.title()}")

        else:
            messagebox.showwarning("Translation Warning", "No translation available for the given text.")

    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred during translation: {str(e)}")

# Initialize GUI
root = tk.Tk()
root.title("Text Translator")

# Input Text Area
text_label = tk.Label(root, text="Enter text to translate:")
text_label.pack()

text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

# Destination Language Dropdown
destination_label = tk.Label(root, text="Select destination language:")
destination_label.pack()

destination_var = tk.StringVar(root)
destination_dropdown = ttk.Combobox(root, textvariable=destination_var, values=list(LANGUAGES.values()))
destination_dropdown.pack()

# Translation Button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Translated Text Area
translated_label = tk.Label(root, text="Translated text:")
translated_label.pack()

translated_text = tk.Text(root, height=5, width=50)
translated_text.pack()

# Pronunciation Label
pronunciation_label = tk.Label(root, text="")
pronunciation_label.pack()

# Source Language Label
source_label = tk.Label(root, text="")
source_label.pack()

root.mainloop()
