import json
import re
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


def indexarticle(article, docpos, ps, stop_words, self, frwdindx, points):
    article = re.sub(r'[^\w\s]', '', article)
    article = word_tokenize(article)
    for word_ in article:
        if word_ not in stop_words:
            word = ps.stem(word_)
            if (word not in self.lexicon):
                self.lexicon[word] = str(
                    len(self.lexicon))
            frwdindx.updateForwardIndex(
                docpos, self.lexicon[word], points)


class docID:
    def __init__(self):
        self.loadDocIDs()

    def loadDocIDs(self):
        with open("docIDs.json") as f:
            self.docIDs = json.load(f)

    def storeDocIDs(self):
        with open("docIDs.json", "w") as f:
            f.write(json.dumps(self.docIDs))

    def updateDocIDs(self, pos, article, totalwords):

        self.docIDs[str(pos)] = {
            "title": article["title"],
            "url": article["url"],
            "content": article["content"][:150] + "...",
            "length": totalwords
        }

    def __del__(self):
        self.storeDocIDs()


class forwardIndex:
    def __init__(self):
        self.forwardIndex = {}

    def updateForwardIndex(self, docID, wordID, points):
        if (docID not in self.forwardIndex):
            self.forwardIndex[docID] = {wordID: points}
        elif (wordID in self.forwardIndex[docID]):
            self.forwardIndex[docID][wordID] += points
        else:
            self.forwardIndex[docID][wordID] = points


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

        for article in data:

            title = article["title"]
            indexarticle(title, docpos, ps, stop_words, self, frwdindx, 6)
            content = article["content"]
            indexarticle(content, docpos, ps, stop_words,
                         self, frwdindx, 1)
            totalwords = len(content)
            doc_ids.updateDocIDs(docpos, article, totalwords)
            docpos += 1

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
                    self.invertedIndex[wordID][docID] = forwardIndex[docID][wordID]
                else:
                    self.invertedIndex[wordID] = {
                        docID: forwardIndex[docID][wordID]}
        self.storeInvertedIndex()
