import random

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def show_board():
    print("# | 1 | 2 | 3 ")
    print(f"1 | {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"2 | {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"3 | {board[2][0]} | {board[2][1]} | {board[2][2]}")
    
gameOn = True
player_1_turn = True
while gameOn:
    show_board()
    if player_1_turn:
        print("A O játékos következik.")
    else:
        print("Az X játékos következik.")
    
    correct_placement = False
    while not correct_placement:
        sor = int(input("Adj meg egy sort:\n"))
        while sor < 1 or sor > 3:
            sor = int(input("Adj meg egy sort:\n"))   
        oszlop = int(input("Adj meg egy oszlopot:\n"))
        while oszlop < 1 or oszlop > 3:
            oszlop = int(input("Adj meg egy oszlopot:\n"))
        
        if board[sor][oszlop] == "-":
            correct_placement = True
            if player_1_turn:
                board[sor][oszlop] = "O"
            else:
                board[sor][oszlop] = "X"
    
        
    