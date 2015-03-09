#from os import listdir
from sentenceSelection import selectSentences
import json

INFO_DICT = "./hnSummarized/info.json"
TEXT_DIR = "./hnSummarized/text/"

infoFile = file(INFO_DICT, "r")
info = json.load(infoFile)

OUT ="""
<!DOCTYPE html>
<html lang="en">

<head>
  <title>HN Summarized</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
  <link rel="stylesheet" type="text/css" href="custom.css">
</head>

<body>

<div class="jumbotron">
    <h1 class="text-center">HN Summarized</h1> 
</div>
"""

ROW = '<div class="row">'
ELE = """
    <div class="col-sm-6">
        <div class="container-fluid">
"""
ELE_END = """
        </div>
    </div>
"""
ROW_END = "</div>\n"

PAGE_END = """
</body>
</html>
"""

def block(title, summary, article, comments):
    ele = """
    <div class="col-sm-6">
        <div class="container-fluid">
            <h3 class ="text-center">{0}</h3>  
            <blockquote>
                <p>
                    {1}
                </p>
                <footer>
                    <a href ="{2}">Article</a> | <a href="{3}">HN Comments</a>
                </footer>
            </blockquote>
        </div>
    </div>
"""
    return ele.format(title, summary, article, comments)


ADD_ROW_BEFORE = True

for folder in listdir(TEXT_DIR):
    for downFile in listdir(TEXT_DIR + folder):
        fileID = downFile.split(".")[0]

        path = TEXT_DIR + folder + "/" + downFile

        # Load text
        rawFile = file(path, "r")
        rawText = rawFile.read()
        rawFile.close()
        sumSents = selectSentences(rawText, 10)

        if ADD_ROW_BEFORE:
            OUT += ROW

        title = info[fileID]["title"].encode("ascii", "ignore")
        summary = sumSents.encode("ascii", "ignore")
        article = info[fileID]["url"].encode("ascii", "ignore")
        comments = info[fileID]["comments"].encode("ascii", "ignore")

        OUT += block(title, summary, article, comments)

        if not ADD_ROW_BEFORE: #False
            OUT += ROW_END
            ADD_ROW_BEFORE = True
        else:
            ADD_ROW_BEFORE = False

ofile = file("out.html", "w+")
ofile.write(OUT)
ofile.close()

