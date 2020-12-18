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
    username = insta_username,
    password = insta_password,
    headless_browser=False
)

for i in range(3):
    with smart_run(session):
        #session.unfollow_users(amount=40, nonFollowers=True, style="RANDOM", unfollow_after=42 * 60 * 60, sleep_delay=655)
        session.like_by_locations(['107083800725738'], amount=2, skip_top_posts=True, randomize=True)
        session.set_do_comment(enabled=True, percentage=25)
        session.set_comments([comments])
        session.comment_by_locations(['107083800725738'], amount=17)
        session.follow_user_followers(['nahom_legesse', 'noah_n18_', 'robsan_hmt'], amount=10, randomize=True, sleep_delay=60)
        session.like_by_feed(amount=10, randomize=True, unfollow=True, interact=True)


