import os

from sentenceSelection import selectSentences


TEXT_DIR = "./hnSummarized/text/"
SUM_DIR = "./hnSummarized/summaries/"
NUM_SENTENCES = 10

def getFolder(folder, name):
    path = SUM_DIR + folder +"/"
    fName = name
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            print "Error on making folder: ", d
    return path + fName

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
        keyWordsList = ["One", "Two", "Three", "Four"]
        keyWords = keyWordsList[0] + " | " + " | ".join(keyWordsList[1:])

        toSave = keyWords + "\n" + summary

        savePath = getFolder(folder, downFile)
        rawFile = file(savePath, "w+")
        rawFile.write(toSave)
        rawFile.close()
