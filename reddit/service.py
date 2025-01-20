import praw
from praw.models import Submission
from reddit.domain import RedditPost
from settings import app_settings

class RedditService:
    def __init__(self):
        username = app_settings.REDDIT_USERNAME
        self.reddit = praw.Reddit(
            client_id=app_settings.REDDIT_CLIENT_ID,
            client_secret=app_settings.REDDIT_CLIENT_SECRET,
            user_agent=f"testscript by u/{username}",
            username=username,
            password=app_settings.REDDIT_PASSWORD,
        )

    def get_posts(self, search_term: str, limit=5, subreddit="all"):
        posts: list[RedditPost] = []
        for submission in self.reddit.subreddit(subreddit).search(search_term):
            if len(posts) >= limit:
                break
            if not RedditPost.valid_submission(submission=submission):
                continue
            posts.append(RedditPost.from_submission(submission=submission))
        return posts