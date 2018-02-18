import json
import re

data = json.load(open('gg2018.json'))
def getRetweetsAboveX(givenList, xValue):
	r=re.compile("RT.*")
	reTweetDict={}
	maxReTweetTimes=0
	maxReTweet="nothing"
	bigReTweets=[]
	for tweet in data:
	    key=tweet.get('text')
	    if(bool(r.match(key))):
	        if key in reTweetDict:
	            reTweetDict[key] += 1
	        else:
	            reTweetDict[key] = 1
	        if reTweetDict[key]>xValue:
	            bigReTweets.append(key)
	bigReTweets=set(bigReTweets)
	return bigReTweets
	#print(len(bigReTweets))


def getTopRetweet(givenList):
	r=re.compile("RT.*")
	reTweetDict={}
	maxReTweetTimes=0
	maxReTweet="nothing"
	bigReTweets=[]
	for tweet in data:
	    key=tweet.get('text')
	    if(bool(r.match(key))):
	        if key in reTweetDict:
	            reTweetDict[key] += 1
	        else:
	            reTweetDict[key] = 1
	        if reTweetDict[key]>maxReTweetTimes:
	            maxReTweetTimes=reTweetDict[key]
	            maxReTweet=key
	bigReTweets=set(bigReTweets)
	return maxReTweet
	#print(len(bigReTweets))


#print("Tweets with over 2000 retweets")
#print('\n')

#toptweetList=getRetweetsAboveX(data,2000)

#for retweet in toptweetList:
#    print(retweet)
#    print('\n')


#print("Most Retweeted tweet")
#print('\n')


#topTweet = getTopRetweet(data)

#print(topTweet)