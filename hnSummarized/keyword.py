import nltk
import nltk
import networkx as nx
import pprint
from nltk.corpus import stopwords
stop = stopwords.words('english')

import matplotlib as plt
TEXT_DIR = "./hnSummarized/text/"

testFile = "Fired.txt"

# Load text
rawFile = file(TEXT_DIR + testFile, "r")
rawText = rawFile.read()
rawFile.close()



# Split text into words
rawWords = nltk.word_tokenize(rawText)

goodWords = []
for word in rawWords:
    if word not in stop:
        goodWords.append(word)

words = []
tagWords = nltk.pos_tag(goodWords)
for word, tag in tagWords:
    if tag =="NN" or tag =="JJ":
        words.append(word)


# Construct the graph
g = nx.DiGraph()
for w in words:
    g.add_node(w)

THRESHOLD = 5
for i, w in enumerate(words):
    for j in xrange(1, THRESHOLD+1):
        try:
            g.add_edge(w, words[i+j])
        except IndexError:
            pass

# Compute values
pairs = nx.pagerank(g)

# Print keywords
for w in sorted(pairs, key=pairs.get, reverse=True)[:10]:
  print w, pairs[w]
# Rank sentences
"""
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
sentList = sent_detector.tokenize(rawText)

high_sent = []

for sentence in sentList:
    sWords = nltk.word_tokenize(sentence)
    length = float(len(sWords))
    sValue = 0
    for w in sWords:
        try:
            sValue += pairs[w]
        except KeyError:
            length -= 1
    if length ==0:
        high_sent.append((sentence, 0))
    else:       
        sValue = sValue / length
        high_sent.append((sentence, sValue))


for x in sorted(high_sent, key=lambda x : x[1], reverse=True):
    print x

"""