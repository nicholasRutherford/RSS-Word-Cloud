from os import listdir
from sentenceSelection import selectSentences
TEXT_DIR = "./hnSummarized/text/"

sm = ""
for textFile in listdir(TEXT_DIR):
    # Load text
    rawFile = file(TEXT_DIR + textFile, "r")
    rawText = rawFile.read()
    rawFile.close()
    sumSents = selectSentences(rawText, 10)

    print textFile
    sm += "************************************************************\n"
    sm += textFile + "\n"
    sm += "************************************************************\n"
    for sent in sumSents:
        sm += sent + "\n---------------------------------------------\n"
    sm += "\n\n\n"

ofile = file("sumall", "w+")
ofile.write(sm)

