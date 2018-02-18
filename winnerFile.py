import json
import re
from helpers import *

def topName(listNames):
    maxAmount=0
    maxItem="No Information"
    r=re.compile(".(?i)*the( |$)")
    total=float(len(listNames))
    nameDict={}
    for tweetName in listNames:
        for name in tweetName:
            key=name[0]
            if key in nameDict:
                nameDict[key] += 1
            else:
                nameDict[key] = 1
    answer=[]
    for item in nameDict.items():
        if item[1]>= maxAmount:
            maxItem=item[0]
            maxAmount=item[1]
    return maxItem



def getWinner (category, tweets, award, run=1):
    winnerList = find_matching_tweets_from_data(".(?i)*"+category+"*", tweets)
    winListWithoutCategory=[]
    for tweet in winnerList:
        winListWithoutCategory.append(eliminate_common_words(tweet,category,award))
    names=[]
    #print(winnerList)
    names=find_matching_tweets("([A-Z|@]['|.|\w-]*(\s+[of|A-Z]['|.|\w-]*)+)", winListWithoutCategory)
    nameCheck=topName(names)
    print("The winner of " +category+" is:")
    print(nameCheck)

def getWinnerHashtag(category, tweets, award):
    award_tweets = find_matching_tweets_from_data("(?i).*" + category + ".*", tweets)
    award_tweets_without_common_words = [eliminate_common_words(tweet,category,award) for tweet in award_tweets]
    hashtags_in_award_tweets = find_matching_tweet_parts("(?i)#\w+", award_tweets_without_common_words)
    d = mostCommonD(hashtags_in_award_tweets)
    if "#s" in d:
        del d["#s"]
    if "#Golde" in d:
        del d["#Golde"]
    if "#goldenglobes" in d:
        del d["#goldenglobes"]
    winner_hashtag = max(d, key=d.get) if d else "No Information"
    print(winner_hashtag)