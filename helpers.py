import re


def find_matching_tweets_from_data(regex, source):
    # source is a list tweet objects, regex is the pattern to match
    returnList = []
    r = re.compile(regex)
    for tweet in source:
        # print(tweet)
        text = tweet.get('text')
        # print(text)
        if(bool(r.match(text))):
            returnList.append(text)
    return returnList


def find_matching_tweets(regex, source):
    # source is a list of strings, regex is the pattern to match
    returnList = []
    r = re.compile(regex)
    for tweet in source:
        # print(tweet)
        # text = tweet.get('text')
        # print(text)
        tweet = r.findall(tweet)
        returnList.append(tweet)
    return returnList
