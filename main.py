from Indexer import *
# from multiprocessing import Pool
from queryParser import *
import time

# qp = queryParser()
# res = qp.search(["donald", "trump"])
# print(res)

# res2 = qp.search(["pakistan", "zindabad"])
# print(res2)
# def poolhandler():
#     p = Pool()
#     p.map(createIndex, files)


def createIndex(filename):
    lex = lexicon()
    lex.updateLex(filename)


if __name__ == '__main__':

    #     # poolhandler()
    #     for file in files:
    createIndex("aljazeera.json")
