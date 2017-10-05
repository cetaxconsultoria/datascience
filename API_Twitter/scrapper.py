#!/usr/bin/env python3

import tweepy
import json

def tweets_to_json(iterator, file_name):
    """
    Function used in order to save the requested iterator as json format. Usually used to
    save tweets and all its features.

    Parameters:
    -----------
    iterator (obj):
        some iterator like items, list, etc, to be saved as json.
    file_name (str):
        this will be the name of the file that will be saved

    Returns:
    -------
    true (bool):
        this function returns True if everything went fine
    exception (obj):
        raises an exception if something went wrong
    """
    try:
        for tweet in iterator:
            tweet_id = tweet._json["id_str"]
            write_json = open(tweet_id+".json", 'w')
            json.dump(tweet._json,write_json,indent = 4)
            write_json.close()
    except:
        raise

    return True

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
    access_keys = {'consumer_key':'zjv8UWDY1T4czSg8BwLapZFix',
                 'consumer_secret':'a7stKtlP53R2Z4AoOsCsEtozCh3T1EyUNnmBvAww10kh0hzShH',
                 'access_token':'129634628-9wRTqDFRsgUAGdNkSwIHprRUo6EuEmSHE3fQibYx',
                 'access_token_secret':'8buBHopCDwuMBKlu3z97OFdM5ywNnJyk0mV86D1CCl7vk'}

    #authorization operations
    try:
        auth = tweepy.OAuthHandler(access_keys['consumer_key'], access_keys['consumer_secret'])
        auth.set_access_token(access_keys['access_token'],access_keys['access_token_secret'])
        return tweepy.API(auth)
    except:
        raise

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
    try:
        new_tweets = api.user_timeline(screen_name = screen_name,count=count)
    except:
        raise
    #writing information as json
    tweets_to_json(new_tweets,'timeline_tweets.json')

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
    try:
        tweets = tweepy.Cursor(api.search, q=search_key).items(count)
    except:
        raise

    tweets_to_json(tweets,'searh_tweets.json')

if __name__ == '__main__':
    #get_timeline('@realDonaldTrump', 200)
    get_search('lollapalooza',200)
