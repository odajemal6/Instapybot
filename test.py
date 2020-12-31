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

def follow():
    session.set_relationship_bounds(enabled=True, potency_ratio=None, delimit_by_numbers=True, max_followers=1000, max_following=900, min_followers=100, min_following=100)
    session.follow_by_tags([
        'nazret', 'nazreth', 'nazrēt', 'habeshakonjo', 'habeshawit', 'followforfollowback', 'python_coder2000', 'python_developer', 'python_proglib', 'djangoframework', 'oromo', 'habeshavibe'
    ], amount=1
    )
    
    
    session.set_user_interact(amount=3,
                 percentage=32,
                  randomize=True,
                   media='Video')
    session.follow_commenters(['liya__solomon', 'mafihela', 'asset_east', 'kidus_gech', 'eya_ye_hena'], amount=2, daysold=365, max_pic = 100, sleep_delay=600, interact=True)

def interact():
    session.set_user_interact(amount=3, randomize=True, percentage=50, media='Photo')
    session.set_do_follow(enabled=True, percentage=35)
    session.set_do_like(enabled=True, percentage=70)
    session.set_comments([comments])
    session.set_do_comment(enabled=True, percentage=80)
    session.interact_user_followers(['robsan_hmt'], amount=10, randomize=True)

def likes():
    session.like_by_tags([
        'nazret', 'nazreth', 'nazrēt', 'habeshakonjo', 'habeshawit', 'followforfollowback', 'python_coder2000', 'python_developer', 'python_proglib', 'djangoframework'
    ], amount=10)
    
    
    

def unfollow():
    session.unfollow_users(amount=20, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)



with smart_run(session):
    #likes()
    #interact()
    follow()

