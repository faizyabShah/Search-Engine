import time
from Indexer import *

start = time.time()

lex = lexicon()
lex.updateLex("aljazeera.json")

inv = invertedIndex()
inv.updateInvertedIndex()

print(time.time() - start)
