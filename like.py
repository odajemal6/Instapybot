from instapy import InstaPy
from instapy import smart_run
from secrets import insta_username, insta_password

session = InstaPy(
    username=insta_username,
    password=insta_password,
    headless_browser=False
)


def like():
    session.set_do_like(enabled=True, percentage=70)
    session.like_by_tags([
        'like4like', 'liking', 'likeall', 'likeforlike',
        'likes4likes', 'love', 'instagood', 'tagblender',
        'likesforlikes', 'ilikeback', 'liketeam', 'liker',
        'ilike', 'likealways', 'likebackteam', 'ilikeyou',
        'ilikeit', 'likeme', 'tflers', 'likes', 'likesback',
        'photooftheday', 'likesforlike', 'iliketurtles',
        'likes4followers', 'likemeback', 'ilu'
        'likesreturned', 'l4l'
    ], amount=100)


with smart_run(session):
    like()
