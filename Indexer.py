import json
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


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
        self.loadForwardIndex()

    def loadForwardIndex(self):
        with open("forwardIndex.json") as f:
            self.forwardIndex = json.load(f)

    def storeForwardIndex(self):
        with open("forwardIndex.json", "w") as f:
            f.write(json.dumps(self.forwardIndex))

    def updateForwardIndex(self, docID, wordID, pos):
        if (docID in self.forwardIndex.keys()):
            if (wordID in self.forwardIndex[docID].keys()):
                if (pos not in self.forwardIndex[docID][wordID]):
                    self.forwardIndex[docID][wordID].append(pos)
            else:
                self.forwardIndex[docID][wordID] = [pos]
        else:
            self.forwardIndex[docID] = {wordID: [pos]}

    def __del__(self):
        self.storeForwardIndex()


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

        docpos = 0

        for article in data:  # loop over entries in file dictionary, where entries are articles
            doc_ids.updateDocIDs(docpos, article)

            pos = 0
            temp = article["title"] + " " + article["content"]
            temp = temp.split()
            for word in temp:  # first, looping over words in the title of the article
                if (word in stop_words or word in string.punctuation):
                    pass  # if stopwords, or punctuation, no op
                else:
                    if (ps.stem(word) not in self.lexicon.keys()):
                        # if word stem is not in the lex file, then add it as key in lex dictionary
                        # and set value to pos in lex file
                        self.lexicon[ps.stem(word)] = str(len(self.lexicon))
                        # now check if docID is in frwd indexed file
                    frwdindx.updateForwardIndex(
                        docpos, self.lexicon[ps.stem(word)], pos)
                pos += 1

            docpos += 1

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

    def updateInvertedIndex(self):
        self.loadInvertedIndex()
        with open("forwardIndex.json") as f:
            forwardIndex = json.load(f)
        for docID in forwardIndex:
            for wordID in forwardIndex[docID]:
                if (wordID in self.invertedIndex):
                    if (docID in self.invertedIndex[wordID]):
                        pass
                    else:
                        self.invertedIndex[wordID].append(docID)
                else:
                    self.invertedIndex[wordID] = [docID]
        self.storeInvertedIndex()
