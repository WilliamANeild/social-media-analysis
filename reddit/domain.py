from praw.models import Submission
from pydantic import BaseModel


class RedditPost(BaseModel):
    title: str
    text: str
    subreddit: str


    @classmethod
    def valid_submission(cls, submission: Submission):
        if submission.selftext:
            return True
        return False
    
    @classmethod
    def from_submission(cls, submission: Submission):
        return cls(title=submission.title, text=submission.selftext, subreddit=submission.subreddit.display_name)

    
    def get_all_text(self):
        return self.title + " " + self.text