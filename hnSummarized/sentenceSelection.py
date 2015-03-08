import nltk
import networkx as nx
from nltk.corpus import stopwords

def word_token(s, STOP_WORDS):
    """Convert a sentence into a list of words, excluding stop words"""
    good = []
    base = nltk.word_tokenize(s)
    for word in base:
        if word not in STOP_WORDS:
            good.append(word)
    return good

def selectSentences(rawText, K):
    # Load stop words
    STOP_WORDS = stopwords.words('english')

    # Remove newlines, sometimes mess up sentence detector
    rawText = rawText.replace("\n", " ")

    # Load pre-learned sentence detector, and split into sentences
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentList = sent_detector.tokenize(rawText)

    # Initialize graph
    g = nx.Graph()

    # Add each sentence as a node
    for sentence in sentList:
        g.add_node(sentence)

    # Determine edge weights
    for i, sent1 in enumerate(sentList):
        for j, sent2 in enumerate(sentList):
            if i < j:
                words1 = word_token(sent1, STOP_WORDS)
                words2 = word_token(sent2, STOP_WORDS)
                wordCount = 0
                for word in words1:
                    if word in words2:
                        wordCount += 1
                w = wordCount / float((len(words1) + len(words2))) #((math.log(len(words1))) + math.log(len(words2)))
                g.add_edge(sent1, sent2, weight =w)

    # Run pagerank and get scores
    scores = nx.pagerank(g)

    # Find cutoff score
    score_list = scores.items()
    try:
        min_score = sorted(score_list, key=lambda x : x[1], reverse=True)[K][1]
    except IndexError:
        min_score = 0

    # Return sentences above cutoff in the order they appeared in the text
    toReturn = []
    for sentence in sentList:
        if scores[sentence] > min_score:
            toReturn.append(sentence)
    return toReturn
