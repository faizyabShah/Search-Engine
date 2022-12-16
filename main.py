from queryParser import *
from Indexer import *


lex = lexicon()
lex.updateLex("airwars.json")

inv = invertedIndex()
inv.updateInvertedIndex()
