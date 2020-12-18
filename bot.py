from instapy import InstaPy
from instapy import smart_run
from secrets import insta_username, insta_password
from random import randint, choice
from time import sleep
session = InstaPy(
    username = insta_username,
    password = insta_password,
    headless_browser=False
)

def likes():
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    location = choice(num)
    feed = randint(1, 2)
    intra = randint(1, 6)
    tag = randint(1, 6)
    session.set_do_like(enabled=True, percentage=70)
    session.like_by_feed(amount=feed, randomize=True, unfollow=False, interact=False)
    sleep(120)
    session.set_user_interact(amount=intra, randomize=True, percentage=100, media='Photo')
    session.like_by_tags(['habesha', 'et', 'oro', 'nazu', 'addis', 'adama'], amount=tag, interact=True)
    sleep(120)

def comment():
    session.set_do_comment(enabled=True, percentage=75)
    session.set_comments([])
    session.comment_by_locations([''], amount=5)

def follow():
    session.set_do_follow(enabled=True, percentage=25, times=2)
    session.follow_commenters(['noah_n18_', 'nahom_legesse', 'robsan_hmt'], amount=3, daysold=365, max_pic=6, sleep_delay=600, interact=False)
    session.follow_likers(['noah_n18_', 'nahom_legesse'], photos_grab_amount=2, follow_likers_per_photo=2, randomize=True, sleep_delay=600, interact=False)
    session.follow_user_followers(['nahom_legesse', 'noah_n18_', 'robsan_hmt'], amount=10, randomize=True, sleep_delay=60)

with smart_run(session):
    follow()