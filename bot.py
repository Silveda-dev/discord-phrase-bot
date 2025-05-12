import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

#Accessing env variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#Setting up intents and bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='', intents=intents)

#Check connection
@bot.event
async def on_ready():
    print(f'{bot.user} is connected to Discord.')

#Use token to connect to Discord
bot.run(TOKEN)