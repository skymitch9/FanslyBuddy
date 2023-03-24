import praw
from reddit_api_credentials import client_id, client_secret, username, password, subreddits, allowed_keywords, denied_keywords

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, username=username, password=password, user_agent="Moderation bot by u/YourUsername")

def check_for_blacklisted_words(title, body):
    # Check if post contains any denied keywords
    for keyword in denied_keywords:
        if keyword in title.lower() or keyword in body.lower():
            return True
    return False

def add_flair(submission):
    # Add flair to post
    submission.flair.select("Post Removed")

def remove_post(submission):
    # Remove post from subreddit
    submission.mod.remove()
    
def check_submissions():
    # Check submissions in subreddits for blacklisted words and remove posts if found
    for subreddit in subreddits:
        for submission in reddit.subreddit(subreddit).new():
            if check_for_blacklisted_words(submission.title, submission.selftext):
                add_flair(submission)
                remove_post(submission)
