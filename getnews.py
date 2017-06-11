#!/usr/bin/python3

import feedparser

#Change to your favourite news RSS
feed_url = "https://news.google.ca/news?cf=all&hl=en&pz=1&ned=ca&output=rss"

#Number of stories to get
stories = 10

print("News")
print("---")

feed = feedparser.parse(feed_url)

try:
    for i in range(stories):
        print(feed['entries'][i]['title'] + " | href='" + feed['entries'][i]['link'] + "'")

except:
    print("[Connection error...]")
    print("---")
    print("Go to Google News... | href='https://news.google.ca'")
    exit()
print("---")

#Change to your favourite news site
print("Go to Google News... | href='https://news.google.ca'")
