import praw
import discord
from discord.ext import commands
from reddit.subreddit_moderator import SubredditModerator
from reddit.user_flair import UserFlair
from reddit.reddit_api_credentials import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD, USER_AGENT
from discord.discord_api_credentials import TOKEN
from discord.bot import DiscordBot
from discord.inactivity_kick import InactivityKick
from discord.inactivity_exceptions import EXCEPTION_LIST

# Initialize Reddit API credentials
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     username=USERNAME,
                     password=PASSWORD,
                     user_agent=USER_AGENT)

# Initialize Discord bot
bot = commands.Bot(command_prefix='!')
discord_bot = DiscordBot(bot)

# Initialize subreddit moderator
subreddit_moderator = SubredditModerator(reddit)

# Initialize user flair
user_flair = UserFlair(reddit)

# Initialize inactivity kick
inactivity_kick = InactivityKick(bot, EXCEPTION_LIST)

# Run Discord bot
bot.run(TOKEN)