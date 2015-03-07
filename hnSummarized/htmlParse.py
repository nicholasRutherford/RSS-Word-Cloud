"""
Author: Nicholas Rutherford
"""

from os import listdir
from bs4 import BeautifulSoup

HTML_DIR = "./hnSummarized/html/"
TEXT_DIR = "./hnSummarized/text/"

for htmlFile in listdir(HTML_DIR):
    rawFile = file(HTML_DIR + htmlFile, "r")
    rawHtml = rawFile.read()
    rawFile.close()

    soup = BeautifulSoup(rawHtml, "html5lib")
    rawText = soup.get_text()
    rawText = rawText.encode("ascii", "ignore")
    rawFile = file(TEXT_DIR + htmlFile.split(".")[0] + ".txt", "w+")
    rawFile.write(str(rawText))
    rawFile.close()
