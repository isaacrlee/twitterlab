import json
import re
from  host import *
from getCategorys import *
from  presntorAndNominee import *
from winner import *
from webScarping import *
from reTweets import *
data = json.load(open('gg2018.json'))

getHostTwitterHandle(data)
print("\n")
getHostName(data)
print("\n")
print("Categorys Found:")
print("\n")
categorys=getCategorys(data)

for text in categorys:
    print(text)
    print("\n")

testList = find_matching_tweets_from_data(".(?i)*present.*", data)

#getPresenter("Best Director",testList, "Presenter", .1, "Golden Globe")

for text in categorys:
    getXFeature(text,testList,"Presenter",.1, "Golden Globe")
    print("\n")

nomineesList = find_matching_tweets_from_data(".(?i)*(nominated|nominee|won|win|lose|lost).*", data)
#getPresenter("Best Animated",nomineesList, "Nominees", .1, "Golden Globe")

for text in categorys:
    getXFeature(text,nomineesList, "Nominees", .1, "Golden Globe")
    print("\n")

winnerList = find_matching_tweets_from_data(".(?i)*(won|win|congratulations).*", data)

for text in categorys:
    getWinner(text,winnerList, "Golden Globe")
    print("\n")

print("Now Used Scrape Data to find winners, presenters, and nominees.")
categories= scrape_award_categories()

movieCategories = categories['motion_picture_awards']
tvCategoires = categories['tv_awards']



for text in movieCategories:
	text=text.replace("– Motion Picture ","")
	text=text.replace("– Motion Picture","")
	getXFeature(text,testList,"Presenter",.1,"Golden Globe")
	print("\n")

for text in tvCategoires:
	text=text.replace("– Motion Picture ","")
	text=text.replace("– Motion Picture","")
	getXFeature(text,testList,"Presenter",.1,"Golden Globe")
	print("\n")


for text in movieCategories:
	text=text.replace("– Motion Picture ","")
	text=text.replace("– Motion Picture","")
	getXFeature(text,nomineesList,"Nominees",.1,"Golden Globe")
	print("\n")

for text in tvCategoires:
	text=text.replace("– Motion Picture ","")
	text=text.replace("– Motion Picture","")
	getXFeature(text,nomineesList,"Nominees",.1,"Golden Globe")
	print("\n")


for text in movieCategories:
	text=text.replace("– Motion Picture ","")
	text=text.replace("– Motion Picture","")
	getWinner(text,winnerList,"Golden Globe")
	print("\n")

for text in tvCategoires:
	text=text.replace("– Motion Picture ","")
	text=text.replace("– Motion Picture","")
	getWinner(text,winnerList,"Golden Globe")
	print("\n")

print("Try to get best dressed at the event")
print("\n")
bestDress=getXFeature("Best Dressed", data, "Who People thought", .1, "Golden Globe")

print("Looking at top ReTweets to see notable moments:")
print("Tweets with over 2000 retweets")
print('\n')

toptweetList=getRetweetsAboveX(data,2000)

for retweet in toptweetList:
    print(retweet)
    print('\n')


print("Most Retweeted tweet")
print('\n')


topTweet = getTopRetweet(data)

print(topTweet)
