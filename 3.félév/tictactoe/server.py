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

def reset():
    global board, turn_x
    board = [["-", "-", "-"] for i in range(3)]
    turn_x = True

def is_valid(index):
    if index[0] < 0 or index[0] > 2 or index[1] < 0 or index[1] > 2:
        return False
    if board[index[0]][index[1]] != "-":
        return False
    return True


async def broadcast(msg: dict):
    dead = []
    for ws in players:
        try:
            await ws.send_text(json.dumps(msg))
        except:
            dead.append(ws)
    for ws in dead:
        players.remove(ws)

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    global turn_x, board

    await ws.accept()

    if len(players) >= 2:
        await ws.send_text(json.dumps({
            "type": "full",
            "message": "Lobby is full."
            }))
        await ws.close()
        return
    
    players.append(ws)
    symbol = "O"
    if len(players) == 1:
        symbol = "X"

    await ws.send_text(json.dumps({
        "type": "init",
        "symbol": symbol,
        "board": board,
        "turn_x": turn_x
    }))

    if len(players) == 2:
        await broadcast({
            "type": "start",
            "board": board,
            "turn_x": turn_x
        })

    try:
        while True:
            raw = await ws.receive_text()
            data = json.loads(raw)
            ## data minta: {"type": "move", "index": (0, 0)}
            if data.get("type") == "move":
                index = data.get("index")

                if symbol == "X" and not turn_x:
                    await ws.send_text(json.dumps({
                        "type": "error",
                        "message": "Nem a te köröd van!"
                    }))
                    continue
                if symbol == "O" and turn_x:
                    await ws.send_text(json.dumps({
                        "type": "error",
                        "message": "Nem a te köröd van!"
                    }))
                    continue

                if not is_valid(index):
                    await ws.send_text(json.dumps({
                        "type": "error",
                        "message": "Érvénytelen lépés!"
                    }))
                    continue
    except:
        pass
