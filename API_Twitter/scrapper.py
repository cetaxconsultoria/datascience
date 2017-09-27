#!/usr/bin/env python3

import tweepy

#put your information here
access_keys = {'consumer_key':'',
            'consumer_secret':'',
            'access_token':'',
            'access_token_secret':''}

def get_timeline(screen_name, count):
    auth = tweepy.OAuthHandler(access_keys['consumer_key'], access_keys['consumer_secret'])
    auth.set_access_token(access_keys['access_token'],access_keys['access_token_secret'])
    api = tweepy.API(auth)

    new_tweets = api.user_timeline(screen_name = screen_name,count=count)

    for tweet in new_tweets:
        print(tweet.text)
        print(' ')

if __name__ == '__main__':
    get_timeline('@realDonaldTrump', 200)
