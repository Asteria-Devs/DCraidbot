import os
import discord
from discord.ext import commands
from database import Database

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
db = Database()

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}!")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
