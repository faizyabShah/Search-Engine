import json
import re
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
        if (docID in self.forwardIndex):
            if (wordID in self.forwardIndex[docID]):
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

        docpos = len(doc_ids.docIDs)

        for article in data:
            # if ("isIndexed" not in article):
            doc_ids.updateDocIDs(docpos, article)
            temp = article["title"] + " " + article["content"]
            temp = re.sub(r'[^\w\s]', '', temp)
            temp = temp.split()
            for i in range(len(temp)):
                if temp[i] not in stop_words:
                    word = ps.stem(temp[i])
                    if (word not in self.lexicon):
                        self.lexicon[word] = str(
                            len(self.lexicon))
                    frwdindx.updateForwardIndex(
                        docpos, self.lexicon[word], i)

            docpos += 1
            # article["isIndexed"] = 1
        self.storeLex()
        # with open(file, "w") as f:
        #     f.write(json.dumps(data))


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
                    # if docID not in self.invertedIndex[wordID]:
                    self.invertedIndex[wordID].append(docID)
                else:
                    self.invertedIndex[wordID] = [docID]
        self.storeInvertedIndex()
