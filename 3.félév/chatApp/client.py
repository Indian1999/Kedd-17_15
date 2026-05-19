import asyncio
import json
import tkinter as tk
import websockets
import threading
from tkinter import messagebox

SERVER = "ws://hauerszabolcs.hu:8020/ws"

class ChatApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("ChatApp")
        self.root.resizable(False, False)

        self.ws = None
        self.loop = asyncio.new_event_loop()

        self.build_gui()
        self.start_ws_thread()

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
        entry.bind("<Return>", lambda x: self.send())
        tk.Button(bot, text="Küldés", width=8, command=self.send).pack(side=tk.RIGHT, padx=4)

    def start_ws_thread(self):
        t = threading.Thread(target=self.run_loop, daemon=True)
        t.start()

    def run_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.connect())

    async def connect(self):
        try:
            async with websockets.connect(SERVER) as ws:
                self.ws = ws
                async for raw in ws:
                    data = json.loads(raw)
                    line = f"{data['timestamp']} - {data['username']}:"
                    self.root.after(0, self.append_to_list, line)
                    line = f"{data['message']}"
                    self.root.after(0, self.append_to_list, line)
        except Exception as ex:
            self.root.after(0, messagebox.showerror, "Kapcsolati hiba!", str(ex))

    def append_to_list(self, line):
        self.listbox.insert(tk.END, line)
        self.listbox.see(tk.END)

    def send(self):
        msg = self.msg_var.get().strip()
        if not msg:
            return
        name = self.name_var.get().strip()
        if not name:
            name = "Ismeretlen"
        payload = json.dumps({"username": name, "message": msg}, ensure_ascii=False)
        if self.ws:
            asyncio.run_coroutine_threadsafe(self.ws.send(payload), self.loop)
        self.msg_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()