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

@bot.command(name='test')
async def test(ctx):
    response = "Hello, this is a test command."
    print(f"Test command received from {ctx.author}: {response}")
    await ctx.send(response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        if len(message.content.split()) == 1:  # check if there is no additional message content
            response = "Misaka just works here"
        else:
            response = "Hi"
        await message.channel.send(response)

    print(f"Received message: {message.content}")
    await bot.process_commands(message)


bot.run(DISCORD_TOKEN)
