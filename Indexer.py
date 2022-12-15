import json
import string
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
ps = PorterStemmer()


class docID:
    def __init__(self):
        pass

    def loadDocIDs(self):
        with open("docIds.json") as f:
            self.docIDs = json.load(f)

    def storeDocIDs(self):
        with open("docIDs.json", "w") as f:
            f.write(json.dumps(self.docIDs))

    def updateDocIDs(self, file):
        self.loadDocIDs()
        with open(file) as f:
            data = json.load(f)
        for article in data:
            if article["url"] in self.docIDs.keys():
                pass
            else:
                self.docIDs[article["url"]] = str(len(self.docIDs))
        self.storeDocIDs()


class forwardIndex:

    def __init__(self):
        pass

    def loadLex(self):
        with open("lexicon.json") as f:
            self.lexicon = json.load(f)

    def loadForwardIndex(self):
        with open("forwardIndex.json") as f:
            self.forwardIndex = json.load(f)

    def storeLex(self):
        with open('lexicon.json', 'w') as f:
            f.write(json.dumps(self.lexicon))

    def storeForwardIndex(self):
        with open('forwardIndex.json', 'w') as f:
            f.write(json.dumps(self.forwardIndex))

    def updateForwardIndex(self, file):
        self.loadLex()
        self.loadForwardIndex()
        with open("docIDs.json") as f:
            docIDs = json.load(f)
        stop_words = set(stopwords.words('english'))

        with open(file) as f:
            data = json.load(f)
        for i in data:  # loop over entries in file dictionary, where entries are articles
            pos = 0
            temp = i["title"] + " " + i["content"]
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
                    if (docIDs[i["url"]] in self.forwardIndex.keys()):
                        # check if wordID present in frwd indexed file
                        if (self.lexicon[ps.stem(word)] in self.forwardIndex[docIDs[i["url"]]].keys()):
                            if (pos not in self.forwardIndex[docIDs[i["url"]]][self.lexicon[ps.stem(word)]]):

                                # if present, then append pos of word to the list of pos
                                self.forwardIndex[docIDs[i["url"]]][self.lexicon[ps.stem(word)]].append(
                                    pos)
                        else:
                            # if not present, then add a key of wordID and save a list with the pos
                            # as its value
                            self.forwardIndex[docIDs[i["url"]]][self.lexicon[ps.stem(word)]] = [
                                pos]
                    else:
                        # if docID not already present, add the docID and join wordId and
                        # pos as a dict entry for its value
                        self.forwardIndex[docIDs[i["url"]]] = {
                            self.lexicon[ps.stem(word)]: [pos]}

                pos += 1

        self.storeLex()
        self.storeForwardIndex()


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
