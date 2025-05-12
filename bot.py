import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

#Accessing env variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

#Setting up intents and bot
intents = discord.Intents.default()
intents.message_content = True #Enable bot to read message content to detect phrases
bot = commands.Bot(command_prefix='', intents=intents)

selected_phrases = [] #Fill with your own selected phrases to respond to
response_options = [] #Fill with your own responses

#Helper function to check message content against selected phrases
def check_phrases(msg):
    found = False
    for phrase in selected_phrases:
        if phrase in msg:
            found = True
    return found

#Check connection
@bot.event
async def on_ready():
    print(f'{bot.user} is connected to Discord.')

#Respond to selected phrases
@bot.event
async def on_message(message):
    if message.author == bot.user: #Do not read messages from the bot itself
        return

    if check_phrases(message.content.lower()):
        response = f'{message.author.mention} {random.choice(response_options)}' #Ping author of message and select random response
        await message.channel.send(response)

#Use token to connect to Discord
bot.run(TOKEN)