import discord
from discord.ext import commands
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Function to fetch meme
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

# Setup bot with command prefix and message content intent
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.command()
async def meme(ctx):
    await ctx.send(get_meme())

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# ✅ Use the correct bot variable
bot.run(os.getenv("TOKEN"))