from queryParser import *
from Indexer import *

query = queryParser()

doc = docID()

docids = query.search("Belgian parliament")

for i in docids:
    print(doc.docIDs[i])
