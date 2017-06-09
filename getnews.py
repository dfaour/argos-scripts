#!/usr/bin/python3

import feedparser

#Change to your favourite news RSS
feed_url = "https://news.google.ca/news?cf=all&hl=en&pz=1&ned=ca&output=rss"

feed = feedparser.parse(feed_url)

print("News")
print("---")


for i in range(10):
    print(feed['entries'][i]['title'] + " | href='" + feed['entries'][i]['link'] + "'")

print("---")

#Change to your favourite news site
print("Go to Google News... | href='https://news.google.ca'")
