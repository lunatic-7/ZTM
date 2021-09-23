# Hacker news is a website, where we get daily news of Programming community,
# It is a quite popular website. A lot of programmers visit this website to see
# daily news on it. There is one more thing there, (upvotes), Poeple often wants to see,
# That news which has most amount of upvotes on it, It means that, that news is quite
# important and in trend.
# So, we are gonna make a bot which will give us only that news which has more than 100 upvotes,
# by scraping the data from hacker news website.

import requests
from bs4 import BeautifulSoup
import pprint  # for cleaner output

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')  # Copied from 2nd page of hacker news
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['Votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)  # None is for default
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'Title': title, 'Link': href, 'Votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
