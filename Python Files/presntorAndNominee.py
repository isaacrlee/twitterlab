import json
import re
from helpers import *

def nameReliability(listNames, threshold):
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
        if (item[1]/total)>= threshold and (not(bool(r.match(item[0])))) and len(item[0].split())<4:
            answer.append(item[0])
        if item[1]>= maxAmount:
            maxItem=item[0]
            maxAmount=item[1]
    if (len(answer)==0):
        answer.append(maxItem)
    return answer



def getXFeature (category, tweets, feature, threshold, award, run=1):
	
	presentorList = find_matching_tweets_from_data(".(?i)*"+category+"*", tweets)
	wordsToIgnore=category.split()
	presentListWithoutCategory=[]
	for tweet in presentorList:
		presentListWithoutCategory.append(eliminate_common_words(tweet,category,award))
	names=find_matching_tweets("([A-Z|@]['|.|\w-]*(\s+[A-Z]['|.|\w-]*)+)", presentListWithoutCategory)
	nameCheck=nameReliability(names,threshold)
	print(feature+"(s) for " +category+" are:")
	for item in nameCheck:
		print(item)
