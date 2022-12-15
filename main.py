from Indexer import *

docs = docID()
docs.updateDocIDs("airwars.json")

indx = forwardIndex()
indx.updateForwardIndex("airwars.json")

inv = invertedIndex()
inv.updateInvertedIndex()
