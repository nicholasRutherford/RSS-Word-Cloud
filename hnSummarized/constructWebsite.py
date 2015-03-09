#from os import listdir
import os
import json
import datetime

import websiteBlocks


INFO_DICT = "./hnSummarized/info.json"
SUM_DIR = "./hnSummarized/summaries/"
WEBSITE = "./hnSummarized/website/index.html"

infoFile = file(INFO_DICT, "r")
info = json.load(infoFile)


webpage = ""
webpage += websiteBlocks.HEADER

def elementBlock(title, keywords, summary, article, comments):
    return websiteBlocks.ELEMENT.format(title, keywords,
                                        summary, article, comments)

def dateBlock(text):
    return websiteBlocks.DATE.format(text)

today = datetime.datetime.now().date().isoformat()

ADD_ROW_BEFORE = True
folderList = os.listdir(SUM_DIR)
folderList.sort(reverse=True)
for folder in folderList:
    print folder, today
    if folder == today:
        webpage += dateBlock("Today")
    else:
        y, m , d = folder.split("-")
        dateOb = datetime.date(int(y), int(m), int(d))
        text = dateOb.strftime("%B %d, %Y") # January 01, 2015
        webpage += dateBlock(text)

    fileList = os.listdir(SUM_DIR + folder)
    fileList.sort(reverse=True)
    for downFile in fileList:
        fileID = downFile.split(".")[0]

        path = SUM_DIR + folder + "/" + downFile

        # Load text
        rawFile = file(path, "r")
        rawText = rawFile.read()
        rawFile.close()

        #Load Sumary Data
        keywords, summary = rawText.split("\n")

        # Load HN data
        title = info[fileID]["title"].encode("ascii", "ignore")
        article = info[fileID]["url"].encode("ascii", "ignore")
        comments = info[fileID]["comments"].encode("ascii", "ignore")

        if ADD_ROW_BEFORE:
            webpage += websiteBlocks.ROW

        webpage += elementBlock(title, keywords, summary, article, comments)

        if not ADD_ROW_BEFORE: #False
            webpage += websiteBlocks.ROW_END
            ADD_ROW_BEFORE = True
        else:
            ADD_ROW_BEFORE = False

ofile = file(WEBSITE, "w+")
ofile.write(webpage)
ofile.close()
