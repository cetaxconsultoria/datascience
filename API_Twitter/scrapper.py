#!/usr/bin/env python3

import tweepy
import json

def get_api():
    """
    This function is used to construct a api object based on tokens and keys

    Parameters:
    -----------
    None
        All the info needed are listed in the dict below

    Returns:
    --------
    api (obj):
        returns api, a object used to obtain information from twitter
    """

    #put your information here
    access_keys = {'consumer_key':'',
                    'consumer_secret':'',
                    'access_token':'',
                    'access_token_secret':''}

    #authorization operations
    auth = tweepy.OAuthHandler(access_keys['consumer_key'], access_keys['consumer_secret'])
    auth.set_access_token(access_keys['access_token'],access_keys['access_token_secret'])
    return tweepy.API(auth)

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
    api = get_api()
    
    #get the 'count' most recent tweets from screen_name
    new_tweets = api.user_timeline(screen_name = screen_name,count=count)
    
    #writing information as json
    write_json = open('tweets.json', 'w')
    for tweet in new_tweets:
        json.dump(tweet._json,write_json,indent = 4)
    
    write_json.close()

def get_search(search_key, count):
    """
    Funtion to get tweets from a search of a key word

    Parameters:
    ----------
    search_key (str): 
        the word or text you want to search tweets
    count (int):
        number of tweets you want to be listed

    Returns:
    --------
    None
        Nothing is returned. Just a json file is saved with tweets
    """
    api = get_api()
    tweets = tweepy.Cursor(api.search, q=search_key).items(count)

    write_json = open('tweets.json', 'w')
    for tweet in tweets:
        json.dump(tweet._json,write_json,indent = 4)
    
    write_json.close()


if __name__ == '__main__':
    #get_timeline('@realDonaldTrump', 200)
    get_search('lollapalooza',1)
