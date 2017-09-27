#!/usr/bin/env python3

import tweepy
import json

#put your information here
access_keys = {'consumer_key':'',
            'consumer_secret':'',
            'access_token':'',
            'access_token_secret':''}

def get_timeline(screen_name, count):
    """
    Function to download the latest tweets from a twitter profile

    Parameters:
    -----------
    screen_name: str
        name of a twitter profile you want to downlaod tweets. Ex: @guilhermeslcs
    count: int 
        number of tweets you want to get

    Returns:
    --------
    None:
        Nothing is returned in this function. It just saves the tweets as json
    """
    #authorization operations
    auth = tweepy.OAuthHandler(access_keys['consumer_key'], access_keys['consumer_secret'])
    auth.set_access_token(access_keys['access_token'],access_keys['access_token_secret'])
    api = tweepy.API(auth)
    
    #get the 'count' most recent tweets from screen_name
    new_tweets = api.user_timeline(screen_name = screen_name,count=count)
    
    #writing information as json
    write_json = open('tweets.json', 'w')
    for tweet in new_tweets:
        json.dump(tweet._json,write_json,indent = 4)
    
    write_json.close()

if __name__ == '__main__':
    get_timeline('@realDonaldTrump', 200)
