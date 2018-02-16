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
    motion_picture_awards_element = element.parent.next_sibling.next_sibling.next_sibling.next_sibling  # element is <ul> of motion picture awards

    motion_picture_awards = []

    for a in motion_picture_awards_element.find_all('a'):
        ss = a.stripped_strings
        for s in ss:
            # clean string
            s = s.encode("ascii", errors="ignore").decode().replace('  ', ' ')
            motion_picture_awards.append(s)

    tv_awards_element = motion_picture_awards_element.next_sibling.next_sibling.next_sibling.next_sibling  # element is <ul> of tv awards

    tv_awards = []

    for a in tv_awards_element.find_all('a'):
        ss = a.stripped_strings
        for s in ss:
            # clean string
            s = s.encode("ascii", errors="ignore").decode().replace('  ', ' ')
            tv_awards.append(s)

    return {'motion_picture_awards': motion_picture_awards, 'tv_awards': tv_awards}

# pp.pprint(scrape_award_categories())
