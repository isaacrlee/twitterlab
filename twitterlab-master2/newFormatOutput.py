import json
import re
from host import *
from categorys import *
from presentorAndNominee import *
from winnerFile import *
from webScarping import *
from reTweetsHelpers import *
from facts import *

data = json.load(open('gg2018.json'))
newOutputWay=json.load(open('gg2018_blankformat.json'))

newOutputWay['Host']=getHostName(data)
categorys=['Best Motion Picture - Drama', 'Best Motion Picture - Musical or Comedy', 'Best Actor in a Motion Picture – Drama', 'Best Actress in a Motion Picture – Drama', 'Best Actor in a Motion Picture – Musical or Comedy', 
			'Best Actress in a Motion Picture – Musical or Comedy', 'Best Supporting Actor in a Motion Picture – Drama, Musical or Comedy', 'Best Supporting Actress in a Motion Picture – Drama, Musical or Comedy', 'Best Director', 
			'Best Screenplay', 'Best Original Score', 'Best Original Song', 'Best Animated Feature Film', 'Best Foreign Language Film', 'Best Series - Drama', 'Best Series - Musical or Comedy', 'Best Actor in a Television Series – Drama', 
			'Best Actress in a Television Series – Drama', 'Best Actor in a Television Series – Musical or Comedy', 'Best Actress in a Television Series – Musical or Comedy', 'Best Actor in a Miniseries or Television Film', 'Best Actress in a Miniseries or Television Film', 
			'Best Supporting Actor in a Series, Miniseries or Television Film', 'Best Supporting Actress in a Series, Miniseries or Television Film', 'Best Miniseries or Television Film', 'Cecil B. DeMille Lifetime Achievement Award']
presentList = find_matching_tweets_from_data(".(?i)*present.*", data)
nomineesList = find_matching_tweets_from_data(".(?i)*(nominated|nominee|won|win|lose|lost).*", data)
winnerList = find_matching_tweets_from_data(".(?i)*(won|win|congratulations).*", data)

for award in categorys:
	award2=award.replace("– Motion Picture ","")
	award2=award2.replace("– Motion Picture","")
	tempDict=newOutputWay[award]
	tempDict["Presenters"]=getXFeature(award2,presentList,"Presenter",.1,"Golden Globe")
	tempDict["Nominees"]=getXFeature(award2,nomineesList,"Nominees",.1,"Golden Globe")
	tempDict["Winner"]=getWinner(award2,winnerList, "Golden Globe")
	newOutputWay[award]=tempDict
#print(newOutputWay)
with open('newdatafromat.txt', 'w') as outfile:  
    json.dump(newOutputWay, outfile)
data = json.load(open('newdatafromat.txt'))
#print(data.keys())
#print(newOutputWay.keys())

