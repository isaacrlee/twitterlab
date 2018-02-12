import json
import re


# Gets the twitter handle of people tweeting about the hosting job
def getHostTwitterHandle(data):
	r=re.compile(".(?i)*host.*")
	hostList = []
	for tweet in data:
	    if(bool(r.match(tweet.get('text')))):
	        hostList.append(tweet)
	#print(len(hostList))
	r=re.compile(".*(?i)job.*")
	jobAsHost = []
	for tweet in hostList:
	    if(bool(r.match(tweet.get('text')))):
	        jobAsHost.append(tweet)
	#print(len(jobAsHost))
	r=re.compile("@.*")
	startwithHandle = []
	for tweet in jobAsHost:
	    if(bool(r.match(tweet.get('text')))):
	        startwithHandle.append(tweet)
	#print(len(startwithHandle))
	maxMentions=0
	mentions=0
	maxMentionName=""
	for tweet in startwithHandle:
	    text=tweet.get('text')
	    name=text.split(' ', 1)[0]
	    for tweet in startwithHandle:
	        egExpres=".*"+name+".*"
	        r=re.compile(egExpres)
	        if(bool(r.match(tweet.get('text')))):
	            mentions+=1
	    if(mentions>maxMentions):
	        maxMentions=mentions
	        maxMentionName=name
	    mentions=0
	print("Host Twitter Handle")
	print(maxMentionName)

#Gets the name of the host by looking at hositng job and most common first two words
def getHostName(data):
	r=re.compile(".*hosting.*")
	hostingList = []
	for tweet in data:
	    if(bool(r.match(tweet.get('text')))):
	        hostingList.append(tweet)

	r=re.compile(".*job.*")
	sethList = []
	for tweet in hostingList:
	    if(bool(r.match(tweet.get('text')))):
	        sethList.append(tweet)
	#print(len(sethList))
	maxMentions=0
	mentions=0
	maxMentionName=""
	for tweet in sethList:
	    text=tweet.get('text')
	    name=text.split(' ', 1)[0]+' '+text.split(' ')[1]
	    for tweet2 in sethList:
	        egExpres=".*"+name+".*"
	        r=re.compile(egExpres)
	        if(bool(r.match(tweet2.get('text')))):
	            mentions+=1
	    if(mentions>maxMentions):
	        maxMentions=mentions
	        maxMentionName=name
	    mentions=0
	#print(maxMentions)
	print("Host Name:")
	print(maxMentionName)
