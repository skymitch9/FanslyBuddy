from dotenv import load_dotenv
import os
import praw
import discord
from discord.ext import commands
from subreddit_moderator import SubredditModerator
from reddit.user_flair import UserFlair
from reddit_api_credentials import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD, USER_AGENT
from discord_api_credentials import DISCORD_TOKEN
from discord_bot import bot
from discord.inactivity_exceptions import ALLOW_LIST
import subprocess

load_dotenv()

# Initialize Reddit API credentials
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     username=USERNAME,
                     password=PASSWORD,
                     user_agent=USER_AGENT)

# Initialize subreddit moderator
subreddit_moderator = SubredditModerator(reddit)

# Initialize user flair
user_flair = UserFlair(reddit)

# Start local OAuth server
oauth_process = subprocess.Popen(['python', 'local_oauth_server.py'])

# Initialize Discord intents
intents = discord.Intents.default()
intents.members = True

# Run Discord bot
bot.run(DISCORD_TOKEN)

# Stop local OAuth server
oauth_process.terminate()