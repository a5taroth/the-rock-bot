# okay so this is basically the rocks heart if you break it
# he will die so dont break it but it also tells him what
# to do and how to do so plz dont break it

import discord

from random import choice # for choosing :)
from urllib.request import urlopen # for opening the url
from json import load # for the json
from os import environ # for the token
from discord.ext import commands # dunno what this does but we need it for the bot to work lmao
from webserver import keep_alive # function to keep the webserver running

bot = commands.Bot(
  command_prefix = "!",
  activity = discord.Activity(
    name = "Face Off",
    type = discord.ActivityType.listening
  ),
  status = discord.Status.online
)
players = []

possible_words = ("Hello", "Bye", "Bad", "Idiot")
hangman_word = choice(possible_words) 

image_path = [
    "chains.jpg",
    "hercules.jpg",
    "idk.jpg",
    "muscles.webp"
]

quote_url = "http://www.famous-quotes.uk/api.php?id=random&minpop=75"

@bot.event
async def on_ready():
    print(f"Executing on {bot.user}")


    @bot.command(
        name="ping",
        help="Tells you how fast The Rock can eat 100 pancakes",
        pass_context=True,
        aliases=["pingpong", "pong", "latency"]
    )
    async def ping(ctx):
        await ctx.send(f":ping_pong: Pong! **{round(bot.latency*1000)} ms**")


    @bot.command(
        name="pancake",
        aliases=["pc", "pancakes"]
    )
    async def eat_pancakes(ctx):
        embed_ = discord.Embed(
            description="The Rock is eating pancakes... like a lot of 'em."
        )
        embed_.set_image(url="http://www.fitness-clubs.be/img/dyn.php?src=/upload-news-pictures/53da57f17a435/news.png&w=400")
        await ctx.channel.send(
            embed = embed_
        )


    @bot.command(
        name="quote",
        help="The Rock will send a very inspiring quote that is guarenteed to be extremely knowledgeable.",
        aliases=["quotes", "q", "i_am_depressed", "nobody_will_ever_find_out_that_this_is_an_alias"]
    )
    async def send_a_quote(ctx):
       quote = load(urlopen(quote_url))[0] # The [0] is because the table is formatted weirdly /shrug

# quote[0] = ID
# quote[1] = Quote
# quote[2] = Author

       await ctx.channel.send(
            embed = discord.Embed(
                title="Quote",
                description=(
                    f"{quote[1]}"
                    f"\n *- ~~{quote[2]}~~ The Rock*"
                ),
                url=f"http://www.Famous-Quotes.uk/api.php?id={quote[0]}"
            )
        )


    @bot.command(
        name="image",
        help="The Rock will flex his muscles... or not.",
        aliases=["img","photo"]
    )
    async def image(ctx):
        await ctx.channel.send(
            embed = discord.Embed(
                title = "Massive Muscles",
                color = discord.Color.blue(),
                description = "The image is... ~~not yet~~ now available."
            ),
            file = discord.File(
                f"the_rock_images/{choice(image_path)}"  
            )
        )


    @bot.command(
        name="race",
        help="Race against another player in your vehicle of choice as the Rock cheers you on.",
        aliases=["Race", "RACE", "vroom-vroom", "vroom vroom"]
    )
    async def vroom_vroom(ctx, arg):
        await players.extend(ctx.author)

        await ctx.channel.send(
            embed = discord.Embed(
                title = "Bumpy Ride by ~~Mohambi~~ The Rock", #HAHAHAHAHAHAHAHHAHA
                description = "Atleast two players needed to begin.",
                color = discord.Color.red()
            )
        )


    @bot.command( # it doesnt like this line apparently 
        name="hangman",
        aliases=["hm", "manhang?"]
    )
    async def hang_the_man(ctx):
        print("idiot")
      
        
    
keep_alive()
bot.run(environ['TOKEN'])