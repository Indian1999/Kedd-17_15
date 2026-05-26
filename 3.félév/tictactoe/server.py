from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json

app = FastAPI()

board = [["-", "-", "-"] for i in range(3)]
players: list[WebSocket] = []
turn_x = True # True - X;   False - O

def check_winner():
    wins = [
        ((0,0), (0, 1), (0,2)), # sor 0
        ((1,0), (1, 1), (1,2)), # sor 1
        ((2,0), (2, 1), (2,2)), # sor 2
        ((0,0), (1, 0), (2,0)), # oszlop 0
        ((0,1), (1, 1), (2,1)), # oszlop 1
        ((0,2), (1, 2), (2,2)), # oszlop 2
        ((0,0), (1, 1), (2,2)), # Főátló
        ((0,2), (1, 1), (2,0)), # Mellékátló
    ]
    for win in wins: # win pl.: ((0,0), (0, 1), (0,2))
        cell = board[win[0][0]][win[0][1]]
        if cell == "-":
            continue
        if cell == board[win[1][0]][win[1][1]]:
            if cell == board[win[2][0]][win[2][1]]:
                return cell   # "X" vagy "O"
    # Döntetlen ellenőrzése:
    draw = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                draw = False
                break
        if not draw:
            break
    if draw:
        return "draw"
    return None



