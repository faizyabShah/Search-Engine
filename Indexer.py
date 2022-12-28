import json
import re
import string
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from multiprocessing import pool


def indexarticle(article, docpos, ps, stop_words, self, frwdindx):
    temp = article["title"] + " " + article["content"]
    temp = temp.translate(str.maketrans('', '', string.punctuation))
    temp = word_tokenize(temp)
    for i in range(len(temp)):
        if temp[i] not in stop_words:
            word = ps.stem(temp[i])
            if (word not in self.lexicon):
                self.lexicon[word] = str(
                    len(self.lexicon))
            frwdindx.updateForwardIndex(
                docpos, self.lexicon[word], i)


class docID:
    def __init__(self):
        self.loadDocIDs()

    def loadDocIDs(self):
        with open("docIDs.json") as f:
            self.docIDs = json.load(f)

    def storeDocIDs(self):
        with open("docIDs.json", "w") as f:
            f.write(json.dumps(self.docIDs))

    def updateDocIDs(self, pos, article):

        self.docIDs[str(pos)] = {
            "title": article["title"],
            "url": article["url"],
            "content": article["content"][:150] + "..."
        }

    def __del__(self):
        self.storeDocIDs()


class forwardIndex:
    def __init__(self):
        self.forwardIndex = {}

    def updateForwardIndex(self, docID, wordID, pos):
        if (docID in self.forwardIndex):
            if (wordID in self.forwardIndex[docID]):
                self.forwardIndex[docID][wordID].append(pos)
            else:
                self.forwardIndex[docID][wordID] = [pos]
        else:
            self.forwardIndex[docID] = {wordID: [pos]}


class lexicon:

    def __init__(self):
        pass

    def loadLex(self):
        with open("lexicon.json") as f:
            self.lexicon = json.load(f)

    def storeLex(self):
        with open('lexicon.json', 'w') as f:
            f.write(json.dumps(self.lexicon))

    def updateLex(self, file):
        ps = PorterStemmer()
        self.loadLex()
        frwdindx = forwardIndex()
        doc_ids = docID()

        stop_words = set(stopwords.words('english'))

        with open(file) as f:
            data = json.load(f)

        docpos = len(doc_ids.docIDs)
        # for article in data:
        #     doc_ids.updateDocIDs(docpos, article)
        #     docpos+=1

        for article in data:

            doc_ids.updateDocIDs(docpos, article)
            docpos += 1
            indexarticle(article, docpos, ps, stop_words, self, frwdindx)

        inv = invertedIndex()
        inv.updateInvertedIndex(frwdindx.forwardIndex)
        self.storeLex()


class invertedIndex:
    def __init__(self):
        pass

    def loadInvertedIndex(self):
        with open("invertedIndex.json") as f:
            self.invertedIndex = json.load(f)

    def storeInvertedIndex(self):
        with open('invertedIndex.json', 'w') as f:
            f.write(json.dumps(self.invertedIndex))

    def updateInvertedIndex(self, forwardIndex):
        self.loadInvertedIndex()
        for docID in forwardIndex:
            for wordID in forwardIndex[docID]:
                if (wordID in self.invertedIndex):
                    # if docID not in self.invertedIndex[wordID]:
                    # if docID in self.invertedIndex[wordID]:
                    self.invertedIndex[wordID][docID] = forwardIndex[docID][wordID]
                    # self.invertedIndex[wordID].append(docID)
                else:
                    self.invertedIndex[wordID] = {
                        docID: forwardIndex[docID][wordID]}
        self.storeInvertedIndex()
