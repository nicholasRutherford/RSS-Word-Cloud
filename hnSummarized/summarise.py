import nltk.data
import nltk
import networkx as nx
import pprint

import matplotlib as plt
TEXT_DIR = "./hnSummarized/text/"

testFile = "Fired.txt"

# Load text
rawFile = file(TEXT_DIR + testFile, "r")
rawText = rawFile.read()
rawFile.close()


# Split text into words
words = nltk.word_tokenize(rawText)

# Construct the graph
g = nx.Graph()
for w1, w2 in [[words[i], words[i+1]] for i in xrange(len(words)-1)]:
    g.add_node(w1)
    g.add_node(w2)
    g.add_edge(w1,w2)

# Compute values
pairs = {}
for n in g.nodes():
    pairs[n] = g.degree(n)


# Rank sentences

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
sentList = sent_detector.tokenize(rawText)

high_sent = []

for sentence in sentList:
    sWords = nltk.word_tokenize(sentence)
    sValue = 0
    for w in sWords:
        sValue += pairs[w]
    sValue = sValue / float(len(sWords))
    high_sent.append((sentence, sValue))

for x in sorted(high_sent, key=lambda x : x[1], reverse=True):
    print x
