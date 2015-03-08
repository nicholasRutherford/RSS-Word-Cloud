"""
Author: Nicholas Rutherford
"""

import requests

import os
from datetime import datetime
import urllib2
import pprint


HTML_DIR = "./hnSummarized/html/"
BASE_URL = "https://hacker-news.firebaseio.com/v0/"
HN_BASE = "https://news.ycombinator.com/item?id="
CUT_OFF = 100

alreadyGot = []
# Get list of files you've already downloaded
for folder in os.listdir(HTML_DIR):
    for downFile in os.listdir(HTML_DIR + folder):
        alreadyGot.append(int(downFile.split(".")[0]))

# Get top stories
r = requests.get(BASE_URL + "topstories.json")
rawLinks =  r.json()[:CUT_OFF]

links = []
for link in rawLinks:
    if link not in alreadyGot:
        links.append(link)
    else:
        print "Already have: ", link

def isGoodStory(q):
    """Determins if a story is 'good'"""
    if q["title"].lower().count('haskell') > 0:
        return True
    if q["score"] < 100:
        return False
    return True

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

def getFolder(query):
    d = datetime.fromtimestamp(query["time"]).date().isoformat()
    path = HTML_DIR + d +"/"
    try: 
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            print "Error on making folder: ", d
    return path



# Download the links for good stories
print "downloading..."
for link in goodStories:
    try:
        name = str(link["id"])
        name = name + ".html"

        folder = getFolder(link)

        # If it is an internal link, preface it with base url
        if link["url"] == "":
            response = urllib2.urlopen(HN_BASE + str(link["id"]))
        else:
            response = urllib2.urlopen(link["url"])
        rawHtml = response.read()

        outFile = file(folder + name, "w+")
        outFile.write(rawHtml)
        outFile.close()
    except (urllib2.HTTPError, ValueError):
        print "Error on : ", link["title"]