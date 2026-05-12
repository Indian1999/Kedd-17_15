import json
import os
import csv
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect # pip install fastapi
from datetime import datetime

app = FastAPI()
PATH = os.path.join(os.path.dirname(__file__), "chat_log.csv")
clients: list[WebSocket] = []

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

    try:
        while True:
            raw = await websocket.recieve_text()
            payload = json.loads(raw)
            data = {
                "timestamp": datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
                "username": payload.get("username", "Ismeretlen"),
                "message": payload.get("message", "")
            }
            await broadcast(data)
    except:
        clients.remove(websocket)
        # Ha bármi hiba fellép, levágjuk a klienst.