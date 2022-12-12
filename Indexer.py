import json
import string
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
ps = PorterStemmer()


class search():
    def __init__(self):
        pass

    def loadLex(self):
        with open("lexicon.json") as f:
            self.lexicon = json.load(f)

    def loadForwardIndex(self):
        with open("forwardIndex.json") as f:
            self.forwardIndex = json.load(f)

    def loadInvertedIndex(self):
        with open("invertedIndex.json") as f:
            self.invertedIndex = json.load(f)

    def storeLex(self):
        with open('lexicon.json', 'w') as f:
            f.write(json.dumps(self.lexicon))

    def storeForwardIndex(self):
        with open('forwardIndex.json', 'w') as f:
            f.write(json.dumps(self.forwardIndex))

    def storeInvertedIndex(self):
        with open('invertedIndex.json', 'w') as f:
            f.write(json.dumps(self.invertedIndex))

    def updateLex(self, file):
        self.loadLex()
        self.loadForwardIndex()
        stop_words = set(stopwords.words('english'))

        with open(file) as f:
            data = json.load(f)
        for i in data:
            pos = 0
            temp = i["title"].split()
            for word in temp:
                if (word in stop_words or word in string.punctuation):
                    pass
                else:
                    if (ps.stem(word) not in self.lexicon.keys()):
                        self.lexicon[ps.stem(word)] = str(len(self.lexicon))
                    if (i["id"] in self.forwardIndex.keys()):
                        if (self.lexicon[ps.stem(word)] in self.forwardIndex[i["id"]].keys()):
                            self.forwardIndex[i["id"]][self.lexicon[ps.stem(word)]].append(
                                pos)
                        else:
                            self.forwardIndex[i["id"]][self.lexicon[ps.stem(word)]] = [
                                pos]
                    else:
                        self.forwardIndex[i["id"]] = {
                            self.lexicon[ps.stem(word)]: [pos]}

                pos += 1
            temp = i["content"].split()
            for word in temp:
                if (word in stop_words or word in string.punctuation):
                    pass
                else:
                    if (ps.stem(word) not in self.lexicon.keys()):
                        self.lexicon[ps.stem(word)] = str(len(self.lexicon))
                    if (i["id"] in self.forwardIndex.keys()):
                        if (self.lexicon[ps.stem(word)] in self.forwardIndex[i["id"]].keys()):
                            self.forwardIndex[i["id"]][self.lexicon[ps.stem(word)]].append(
                                pos)
                        else:
                            self.forwardIndex[i["id"]][self.lexicon[ps.stem(word)]] = [
                                pos]
                    else:
                        self.forwardIndex[i["id"]] = {
                            self.lexicon[ps.stem(word)]: [pos]}

                pos += 1

        self.storeLex()
        self.storeForwardIndex()


obj = search()
# The file to be forward-indexed and new words from which to be added into the lexicon
# go as argument to the updateLex function
obj.updateLex("airwars.json")
