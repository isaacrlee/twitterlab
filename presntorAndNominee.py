import json
import re


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



def getPresenter (category, tweets, feature, run=1):
    r=re.compile(".(?i)*"+category+"*")
    presentorList = []
    for tweet in tweets:
        if(bool(r.match(tweet.get('text')))):
            presentorList.append(tweet)
    wordsToIgnore=category.split()
    presentListWithoutCategory=[]
    for tweet in presentorList:
        text=tweet.get('text')
        for word in wordsToIgnore:
            text=text.replace(word,"")
            text=text.replace(word.lower(),"")
        text=text.replace("Motion","")
        text=text.replace("Picture","")
        presentListWithoutCategory.append(text)
    names=[]
    r=re.compile("([A-Z][\w-]*(\s+[A-Z][\w-]*)+)")
    for tweet in presentListWithoutCategory:
        text=r.findall(tweet)
        if len(text)!=0:
            names.append(text)
    #print(len(names))
    nameCheck=nameReliability(names,.1)
 #   if(len(nameCheck)>3 and run==1):
 #       r=re.compile("RT.*")
 #       testList2 = []
 #       for tweet in tweets:
 #           if(not (bool(r.match(tweet.get('text'))))):
 #               testList2.append(tweet)
 #       getPresenter(category, testList2, run=2) 
 #   else:
    print(feature+"(s) for " +category+" are:")
    for item in nameCheck:
        print(item)