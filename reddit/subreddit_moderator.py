from reddit.subreddit_list import SUBREDDITS
from reddit.allowlist_keywords import ALLOWLIST_KEYWORDS
from reddit.denylist_keywords import DENYLIST_KEYWORDS

class SubredditModerator:
    def __init__(self, reddit):
        self.reddit = reddit

    def check_keywords(self, post):
        """
        Check if post contains any denied or allowed keywords
        """
        title = post.title.lower()
        selftext = post.selftext.lower()
        
        for keyword in DENYLIST_KEYWORDS:
            if keyword in title or keyword in selftext:
                post.mod.remove()
                post.mod.send_removal_message()
                return
        
        for keyword in ALLOWLIST_KEYWORDS:
            if keyword in title or keyword in selftext:
                post.mod.approve()
                return
        
        post.mod.remove()
        post.mod.send_removal_message()

    def moderate_subreddits(self):
        """
        Moderate posts in specified subreddits
        """
        for subreddit_name in SUBREDDITS:
            subreddit = self.reddit.subreddit(subreddit_name)
            for post in subreddit.new(limit=50):
                self.check_keywords(post)
