# Search-Engine 📌
DSA Search Engine Project

A fun search engine made for our end semester project for Data Structures and ALgorithms, made with python, react js and html/css.

## Introduction: About the project ❓
*  **Team Members: 👤**
•	Faizyab Ali Shah
•	Manahil Ahmad 
•	Sohaib Aslam

*  **Dataset:**
We will use a dataset from the provided NELA-GT-2021 collection. 


## Structures and Frameworks 
We developed the UI using Html/Css with ReactJS. Whereas the code is in Python 3.

*    **Python** 
*    **ReactJS** for fast responding UI
*    **HTML/CSS** to style frontend
*    **Github** for team collaboration

## Contents

*   [Lexicon]
*   [Indexing]
    *   [Forward Indexing]
    *   [Inverted Indexing]
*   [Here is where it's your turn](#here-is-where-its-your-turn)
*   [Don't forget anything](#dont-forget-anything)
    * [Used Technologies](#used-technologies)
    * [Testing](#testing)
    * [Logging](#logging)
*   [Contribute](#contribute)
*   [License](#license)
*   [Sources](#sources)
*   [Conclusion](#conclusion)

## Lexicon:

First, we needed to remove stopwords and implement stemming on our dataset. For this purpose, we used *nltk* in Python. 
The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language.
To implement specific functions like *porterstemmer()* and use the library of *stop words* we might get in the dataset or in a query, we imported these specific libraries from the suite nltk.


## Indexing:

### Forward Indexing

It's data structure that stores mapping from documents to words i.e. directs you from document to word.
Generally, steps to build Forward index are:
* Fetch the document and gather all the keywords.
* Append all the keywords in the index entry for this document.
* Repeat above steps for all documents

### Inverted Indexing

An inverted index is an index data structure storing a mapping from content, such as words or numbers, to its locations in a document or a set of documents.
Generally, steps to build an inverted index:

* Fetch the Document 
* Removing of Stop Words: Stop words are most occurring and useless words in document like “I”, “the”, “we”, “is”, “an”.
* Stemming of Root Word 
Whenever I want to search for “cat”, I want to see a document that has information about it. But the word present in the document is called “cats” or “catty” instead of “cat”. To relate the both words, I’ll chop some part of each and every word I read so that I could get the “root word”. There are standard tools for performing this like “Porter’s Stemmer”.
* Record Document IDs 
If word is already present add reference of document to index else create new entry. Add additional information like frequency of word, location of word etc.
