import nltk
import networkx as nx

from nltk.corpus import stopwords
from sentenceSelection import tokeniseSentences

STOP = stopwords.words('english')


def tokeniseWords(rawText):
    # Use sentence tokensiser to remove code 'sentences'
    sentList = tokeniseSentences(rawText)
    text = ""
    for sentence in sentList:
        text += sentence + " "

    # Split text into words
    return  nltk.word_tokenize(text)

def removeStop(wordList, stopList):
    goodWords = []
    for word in wordList:
        if word not in stopList:
            goodWords.append(word)
    return goodWords

def filterTags(wordList):
    filteredWords = []
    tagWords = nltk.pos_tag(wordList)
    for word, tag in tagWords:
        if tag =="NN" or tag =="JJ":
            filteredWords.append(word)

    return filteredWords

def extract(wordList, num=4, threshold=5):
    # Construct the graph
    g = nx.DiGraph()
    for w in wordList:
        g.add_node(w)

    for i, w in enumerate(wordList):
        for j in xrange(1, threshold+1):
            try:
                g.add_edge(w, wordList[i+j])
            except IndexError:
                pass

    # Compute values
    pairs = nx.pagerank(g).items()
    sortedPairs = sorted(pairs, key=lambda x: x[1], reverse=True)
    goodKeywords = []
    for keyword, _ in sortedPairs[:num]:
        goodKeywords.append(keyword)

    return goodKeywords

def extractKeywords(rawText, num=4, stopList=STOP, threshold=5):
    wordList = tokeniseWords(rawText)
    wordList = removeStop(wordList, stopList)
    wordList = filterTags(wordList)
    return extract(wordList, num, threshold)
