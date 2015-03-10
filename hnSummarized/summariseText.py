import os

from sentenceSelection import selectSentences
from keywordExtraction import extractKeywords


TEXT_DIR = "./hnSummarized/text/"
SUM_DIR = "./hnSummarized/summaries/"
NUM_SENTENCES = 10

def getFolder(fold, name):
    folderPath = SUM_DIR + fold +"/"
    fName = name
    try:
        os.makedirs(folderPath)
    except OSError:
        if not os.path.isdir(folderPath):
            print "Error on making folder: ", fold
    return folderPath + fName

for folder in os.listdir(TEXT_DIR):
    for downFile in os.listdir(TEXT_DIR + folder):
        path = TEXT_DIR + folder + "/" + downFile

        # Load text
        rawFile = file(path, "r")
        rawText = rawFile.read()
        rawFile.close()

        # Summarise
        summary = selectSentences(rawText, NUM_SENTENCES)

        # Key Words
        keyWordsList = extractKeywords(rawText)
        if len(keyWordsList) == 0:
            keyWords = ""
        elif len(keyWordsList) == 1:
            keyWords = keyWordsList[0]
        elif len(keyWordsList) == 2:
            keyWords = keyWordsList[0] + " | " + keyWordsList[1]
        else:
            keyWords = keyWordsList[0] + " | " + " | ".join(keyWordsList[1:])


        toSave = keyWords + "\n" + summary

        savePath = getFolder(folder, downFile)
        rawFile = file(savePath, "w+")
        rawFile.write(toSave)
        rawFile.close()
