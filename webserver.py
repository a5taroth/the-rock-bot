# basically what this does is the rock is on his death bed
# and he dies after an hour so this file makes a tube
# for uptimerobot.com to give him oxygen

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "The Rock is grinding.. dont disturb him plz"
    
def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()