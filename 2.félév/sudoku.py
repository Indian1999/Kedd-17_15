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
    """
    Igazt ad vissza, ha a board[row][col] helyére be lehet írni legálisan a numot
    Egyébként hamis értéket ad vissza
    (Egy sorban csak egyszer szerepelhet egy szám)
    (Egy oszlolpban csak egyszer szerepelhet egy szám)
    (Egy kisebb négyzetben szintén csak egszer egy szám)
    """
    pass

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
            else:
                return False
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

print_board(board)
solve(board)
print("Solved:")
print_board(board)