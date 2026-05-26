import tkinter as tk
from tkinter import messagebox
import asyncio
import threading
import websockets
import json
import queue

SERVER_URL = "ws://localhost:8000/ws"

class TicTacToeClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.symbol = None
        self.my_turn = False
        self.game_started = False
        self.ws = None
        self.msg_queue = queue.Queue()

        self._build_ui()
        self._start_ws_thread()
        self._poll_queue()

    def _build_ui(self):
        self.status_var = tk.StringVar(value="Csatlakozás...")
        tk.Label(self.root, textvariable=self.status_var, font=("Arial", 14)).grid(
            row=0, column=0, columnspan=3, pady=10
        )

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(
                    self.root, text="", font=("Arial", 28, "bold"),
                    width=4, height=2,
                    command=lambda r=i, c=j: self._on_click(r, c)
                )
                btn.grid(row=i + 1, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def _start_ws_thread(self):
        self.loop = asyncio.new_event_loop()
        t = threading.Thread(target=self._run_ws, daemon=True)
        t.start()

    def _run_ws(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._ws_handler())

    async def _ws_handler(self):
        try:
            async with websockets.connect(SERVER_URL) as ws:
                self.ws = ws
                async for raw in ws:
                    data = json.loads(raw)
                    self.msg_queue.put(data)
        except Exception as e:
            self.msg_queue.put({"type": "conn_error", "message": str(e)})

    def _poll_queue(self):
        try:
            while True:
                msg = self.msg_queue.get_nowait()
                self._handle_msg(msg)
        except queue.Empty:
            pass
        self.root.after(100, self._poll_queue)

    def _handle_msg(self, data):
        t = data.get("type")

        if t == "init":
            self.symbol = data["symbol"]
            self.status_var.set(f"Te vagy: {self.symbol} — Várakozás a másik játékosra...")
            self._update_board(data["board"])

        elif t == "start":
            self.game_started = True
            self._update_board(data["board"])
            self._update_turn(data["turn_x"])

        elif t == "update":
            self._update_board(data["board"])
            self._update_turn(data["turn_x"])

        elif t == "end":
            self._update_board(data["board"])
            winner = data["winner"]
            if winner == "draw":
                msg = "Döntetlen!"
            elif winner == self.symbol:
                msg = "Nyertél!"
            else:
                msg = "Vesztettél!"
            self.status_var.set(msg)
            self._disable_all()
            messagebox.showinfo("Játék vége", msg)

        elif t == "error":
            self.status_var.set(f"Hiba: {data['message']}")

        elif t == "full":
            self.status_var.set("A szoba tele van!")
            messagebox.showerror("Hiba", data["message"])
            self.root.destroy()

        elif t == "opponent left":
            self.status_var.set("Az ellenfél kilépett.")
            self._disable_all()
            messagebox.showinfo("Játék vége", data["message"])

        elif t == "conn_error":
            self.status_var.set(f"Kapcsolódási hiba: {data['message']}")

    def _update_board(self, board):
        for i in range(3):
            for j in range(3):
                val = board[i][j]
                text = val if val != "-" else ""
                color = "blue" if val == "X" else ("red" if val == "O" else "black")
                self.buttons[i][j].config(text=text, fg=color)

    def _update_turn(self, turn_x):
        self.my_turn = (turn_x and self.symbol == "X") or (not turn_x and self.symbol == "O")
        if self.my_turn:
            self.status_var.set(f"Te jössz! ({self.symbol})")
        else:
            opp = "O" if self.symbol == "X" else "X"
            self.status_var.set(f"Az ellenfél lép... ({opp})")

    def _on_click(self, row, col):
        if not self.game_started or not self.my_turn:
            return
        if self.buttons[row][col].cget("text") != "":
            return
        asyncio.run_coroutine_threadsafe(self._send_move(row, col), self.loop)

    async def _send_move(self, row, col):
        await self.ws.send(json.dumps({"type": "move", "index": [row, col]}))

    def _disable_all(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    TicTacToeClient(root)
    root.mainloop()
