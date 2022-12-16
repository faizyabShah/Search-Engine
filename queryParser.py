import json
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


class queryParser:
    def __init__(self):
        with open("invertedIndex.json") as f:
            self.invertedIndex = json.load(f)
        with open("lexicon.json") as f:
            self.lexicon = json.load(f)

    def search(self, text):
        ps = PorterStemmer()
        text = text.split()
        docs = []
        for i in text:
            docs.extend(self.invertedIndex[self.lexicon[ps.stem(i)]])
        return docs
