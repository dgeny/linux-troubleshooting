from flask import Flask
from hashlib import sha384


app = Flask(__name__)

@app.route("/")
def root():
    return '{"status": 1, "message": "fast"}' 

@app.route("/hard")
def hard():
    hash384 = sha384('password'.encode())
    c = 0
    while c < 5000000:
        hash384.update(hash384.digest())
        c = c+1 
    return {"status": 1, "message": hash384.hexdigest()} 

@app.route("/loop")
def infloop():
    hash384 = sha384('password'.encode())
    c = 0
    while c < 50000:
        hash384.update(hash384.digest())
        # c = c+1 
    return {"status": 1, "message": hash384.hexdigest()}
