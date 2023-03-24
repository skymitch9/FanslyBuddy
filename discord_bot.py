import discord
from discord.ext import commands
from discord_api_credentials import DISCORD_TOKEN
from discord.inactivity_exceptions import ALLOW_LIST
from datetime import datetime, timedelta

# Initialize Discord intents
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='kick_inactive_users')
async def kick_inactive_users(ctx, days: int):
    now = datetime.utcnow()
    guild = ctx.guild
    for member in guild.members:
        if member.id not in ALLOW_LIST:
            if not member.voice:
                if (now - member.joined_at) > timedelta(days=days):
                    await member.kick(reason=f"Inactive for {days} days.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "<@!Sky#3540>":
        response = "Misaka just works here"
        await message.channel.send(response)

    await bot.process_commands(message)
