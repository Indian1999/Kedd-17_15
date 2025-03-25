import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        
        self.current_player = "X"
        self.board = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_board()
        
        self.window.mainloop()
    
    def create_board(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.window, text="", font=("Arial", 24), height=2, width=5,
                                command=lambda r=row, c=col: self.make_move(r, c))
                btn.grid(row=row, column=col)
                self.board[row][col] = btn
    
    def make_move(self, row, col):
        if self.board[row][col]["text"] == "":
            self.board[row][col]["text"] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        for row in range(3):
            if self.board[row][0]["text"] == self.board[row][1]["text"] == self.board[row][2]["text"] != "":
                return True
        
        for col in range(3):
            if self.board[0][col]["text"] == self.board[1][col]["text"] == self.board[2][col]["text"] != "":
                return True
        
        if self.board[0][0]["text"] == self.board[1][1]["text"] == self.board[2][2]["text"] != "":
            return True
        
        if self.board[0][2]["text"] == self.board[1][1]["text"] == self.board[2][0]["text"] != "":
            return True
        
        return False
    
    def is_draw(self):
        return all(self.board[row][col]["text"] != "" for row in range(3) for col in range(3))
    
    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col]["text"] = ""
        self.current_player = "X"

if __name__ == "__main__":
    TicTacToe()
