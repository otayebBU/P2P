#api.py

from fastapi import FastAPI
from pydantic import BaseModel
import socket
from secure_utils import encrypt

app = FastAPI()

peers = {}           
subscriptions = {}   
blocked = {}         
muted = {}           
class Peer(BaseModel):
    username: str
    ip: str
    port: int

class Sub(BaseModel):
    subscriber: str
    target: str

class Message(BaseModel):
    from_user: str
    to: str
    message: str
    special: bool = False

def send_message(ip, port, message):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(encrypt(message))
        s.close()
    except Exception as e:
        print(f"Failed to send to {ip}:{port}, Error: {e}")

@app.post("/register")
def register_peer(peer: Peer):
    peers[peer.username] = (peer.ip, peer.port)
    return {"status": "registered", "peers": peers}

@app.post("/subscribe")
def subscribe(sub: Sub):
    if sub.target not in subscriptions:
        subscriptions[sub.target] = []
    if sub.subscriber not in subscriptions[sub.target]:
        subscriptions[sub.target].append(sub.subscriber)
    return {"status": f"{sub.subscriber} subscribed to {sub.target}"}

@app.post("/block")
def block_user(sub: Sub):
    if sub.target not in blocked:
        blocked[sub.target] = []
    blocked[sub.target].append(sub.subscriber)
    return {"status": f"{sub.subscriber} blocked by {sub.target}"}

@app.post("/mute")
def mute_user(sub: Sub):
    if sub.target not in muted:
        muted[sub.target] = []
    muted[sub.target].append(sub.subscriber)
    return {"status": f"{sub.subscriber} muted by {sub.target}"}

@app.post("/send")
def send(msg: Message):
    if msg.special:
        recipients = subscriptions.get(msg.to, [])
    else:
        recipients = [msg.to]

    sent_to = []
    for user in recipients:
        if user in peers:
            if msg.from_user in blocked.get(user, []):
                continue
            if user in muted.get(msg.from_user, []):
                continue
            ip, port = peers