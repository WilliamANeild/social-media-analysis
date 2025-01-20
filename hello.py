from reddit.domain import RedditPost
from reddit.service import RedditService
from flytekit import task, workflow


@task
def get_posts(search_term: str) -> list[RedditPost]:
    return RedditService().get_posts(search_term=search_term, limit=2)
    


@workflow
def reddit_wf(search_term: str) -> list[RedditPost]:
    res = get_posts(search_term=search_term)
    return res


if __name__ == "__main__":
    print(f"Running wf() {reddit_wf(search_term='NVDA')}")
