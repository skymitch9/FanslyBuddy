from reddit.subreddit_list import SUBREDDITS

class UserFlair:
    def __init__(self, reddit):
        self.reddit = reddit

    def add_flair(self):
        """
        Add flair to approved users in specified subreddits
        """
        for subreddit_name in SUBREDDITS:
            subreddit = self.reddit.subreddit(subreddit_name)
            for comment in subreddit.comments(limit=50):
                if comment.author_flair_text is None and comment.approved:
                    flair_text = 'Approved User'
                    subreddit.flair.set(comment.author, flair_text, '')
