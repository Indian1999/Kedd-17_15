import asyncio
import json
import tkinter as tk
import websockets
import threading

SERVER = "ws://localhost:8000/ws"

class ChatApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("ChatApp")
        self.root.resizable(False, False)

        self.ws = None
        self.loop = asyncio.new_event_loop()

        self.build_gui()

    def build_gui(self):
        top = tk.Frame(self.root, pady=6, padx=6)
        top.pack(fill=tk.X) # Az ablak teljes szélességét töltse ki
        tk.Label(top, text="Neved: ").pack(side=tk.LEFT)
        self.name_var = tk.StringVar(value="Vendég")
        tk.Entry(top, textvariable=self.name_var, width = 20).pack(side=tk.LEFT, padx=5)

        mid = tk.Frame(self.root, padx=6)
        mid.pack(fill=tk.BOTH, expand = True)
        scrollbar = tk.Scrollbar(mid, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(mid, width=70, height=22, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side= tk.RIGHT, fill=tk.Y)

        bot = tk.Frame(self.root, padx = 6, pady=6)
        bot.pack(fill=tk.BOTH, expand=True)
        self.msg_var = tk.StringVar()
        entry = tk.Entry(bot, textvariable=self.msg_var)
        entry.pack(side=tk.LEFT, fill=tk.X, expand = True)
        tk.Button(bot, text="Küldés", width=8).pack(side=tk.RIGHT, padx=4)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()