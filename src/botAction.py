import tweepy
import time
import random
from log import Log
from Keys import Keys

filepath = "../logs/seentweetslog.txt"
commentspath = "../logs/comments.txt"
key = Keys()
pullKeys = key.getKeys()
logs = Log()

consumer_key = pullKeys['a']
consumer_secret = pullKeys['b']
access_token = pullKeys['c']
access_token_secret = pullKeys['d']
mentioned = pullKeys['e']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# hashtag1 = "#kingkongwillwin"
# hashtag2 = "#kingkongflip"
tweetCount = 5
followerCount = 10

def scantweet():
    #auto follow every follower first
    # for follower in tweepy.Cursor(api.followers).items(followerCount):
    #     follower.follow()

    tweets = tweepy.Cursor(api.search, q='#hellcase AND #csgo').items(tweetCount)

    for tweet in tweets:
        try:
            commentpick = open(commentspath).read().splitlines()
            randComment = random.choice(commentpick)
            time.sleep(10)
            api.retweet(tweet.id)
            print('retweet success!')
            time.sleep(9)
            api.create_favorite(tweet.id)
            print('favorite success!')
            time.sleep(14)
            api.update_status("@" + tweet.user.screen_name + randComment + mentioned, tweet.id)
            print('comment success!')
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(30)

    # tweets = api.mentions_timeline(logs.readLog(filepath), tweet_mode='extended')
    # tweets = api.search('#kingkongwillwin', logs.readLog(filepath), tweet_mode='extended')
    # for tweet in reversed(tweets):
    #     if '#kingkongwillwin'in tweet.full_text.lower():
    #         print(str(tweet.id) + ' - ' + tweet.full_text)
    #         api.update_status("@" + tweet.user.screen_name + " Hello human! ", tweet.id)
    #         api.create_favorite(tweet.id)
    #         api.retweet(tweet.id)
    #         logs.storeLog(filepath, tweet.id)


while True:
    scantweet()