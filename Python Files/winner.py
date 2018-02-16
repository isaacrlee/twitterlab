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
    names=find_matching_tweets("([A-Z|@]['|.|\w-]*(\s+[A-Z]['|.|\w-]*)+)", winListWithoutCategory)
    nameCheck=topName(names)
    print("The winner of " +category+" is:")
    print(nameCheck)