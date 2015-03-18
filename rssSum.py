import feedparser
from bs4 import BeautifulSoup
from wordcloud import WordCloud

import urllib2
import sys

# Get the feed
FEED = raw_input("Enter the url of the feed: ")

# Get all the urls:
print "Retrieving rss feed..."
feedObj = feedparser.parse(FEED)

webLinks = []
for link in feedObj["items"]:
    webLinks.append(link["link"])

# Download the html pages and parse into text:
print "Downloading and parsing pages..."
allText = ""
for i, link in enumerate(webLinks):
    # Status Bar
    sys.stdout.write("\r " + str(i*100/float(len(webLinks))) + "%")
    sys.stdout.flush()

    try:
        # Download the link
        response = urllib2.urlopen(link)
        rawHtml = response.read()

        # Parse the link
        soup = BeautifulSoup(rawHtml, "html5lib")
        paragraphs = soup.find_all('p')
        rawText = ""
        
        for para in paragraphs:
            rawText += para.getText()
        rawText = rawText.encode("ascii", 'ignore')
        allText = rawText 

    except (urllib2.HTTPError, ValueError):
        print "Error on : ", link

print "\nConstructing cloud..."

# Construct the word cloud
wordcloud = WordCloud(width=800, height=400).generate(allText)
wordcloud.to_file("image.png")
print "Done!"