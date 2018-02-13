import json
import pprint
import re
import requests

from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter(indent=4)

data = json.load(open('gg2018.json'))


# helper functions
def find_matching_tweets_from_data(regex, source):
    # source is a list of tweet objects, regex is the pattern to match
    returnList = []
    r = re.compile(regex)
    for tweet in source:
        if(bool(r.match(tweet.get('text')))):
            returnList.append(tweet)
    return returnList


def find_matching_tweet_part(regex, source):
    # source is a list of tweet object, regex is the pattern to match, returns first matched part
    returnList = []
    r = re.compile(regex)
    for tweet in source:
        text = tweet.get('text')
        text = r.findall(text)
        returnList.append(text[0])
    return returnList


def find_matching_tweet_parts(regex, source):
    # source is a list of strings, regex is the pattern to match, returns all matched parts
    returnList = []
    r = re.compile(regex)
    for tweet in source:
        returnList += (re.findall(r, tweet))
    return returnList


def find_matching_tweets(regex, source):
    # source is a list of strings, regex is the pattern to match
    returnList = []
    r = re.compile(regex)
    for tweet in source:
        if(bool(r.match(tweet))):
            returnList.append(tweet)
    return returnList


def occurences_dict(source):
    # returns dictionary with # of occurences for each string in source (useful for lists of hashtags/handles)
    d = {}
    for tweet in source:
        if tweet in d:
            d[tweet] += 1
        else:
            d[tweet] = 1
    return d


def occurences_list(d):
    # reformats dictionary from occurences_dict into an ordered list
    sorted_list = []
    d_invert = dict(map(lambda item: (item[1], item[0]), d.items()))
    sorted_by_vals = sorted(d_invert)
    for val in reversed(sorted_by_vals):
        sorted_list.append([val, d_invert[val]])
    return sorted_list
