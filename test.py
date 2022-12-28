import json

test = {}


with open("invertedIndex.json", "w") as f:
    f.write(json.dumps(test))

with open("lexicon.json", "w") as f:
    f.write(json.dumps(test))

with open("docIDs.json", "w") as f:
    f.write(json.dumps(test))
