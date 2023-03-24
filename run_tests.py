import reddit_test
import reddit_oauth_credentials

# create the Reddit API instance using OAuth credentials
reddit = reddit_oauth_credentials.create_reddit_instance()

# run the test functions
reddit_test.test_moderator(reddit)
reddit_test.check_keywords(reddit)
reddit_test.test_check_keywords(reddit)
