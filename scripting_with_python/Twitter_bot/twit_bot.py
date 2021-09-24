# First we are gonna install a 3rd party library called 'tweepy' for this twitter bot.
import tweepy
import time

auth = tweepy.OAuthHandler('vgSMpAUM***************', 'RCIpYRyp4QX4HQor2f6FO*************')
auth.set_access_token('4365645314-ayXWOr3HkHCDS******************', 'wQQ3OmHdudxZY8pIL8uKx***********************')

api = tweepy.API(auth)

public_tweets = api.home_timeline()  # To print whatever is on your twitter home page.
for tweet in public_tweets:
    print(tweet.text)

# Some calls which we can do with tweepy library.

user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)

# Upper code copied from tweepy website.

# Generous Bot (It will help us to follow back our followers)

# This is necessary to pause this program for 1000ms = 1s. So, that we don't hit twitter's API. And don't crash it.


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    if follower.name == 'EwwFeelinqs':
        follower.follow()
        break

# Auto likes

search_string = 'life'
numbers_of_tweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbers_of_tweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
