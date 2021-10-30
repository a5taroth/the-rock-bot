# The main program where everything runs (I mean it's called main.py)

import shit
import random

from datetime import time
from os import environ 
from webserver import keep_alive 

@shit.bot.event
async def on_ready():
    random.seed(time)
    print(f"{shit.bot.user} is now online.")


@shit.bot.event
async def on_message(msg):
    await shit.bot.process_commands(msg)

keep_alive()
shit.bot.run(environ['TOKEN'])