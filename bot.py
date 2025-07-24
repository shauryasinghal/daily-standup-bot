import os
import discord
from discord.ext import commands, tasks
from datetime import datetime

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    send_standup_reminder.start()

@tasks.loop(time=datetime.strptime("10:00", "%H:%M").time())
async def send_standup_reminder():
    channel_id = 1373366508540924054  # 🔁 Replace with your channel ID (without quotes)
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("👋 Good morning team! Please post your daily standup updates.")

bot.run(TOKEN)

