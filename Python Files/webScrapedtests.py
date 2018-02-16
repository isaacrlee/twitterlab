import json
import re
from host import *
from getCategorys import *
from presntorAndNominee import *
from webScarping import *
from winner import *

tweetData = json.load(open('gg2018.json'))


categories= scrape_award_categories()

movieCategories = categories['motion_picture_awards']
tvCategoires = categories['tv_awards']

testList = find_matching_tweets_from_data(".(?i)*present.*", tweetData)


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


nomineesList = find_matching_tweets_from_data(".(?i)*(nominated|nominee|won|win|lose|lost).*", tweetData)


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


winnerList = find_matching_tweets_from_data(".(?i)*(won|win|congratulations).*", tweetData)

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
