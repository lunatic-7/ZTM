# Hacker news is a website, where we get daily news of Programming community,
# It is a quite popular website. A lot of programmers visit this website to see
# daily news on it. There is one more thing there, (upvotes), Poeple often wants to see,
# That news which has most amount of upvotes on it, It means that, that news is quite
# important and in trend.
# So, we are gonna make a bot which will give us only that news which has more than 100 upvotes,
# by scraping the data from hacker news website.
# We will use beautiful soup library for this purpose.
import requests  # requests is used to grab html from any site.
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')  # Scrapes all html
print(res)  # Gives <Response [200]> Means everything is good.
# print(res.text)  # Gives all html which we have scraped from the site.

# What we just received is a string, Now we are gonna use BeautifulSoup to convert the data,
# into something useful, something cleaner to understand.

soup = BeautifulSoup(res.text, 'html.parser')  # To convert the data in HTML
# print(soup)
# print(soup.body)  # To print body
# print(soup.body.contents)  # To print contents of body only
print(soup.title)   # To grab title.
print(soup.find_all('div'))  # Gives a list of all the div.
print(soup.find_all('a'))  # Gives a list of all the links.
print(soup.find('div'))  # Find only finds the first dic which shows up. ---> print(soup.div) It does the same as well.
print(soup.find(id='score_28547202'))  # Copied by inspecting the website

# Better way to grab info is to use CSS selectors, using select method.

print(soup.select('.score'))  # to print all which has score as id
print(soup.select('#score_28547202'))  # to print which has this as class

link = soup.select('.storylink')  # Class copied by inspecting the webpage.
votes = soup.select('.score')
print(link[0])  # to print 1st link
print(votes[0])  # as they are in a list, we can grab first item like this.
print(votes[0].get('id'))  # To get 1st elements id, So, with beautiful soup we can keep chaining these
