from instapy import InstaPy
from instapy import smart_run
from secrets import insta_username, insta_password
from random import randint, choice
session = InstaPy(
    username=insta_username,
    password=insta_password,
    headless_browser=False
)
comments = [
    'Nice shot!',
    'cooooool',
    'Like your post',
    'awesome'
]
tags = ['habeshabeauty', 'habesha', 'ethiopia', 'ethiopian', 'eth',
        'habeshastyle', 'habeshaparty', 'reviewethio', 'habeshafashion',
        'ethiopianstyle', 'habeshakonjo', 'habeshan', 'habeshanbeauty',
        'habeshaladies', 'oromo', 'oromobeauty', 'oromoculture',
        'oromogirl', 'oromoo', 'oromolove', 'oromopride', 'oromowomen',
        'oromofirst'
liketag = ['like4like', 'liking', 'likeall', 'likeforlike',
        'likes4likes', 'love', 'instagood', 'tagblender',
        'likesforlikes', 'ilikeback', 'liketeam', 'liker',
        'ilike', 'likealways', 'likebackteam', 'ilikeyou',
        'ilikeit', 'likeme', 'tflers', 'likes', 'likesback',
        'photooftheday', 'likesforlike', 'iliketurtles',
        'likes4followers', 'likemeback', 'ilu'
        'likesreturned', 'l4l']

location = [
    '1803190983301422/haile-hotels-and-resorts/',
    '292006909/nazareth-shewa-ethiopia/',
    '598461275/adama-shewa-ethiopia/',
    '220596416/addis-ababa-ethiopia/'
]
users = [
    'eyu.g_', 'farees4real', 'f_a_r_i_s_a_b', 'Farracer_999',
    'robsan_hmt', 'nahom_legesse', 'official_naolx', 'kei__g_',
    'ethio_pure_habesha', 'official_leul', 'makbooll_a',
    'beckham7bkm', 'eyor_cawe', 'official_blackye', 
    'guyyeman', 'kena_zgreat', 'giruma__', 'kaleab__endashw'
]
with smart_run(session):
    # General setting
    session.set_blacklist(enabled=True, campaign='yada2k21')
    session.set_do_like(enabled=True, percentage=70)
    session.set_do_follow(enabled=True, percentage=25)
    session.set_do_comment(enabled=True, percentage=25)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=1000,
                                    max_following=1000,
                                    min_followers=400,
                                    min_following=500,
                                    min_posts=0,
                                    max_posts=1000)
    # Liking
    # Like posts based on hashtags
    #session.like_by_tags(tags, amount=50)
    #session.like_by_locations(location, amount=50, randomize=True)

    # Comment

    # session.set_comments(comments)

    # Follow

    # session.follow_by_locations(location, amount=100)
    session.follow_user_followers(
        users, amount=200, randomize=True, interact=True, sleep_delay=27)
    # Unfollow
    # session.unfollow_users(
    #    amount = 50, nonFollowers = True, style = "RANDOM", unfollow_after = 42*60*60, sleep_delay = 23
    # )
