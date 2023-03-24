import praw
from reddit.reddit_api_credentials import SUBREDDITS_TO_MONITOR
from reddit.reddit_api_credentials import USER_AGENT
from reddit.reddit_oauth_credentials import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD

def test_moderator():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=USERNAME,
        password=PASSWORD,
        user_agent=USER_AGENT,
    )

    for subreddit_name in SUBREDDITS_TO_MONITOR:
        subreddit = reddit.subreddit(subreddit_name)

        for post in subreddit.new(limit=50):
            if post.author == reddit.user.me():
                continue
            print(f"Checking post {post.id} in subreddit {subreddit_name}")
            check_keywords(post)

def check_keywords(post):
    title = post.title.lower()
    body = post.selftext.lower()
    if any(keyword in title or keyword in body for keyword in KEYWORDS_TO_MONITOR):
        print(f"Post {post.id} matches keyword in title or body")

def test_check_keywords():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=USERNAME,
        password=PASSWORD,
        user_agent=USER_AGENT,
    )

    subreddit = reddit.subreddit("test")

    post = subreddit.submit(
        "Test post with keyword",
        selftext="This post contains the word python",
        send_replies=False,
    )

    check_keywords(post)

    post.delete()

if __name__ == "__main__":
    test_moderator()
    test_check_keywords()
