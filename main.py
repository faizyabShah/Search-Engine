from Indexer import *
from multiprocessing import Pool
import time


files = ["airwars.json"]


def poolhandler():
    p = Pool()
    p.map(createIndex, files)


def createIndex(filename):
    lex = lexicon()
    lex.updateLex(filename)


if __name__ == '__main__':

    start = time.time()
    # poolhandler()
    for file in files:
        createIndex(file)
    print(time.time() - start)
