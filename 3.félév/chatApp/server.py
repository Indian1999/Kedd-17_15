import json
import os
import csv
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect # pip install fastapi
from datetime import datetime

app = FastAPI()
PATH = os.path.join(os.path.dirname(__file__), "chat_log.csv")
clients: list[WebSocket] = []

def load_history():
    if not os.path.exists(PATH):
        return []
    with open(PATH, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
    
def append_message(timestamp, username, message):
    new_file = not os.path.exists(PATH)
    with open(PATH, "a", newline= "", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "username", "message"])
        if new_file:
            writer.writeheader()
        writer.writerow({"timestamp": timestamp, "username": username, "message": message})

async def broadcast(data):
    dead = []
    for ws in clients:
        try:
            await ws.send_text(json.dumps(data, ensure_ascii=False))
        except:
            dead.append(ws)
    for ws in dead:
        clients.remove(ws)


@app.websocket("/ws")
async def chat(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    for msg in load_history():
        await websocket.send_text(json.dumps(msg, ensure_ascii=False))

    try:
        while True:
            raw = await websocket.receive_text()
            payload = json.loads(raw)
            data = {
                "timestamp": datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
                "username": payload.get("username", "Ismeretlen"),
                "message": payload.get("message", "")
            }
            append_message(data["timestamp"], data["username"], data["message"])
            await broadcast(data)
    except:
        clients.remove(websocket)
        # Ha bármi hiba fellép, levágjuk a klienst.