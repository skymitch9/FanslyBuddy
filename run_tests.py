import reddit_test
import reddit_oauth_credentials

SUBREDDIT_NAME = "fansly"

# create the Reddit API instance using OAuth credentials
reddit = reddit_oauth_credentials.create_reddit_instance()

# run the test functions
reddit_test.test_moderator(reddit)
reddit_test.check_keywords(reddit)
post = next(reddit.subreddit(SUBREDDIT_NAME).new(limit=1))
reddit_test.test_check_keywords(reddit)
