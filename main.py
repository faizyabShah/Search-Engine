from Indexer import *

docs = docID()
docs.updateDocIDs("airwars.json")

indx = search()
indx.updateLex("airwars.json")
indx.makeInvertedIndex()
