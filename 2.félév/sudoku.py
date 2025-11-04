import tkinter as tk
board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j

def valid(board, num, row, col):
    for j in range(9):
        if board[row][j] == num:
            return False
    for i in range(9):
        if board[i][col] == num:
            return False
    sq_row = row // 3 * 3      # pl.: 5 -> 3,  7 -> 6, 3 -> 3
    sq_col = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[sq_row + i][sq_col + j] == num:
                return False
    return True
    
def solve(board):
    empty = find_empty(board)
    if empty == None:
        return True
    row, col = empty     # row, col = (0, 2)   -> row = 0, col = 2
    for i in range(1, 10):
        if valid(board, i, row, col):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def print_board(board):
    for i in range(9):
        if i % 3 == 0:            
            print("■ " * 13)
        for j in range(9):
            if j % 3 == 0:
                print("■ ", end = "")
            print(board[i][j], end = " ")
        print("■")
    print("■ " * 13)

root = tk.Tk()
root.title("Sudoku Solver")

cells = [[None for j in range(9)] for i in range(9)]

def draw_board(pad:int = 3):
    for i in range(9):
        for j in range(9):
            entry = tk.Entry(root, width=3, justify="center")
            entry.grid(row=i, column=j, padx=pad, pady=pad)

            if board[i][j] != 0:
                entry.insert(0, str(board[i][j]))
                entry.config(state="disabled", disabledforeground="black", disabledbackground="gray")

            cells[i][j] = entry

def update_gui():
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END) # 0.tól az utolsó karakterig töröljük a textbox tartalmát
            cells[i][j].insert(0, str(board[i][j]))

def solve_and_show():
    solve(board)
    update_gui()

draw_board(pad = 5)
solve_button = tk.Button(root, text="Solve", command=solve_and_show)
solve_button.grid(row=9, column=0, columnspan=9, pady=10)
root.mainloop()

