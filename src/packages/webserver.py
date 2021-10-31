# This script keeps the bot running using Uptime Robot

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "The Rock is grinding... don't disturb him and go to discord.com"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()