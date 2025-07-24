import os
import discord
from discord.ext import commands, tasks

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1373366508540924054

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    send_reminder.start()

@tasks.loop(hours=24)
async def send_reminder():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("👋 Time for your daily standup!\n\n1. What did you do yesterday?\n2. What will you do today?\n3. Any blockers?")

send_reminder.before_loop
async def before():
    await bot.wait_until_ready()

bot.run(TOKEN)
