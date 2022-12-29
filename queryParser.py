import json
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import math


def combine(dict1, dict2):
    dict3 = {}
    for i in dict1:
        if i in dict2:
            dict3[i] = dict1[i] * dict2[i] * 2
        else:
            dict3[i] = dict1[i]
    for i in dict2:
        if i not in dict3:
            dict3[i] = dict2[i]

    return dict3


class queryParser:
    def __init__(self):
        with open("invertedIndex.json") as f:
            self.invertedIndex = json.load(f)
        with open("lexicon.json") as f:
            self.lexicon = json.load(f)
        with open("docIDs.json") as f:
            self.docIDs = json.load(f)

    def search(self, text):
        ps = PorterStemmer()
        docs = {}
        for term in text:
            term = ps.stem(term)
            if (term in self.lexicon):
                docs = combine(docs, self.invertedIndex[self.lexicon[term]])
        docs = sorted(
            docs.items(), key=lambda item: item[1], reverse=True)
        article_dict = []
        for i in docs:
            article_dict.append(self.docIDs[i[0]])
        return article_dict
