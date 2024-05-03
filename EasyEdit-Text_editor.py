from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

window = Tk()
window.geometry('500x500')
window.title('EASY EDIT')

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

Editor = tk.Text(
    window,
    width=4000,
    height=4500,
    yscrollcommand=scrollbar.set
)
Editor.pack(fill=BOTH)

def save():
    filepath = asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = Editor.get(1.0, tk.END)
        output_file.write(text)
    window.title(f'Entitled – {filepath}')





window.mainloop()