import json
import re

def getCategorys(data):
	r=re.compile(".*(?i)nominated for best.*")
	categoryList = []
	for tweet in data:
	    if(bool(r.match(tweet.get('text')))):
	        categoryList.append(tweet)
	combineList = []
	for tweet in categoryList:
	    r=re.compile("(?i)best .*")
	    text=tweet.get('text')
	    text=r.findall(text)
	    combineList.append(text[0])
	#print(len(combineList))
	#print(len(categoryList))
	bestBlankList=[]
	for tweet in combineList:
	    r=re.compile("[?.,!-#'@].*")
	    text=r.findall(tweet)
	    if len(text)!=0:
	        bestBlankList.append(tweet.replace(text[0], '', 1))
	#bestBlankList[0]
	nonEmptyBlankList=[]
	for tweet in bestBlankList:
	    r=re.compile(".*http[s]?://.*")
	    if(not bool(r.match(tweet))):
	        nonEmptyBlankList.append(tweet.lower().rstrip())
	#len(nonEmptyBlankList)
	#nonEmptyBlankList[0]
	finalCategoryList=eliminatingCommonWords(checkReliabiltiy(nonEmptyBlankList))
	replacingIn=[]
	for tweet in finalCategoryList:
	    noInATweet=tweet.replace(" in a ", " - ")
	    noInTweet=noInATweet.replace(" in ", " - ")
	    endingIn=re.sub(' in$', '',noInTweet)
	    replacingIn.append(endingIn.title())
	replacingIn=set(replacingIn)
	#len(replacingIn)
	return replacingIn

def checkReliabiltiy(givenList, threshold=.0015):
	mentions = 0
	total = float(len(givenList))
	finalCategoryList=[]
	for tweet in givenList:
	    bestStatement = tweet
	    #print(bestStatement)
	    egExpres=".*"+bestStatement+".*"
	    try:
	        r=re.compile(egExpres)
	        for tweet2 in givenList:
	            if(bool(r.match(tweet2))):
	                mentions+=1
	        if((mentions/total)>=threshold):
	            finalCategoryList.append(bestStatement)
	        mentions = 0
	    except re.error:
	        mentions = 0
	return finalCategoryList

def eliminatingCommonWords(givenList):
	eliminatingFor=[]
	for tweet in givenList:
	    noAtTweet =re.sub(' at( |$).*', '',tweet)
	    noForTweet=re.sub(' for( |$).*', '',noAtTweet)
	    noAndTweet=re.sub(' and( |$).*', '',noForTweet)
	    noIsTweet=re.sub(' is( |$).*', '',noAndTweet)
	    noOfTweet=re.sub(' of( |$).*', '',noIsTweet)
	    noButTweet=re.sub(' but( |$).*', '',noOfTweet)
	    noSoTweet=re.sub(' so( |$).*', '',noButTweet)
	    noYetTweet=re.sub(' yet( |$).*', '',noSoTweet)
	    noTheTweet=re.sub(' the( |$).*', '',noYetTweet)
	    noCategoryTweet=re.sub(' category( |$).*', '',noTheTweet)
	    noThisTweet=re.sub(' this( |$).*', '',noCategoryTweet)
	    noTonightTweet=re.sub(' tonight( |$).*', '',noThisTweet)
	    if(noTonightTweet!="best"):
	        eliminatingFor.append(noTonightTweet)
	eliminatingFor=set(eliminatingFor)
	return eliminatingFor
	#len(eliminatingFor)