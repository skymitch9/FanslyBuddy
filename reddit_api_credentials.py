from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
USERNAME = os.getenv('REDDIT_USERNAME')
PASSWORD = os.getenv('REDDIT_PASSWORD')
USER_AGENT = os.getenv('REDDIT_USER_AGENT')

AUTHORIZATION_URL = 'https://www.reddit.com/api/v1/authorize'
TOKEN_URL = 'https://www.reddit.com/api/v1/access_token'
REDIRECT_URI = 'http://localhost:8000'

SCOPES = ['edit', 'flair', 'history', 'identity', 'modconfig', 'modflair',
          'modlog', 'modposts', 'modwiki', 'mysubreddits', 'privatemessages',
          'read', 'report', 'save', 'submit', 'subscribe', 'vote', 'wikiedit',
          'wikiread']

AUTHORIZE_URL = f'{AUTHORIZATION_URL}?client_id={CLIENT_ID}&response_type=code&state=state&redirect_uri={REDIRECT_URI}&duration=permanent&scope={"+".join(SCOPES)}'
