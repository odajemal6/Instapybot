from instapy import InstaPy
from instapy import smart_run
from secrets import insta_username, insta_password
from random import randint, choice
session = InstaPy(
    username = insta_username,
    password = insta_password,
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
        'habeshaladies'
        ]
location = [
        '1803190983301422/haile-hotels-and-resorts/',
        '292006909/nazareth-shewa-ethiopia/',
        '598461275/adama-shewa-ethiopia/',
        '220596416/addis-ababa-ethiopia/'
        ]
with smart_run(session):
    # General setting
    session.set_do_like(enabled=True, percentage=70)
    session.set_do_follow(enabled=True, percentage=25)
    session.set_relationship_bounds(enabled=True,
                 potency_ratio=1.34,
                  delimit_by_numbers=True,
                   max_followers=3000,
                    max_following=4490,
                     min_followers=100,
                      min_following=300,
                       min_posts=0,
                max_posts=1000)
    # Liking
    # Like posts based on hashtags
    session.like_by_tags(tags, amount=1000)
    session.like_by_locations(location, amount=1000, randomize=True)
