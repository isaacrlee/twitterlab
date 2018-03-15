from helpers import *
import re
import string

# Gets the name of the host by looking at hositng job and most common first two words
def getFacts(data):
    factsList = find_matching_tweets_from_data('.*(?i)(fun fact:).*', data)
    factsList2 = []
    for tweet in factsList:
        text = tweet.get('text')
        factsList2.append(text)
    # print (factsList2)

    factsList3 = []
    str = "Fun Fact:"
    for tweet in factsList2:
        idx = tweet.lower().find(str.lower())
        text = tweet[idx+len(str)+1:]
        # print (text)
        factsList3.append(text)
    facts = set(factsList3)
    # facts = factsList3

    unwanted_words = ["I", "You"]
    finalfacts = set()
    for fact in facts:
        for word in unwanted_words:
            if (fact.lower().find(word.lower())) >= 0:
                finalfacts.add(fact)
                break
    #print (finalfacts)



    #cleaning data
    # finalfacts = set()
    # for fact in facts:
    #     if(re.search(".*http[s]?://.*",  fact)):
    #         print (fact)
    #         fact.rsplit (' ', 1)[0]
    #         finalfacts.add(fact)
    #     else:
    #         finalfacts.add(fact)
    # print (finalfacts)


    return facts


