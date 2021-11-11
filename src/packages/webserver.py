# Copyright (C) 2021, A5taroth and iluvsoup
# This package keeps the bot running using Uptime Robot

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main(): return "The Rock is holding up this webserver with his titan-like strength."

def host(): app.run(host="0.0.0.0", port=8080)

def run(): Thread(target=host).start()