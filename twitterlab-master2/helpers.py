import re


def find_matching_tweets_from_data(regex, source):
    # source is a list tweet objects, regex is the pattern to match
    returnList = []
    r = re.compile(regex)
    for tweet in source:
        text = tweet.get('text')
        # print(text)
        if(bool(r.match(text))):
            returnList.append(tweet)
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

def eliminate_common_words(tweet, feature, award):
    awardSave=award
    awardPlural=award+'s'
    awardNoSpace=award=award.replace(' ','')
    awardNoSpacePlural=awardNoSpace+'s'
    wordsToIgnore=feature.split()
    text=tweet.get('text')
    for word in wordsToIgnore:
        if (word.istitle()):
            text=text.replace(word,"")
            text=text.replace(word.lower(),"")
    text=text.replace("Motion","")
    text=text.replace("Picture","")
    text=re.sub(awardSave, '',text)
    text=re.sub(awardPlural, '',text)
    text=re.sub(awardNoSpace, '',text)
    text=re.sub(awardNoSpacePlural, '',text)
    return text

def find_matching_tweet_parts(regex, source):
    # source is a list of strings, regex is the pattern to match
    returnList = []
    r = re.compile(regex)
    for tweet in source:
        # print(tweet)
        returnList += (re.findall(r, tweet))
    return returnList

def mostCommonD(source):
    # returns dictionary with number of occurences for each string in source (useful for lists of hashtags/handles)
    d = {}
    for tweet in source:
        if tweet in d:
            d[tweet] += 1
        else:
            d[tweet] = 1
    return d