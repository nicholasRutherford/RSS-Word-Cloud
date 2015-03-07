import nltk.data
import nltk
import networkx as nx

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

pairs = []
for w in words:
    print nx.degree(w)
    #pairs.append(w, nx.degree(w))

print pairs

#nx.draw(g)
# Rank sentences
"""
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
print '\n---\n'.join(sent_detector.tokenize(rawText))
"""