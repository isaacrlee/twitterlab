

from helpers import *

# Gets the twitter handle of people tweeting about the hosting job
def getHostTwitterHandle(data):
    hostList = find_matching_tweets_from_data('.(?i)*host.*', data)
    # print('len(hostList): ' + str(len(hostList)))
    jobAsHost = find_matching_tweets_from_data('.*(?i)job.*', hostList)
    # print('len(jobAsHost): ' + str(len(jobAsHost)))
    startwithHandle = find_matching_tweets_from_data('@.*', jobAsHost)
    # print('len(startwithHandle): ' + str(len(startwithHandle)))
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
    print("Host Twitter Handle: " + maxMentionName)


# Gets the name of the host by looking at hositng job and most common first two words
def getHostName(data):
    hostingList = find_matching_tweets_from_data('.*hosting.*', data)
    sethList = find_matching_tweets_from_data('.*job.*', hostingList)
    # print(len(sethList))
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
    # print(maxMentions)
    print("Host Name: " + maxMentionName)

# getHostTwitterHandle(data)
# getHostName(data)