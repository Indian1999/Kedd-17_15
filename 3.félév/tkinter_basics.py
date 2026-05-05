import tkinter as tk
from tkinter import ttk

def greet_user():
    name = entry_name.get()
    label_output.config(text=f"Hello {name}!")

root = tk.Tk()
root.title("Hello Tkinter!")
root.geometry("400x225")

label_name = ttk.Label(root, text = "Enter your name:")
label_name.pack()

entry_name = ttk.Entry(root, width=30)
entry_name.pack()
entry_name.focus() # A program indulásakor egyből ide lehet írni

button_hello = ttk.Button(root, text="Üdvözlés", command=greet_user)
button_hello.pack()

label_output = ttk.Label(root, text="", font=("Arial", 18, "bold"))
label_output.pack()

root.mainloop()