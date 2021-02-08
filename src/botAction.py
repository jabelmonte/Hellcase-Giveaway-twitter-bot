import tweepy
import time
from log import Log
from Keys import Keys

filepath = "../logs/seentweetslog.txt"
key = Keys()
pullKeys = key.getKeys()
logs = Log()

consumer_key = pullKeys['a']
consumer_secret = pullKeys['b']
access_token = pullKeys['c']
access_token_secret = pullKeys['d']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def scantweet():

    #auto follow every follower first
    for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

    tweets = api.mentions_timeline(logs.readLog(filepath), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#letsgonow09'in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + "@ADSFGHJOLO" + " " + "@gibblehayo" + " " + "@greenmalware", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            logs.storeLog(filepath, tweet.id)

while True:
    scantweet()
    time.sleep(20)