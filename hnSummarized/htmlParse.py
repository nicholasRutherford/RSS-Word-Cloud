"""
Author: Nicholas Rutherford
"""

from bs4 import BeautifulSoup
import magic
import os
import re
from os import listdir
import codecs

def replace_spc_error_handler(error):
# error is an UnicodeEncodeError/UnicodeDecodeError instance
# with these attributes:
# object = unicode object being encoded
# start:end = slice of object with error
# reason = error message
# Must return a tuple (replacement unicode object,
# index into object to continue encoding)
# or raise the same or another exception
    return (u' ' * (error.end-error.start), error.end)

codecs.register_error("replace_spc", replace_spc_error_handler) 

HTML_DIR = "./hnSummarized/html/"
TEXT_DIR = "./hnSummarized/text/"

def getFolder(folder, downFile):
    path = TEXT_DIR + folder +"/"
    fName = downFile.split(".")[0] + ".txt"
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            print "Error on making folder: ", d
    return path + fName

for folder in listdir(HTML_DIR):
    for downFile in listdir(HTML_DIR + folder):
        # Make sure the files are html files
        path = HTML_DIR + folder + "/" + downFile
        fileDesc = magic.from_file(path)
        if fileDesc.split(",")[0] == "HTML document":
            rawFile = file(path, "r")
            rawHtml = rawFile.read()
            rawFile.close()

            soup = BeautifulSoup(rawHtml, "html5lib")
            rawText = soup.get_text()
            rawText = rawText.encode("ascii", "replace_spc")
        else:
            rawText = "No summary available."

        dPath = getFolder(folder, downFile)
        rawFile = file(dPath, "w+")
        rawFile.write(str(rawText))
        rawFile.close()
