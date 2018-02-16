import json
import re
from bs4 import BeautifulSoup
import requests
from helpers import *
# Web Scraping

# Scraping Categories


def scrape_award_categories():
    res = requests.get("https://en.wikipedia.org/wiki/Golden_Globe_Award")
    # print(res.status_code)
    # print(res.headers)
    content = res.content
    soup = BeautifulSoup(content, 'lxml')
    element = soup.find(id="Categories")

    # navigate
    element = element.parent.next_sibling.next_sibling.next_sibling.next_sibling  # element is <ul> of motion picture awards

    motion_picture_awards = [s for s in element.stripped_strings]
    # print(motion_picture_awards)

    element = element.next_sibling.next_sibling.next_sibling.next_sibling  # element is <ul> of tv awards

    tv_awards = [s.encode("ascii", errors="ignore").decode() for s in element.stripped_strings]

    # get rid of ': since 1962'
    tv_awards = [award.split(':')[0].encode("ascii", errors="ignore").decode()  for award in tv_awards]

    # get rid of empty strings
    tv_awards = [s for s in tv_awards if s != '']
    #print(tv_awards)
    return {'motion_picture_awards': motion_picture_awards, 'tv_awards': tv_awards}

#print(scrape_award_categories())