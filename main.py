import json
import re
from  host import *
from getCategorys import *
from  presntorAndNominee import *

data = json.load(open('gg2018.json'))

getHostTwitterHandle(data)

getHostName(data)

categorys=getCategorys(data)

for text in categorys:
    print(text)
    print"\n"

r=re.compile(".(?i)*present.*")
testList = []
for tweet in data:
    if(bool(r.match(tweet.get('text')))):
            testList.append(tweet)


getPresenter("Best Director",testList, "Presenter")

for text in categorys:
    getPresenter(text,testList,"Presenter")
    print"\n"


r=re.compile(".(?i)*nominated.*")
nomineesList = []
for tweet in data:
    if(bool(r.match(tweet.get('text')))):
            nomineesList.append(tweet)
print(len(nomineesList))
getPresenter("Best Animated",nomineesList, "Nominees")

for text in categorys:
    getPresenter(text,nomineesList, "Nominees")
    print"\n"
