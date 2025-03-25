import random

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
gameOn = True
player_1_turn = True
winner = "draw"

def show_board():
    print("# | 1 | 2 | 3 ")
    print(f"1 | {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"2 | {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"3 | {board[2][0]} | {board[2][1]} | {board[2][2]}")
    if player_1_turn:
        print("A O játékos következik.")
    else:
        print("Az X játékos következik.")
    
def read_and_put_symbol():
    correct_placement = False
    while not correct_placement:
        sor = int(input("Adj meg egy sort:\n"))
        while sor < 1 or sor > 3:
            sor = int(input("Adj meg egy sort:\n"))   
        oszlop = int(input("Adj meg egy oszlopot:\n"))
        while oszlop < 1 or oszlop > 3:
            oszlop = int(input("Adj meg egy oszlopot:\n"))
        
        if board[sor-1][oszlop-1] == "-":
            correct_placement = True
            if player_1_turn:
                board[sor-1][oszlop-1] = "O"
            else:
                board[sor-1][oszlop-1] = "X"
    
def check_for_win():
    # Sorok ellenőrzése
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != "-":
            if player_1_turn:
                winner = "O wins"
            else:
                winner = "X wins"
            return True
    # Oszlopok ellenőrzése
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] != "-":
            if player_1_turn:
                winner = "O wins"
            else:
                winner = "X wins"
            return True
    # Átlók ellenőrzése
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "-": #Főátló
            if player_1_turn:
                winner = "O wins"
            else:
                winner = "X wins"
            return True    
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != "-": #Mellékátló
            if player_1_turn:
                winner = "O wins"
            else:
                winner = "X wins"
            return True   
    return False 
  
def check_for_draw():
    for lista in board:
        print(lista)
        if "-" in lista:
            return False
    return True
  
while gameOn:
    # A játékállás megjelenítése
    show_board()
        
    # A sor-oszlop index megfelelő beolvasása 
    read_and_put_symbol()
    
    # Win condition ellenőrzése
    have_winner = check_for_win()
    if have_winner:
        gameOn = False
        break # Kilép a ciklusból
    draw = check_for_draw()
    if draw:
        break
    player_1_turn = not player_1_turn
print(winner)
    
        
    