"""
Author: Nicholas Rutherford
"""

import requests

import urllib2
import pprint


HTML_DIR = "./html/"
BASE_URL = "https://hacker-news.firebaseio.com/v0/"
CUT_OFF = 100

# Get top stories
r = requests.get(BASE_URL + "topstories.json")
links =  r.json()[:CUT_OFF]

def isGoodStory(q):
    """Determins if a story is 'good'"""
    if q["score"] > 100:
        return True
    return False

# Go through the stories and select the good ones
goodStories = []
for link in links:
    r = requests.get(BASE_URL + "item/" + str(link) + ".json")
    query = r.json()
    try:
        if isGoodStory(query):
            goodStories.append(query)
            print query["title"], query["score"]
    except KeyError:
        print KeyError.text()

# Download the links for good stories
print "downloading..."
for link in goodStories:
    try:
        name = link["title"]
        name = name.replace(" ", "_")
        name = name.replace("/", "")
        name = name + ".html"
        response = urllib2.urlopen(link["url"])
        rawHtml = response.read()
        outFile = file(HTML_DIR + name, "w+")
        outFile.write(rawHtml)
        outFile.close()
    except (urllib2.HTTPError, ValueError):
        print "Error on : ", link["title"]