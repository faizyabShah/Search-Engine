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
    
    #function takes in empty/already formed lexicon and frwrd indexed files, and updates it for the
    #file included

    def updateLex(self, file):
        self.loadLex()
        self.loadForwardIndex()
        stop_words = set(stopwords.words('english'))

        with open(file) as f:
            data = json.load(f)
        for i in data:      #loop over entries in file dictionary, where entries are articles
            pos = 0
            temp = i["title"].split()
            for word in temp:   #first, looping over words in the title of the article
                if (word in stop_words or word in string.punctuation):
                    pass        #if stopwords, or punctuation, no op
                else:           
                    if (ps.stem(word) not in self.lexicon.keys()):
                        #if word stem is not in the lex file, then add it as key in lex dictionary 
                        #and set value to pos in lex file
                        self.lexicon[ps.stem(word)] = str(len(self.lexicon))
                        #now check if docID is in frwd indexed file
                    if (i["id"] in self.forwardIndex.keys()):
                        #check if wordID present in frwd indexed file
                        if (self.lexicon[ps.stem(word)] in self.forwardIndex[i["id"]].keys()):
                            #if present, then append pos of word to the list of pos
                            self.forwardIndex[i["id"]][self.lexicon[ps.stem(word)]].append(
                                pos)
                        else:
                            #if not present, then add a key of wordID and save a list with the pos 
                            #as its value
                            self.forwardIndex[i["id"]][self.lexicon[ps.stem(word)]] = [
                                pos]
                    else:
                        #if docID not already present, add the docID and join wordId and
                        #pos as a dict entry for its value
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
