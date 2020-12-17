from instapy import InstaPy
from instapy import smart_run
from secrets import insta_username, insta_password


comments = [
    'Nice shot!',
    'cooooool',
    'Like your post',
    'awesome'
]

session = InstaPy(
    username= insta_username,
    password= insta_password,
    headless_browser=False
)

for i in range(3):
    with smart_run(session):
        session.like_by_locations(['224442573'], amount=5, skip_top_posts=False, randomize=True)
        session.follow_user_followers(['friend', 'friend2'], amount=20, randomize=False, sleep_delay=60)
        session.like_by_feed(amount=10, randomize=True, unfollow=True, interact=True)

session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
