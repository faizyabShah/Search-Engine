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

*   [Lexicon](#using nltk library in python))
*   [Indexing](#Forward and Backward indexing)
*   [Getting started](#getting-started)
    *   [Requirements](#requirements)
    *   [Install](#install)
    *   [Usage](#usage)
*   [Here is where it's your turn](#here-is-where-its-your-turn)
*   [Don't forget anything](#dont-forget-anything)
    * [Used Technologies](#used-technologies)
    * [Testing](#testing)
    * [Logging](#logging)
*   [Contribute](#contribute)
*   [License](#license)
*   [Sources](#sources)
*   [Conclusion](#conclusion)

## Indexing:

* **Forward Indexing**

It's data structure that stores mapping from documents to words i.e. directs you from document to word.
Generally, steps to build Forward index are:
* Fetch the document and gather all the keywords.
* Append all the keywords in the index entry for this document.
* Repeat above steps for all documents

* **Inverted Indexing**

An inverted index is an index data structure storing a mapping from content, such as words or numbers, to its locations in a document or a set of documents.
Generally, steps to build an inverted index:

* Fetch the Document 
* Removing of Stop Words: Stop words are most occurring and useless words in document like “I”, “the”, “we”, “is”, “an”.
* Stemming of Root Word 
Whenever I want to search for “cat”, I want to see a document that has information about it. But the word present in the document is called “cats” or “catty” instead of “cat”. To relate the both words, I’ll chop some part of each and every word I read so that I could get the “root word”. There are standard tools for performing this like “Porter’s Stemmer”.
* Record Document IDs 
If word is already present add reference of document to index else create new entry. Add additional information like frequency of word, location of word etc.

## Why should I use this?

There are many README templates out there so why this one? The two main reasons for this are
that they contain often too little content or they are not easy to read or navigate through.

## Getting Started

So how do you get this template to work for your project? It is easier than you think.

### Requirements

* Have a project ready where you can add a README
* Basic knowledge of [Markdown][about-markdown] (here is a [Cheatsheet][markdown-cheatsheet])

### Install

Use git to clone this repository into your computer.

```
git clone https://gitlab.com/kopino4-templates/readme-template
```

### Usage

Use the well known command to copy the template

```bash
# Copy the content
CTRL + C

# Pase into your project
CTRL + V
```

## Here is where it's your turn

Here starts the main content of your README. This is why you did it for in the first place.
To describe to future users of this project (including yourself) everything they need to know
to be able to use it and understand it.

Use visuals to help the reader understand better. An image, diagram, chart or code example says
more than thousand words

![Diagram](doc/diagram.jpg)

## Don't forget anything

Think hard about anything that is clear to you but might not be clear for others. Why are you
using this aproach or why did you pick this solution instead?

### Used technologies

For sure mention all the technologies you used. If the technologies age in time you don't forget
they are used and need to be replaced.

### Testing

No tests no sucess. You SHOULD have tests for every project, but do new users know how to run them?

### Logging

Logging is essential. How do you know something went wrong if the computer doesn't tell you? Logs
are the first place to search for bugs. Explain to everybody how you can customize it or used it
in the right way.

## Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Sources

[react-markdown][react-markdown] - Project which served as an inspiration for this README

[Blog post templates][blog-post-templates] - Used to structure this template as an easy to read blog post

[About markdown][about-markdown] - Why should you use markdown?

[Markdown Cheat Sheet][markdown-cheatsheet] - Get a fast overview of the syntax

[//]: # "Source definitions"
[react-markdown]: https://github.com/remarkjs/react-markdown "React-markdown project"
[blog-post-templates]: https://backlinko.com/hub/content/blog-post-templates "Backlinko blog post templates"
[about-markdown]: https://www.markdownguide.org/getting-started/ "Introduction to markdown"
[markdown-cheatsheet]: https://www.markdownguide.org/cheat-sheet/ "Markdown Cheat Sheet"

## Conclusion

To summarize..

We have an exhaustive README template with many features. The README is easy to read and navigate like an article.
In our future projects we can use this template to get a great head start in creating a custom README.


