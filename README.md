# NTI Buddhist Text Reader Project
===============================================================================

The NTI Buddhist Text Reader is a digital library for Chinese Buddhist texts
with a built-in text reader, a Chinese-English dictionary and corpus management
tools, for analyzing and managing Buddhist Chinese texts. This is a non-profit,
open source project. Subscribe to the group
[ntireader-announce](https://groups.google.com/forum/#!forum/ntireader-announce),
a low volume group for announcements, to keep up to date.

## Goals

1. Create a text reader for the Taishō Shinshū Daizōkyō version of the 
   Chinese Buddhist canon.

2. Create a Chinese-English Buddhist dictionary that is free and easy to use for 
   everybody interested in Buddhism, including lay people reading Buddhist
   texts, students, translators, and academics.

3. Create tools that are useful for lingustic analysis of Buddhist texts,
   including identification of specialist Buddhist terms and comparison of
   Chinese texts.

There are three parts to the project:

1. The web user interface. This includes HTML and JavaScript files. 
   The HTML files are generated by the Go language 
   [cnreader](https://github.com/alexamies/chinesenotes.com/tree/master/go/src/cnreader)
   command line tool from the [Chinese Notes](http://chinesenotes.com) sister
   project. The dynamic content is driven by a Go web application.

2. The data. This is the dictionary and text files. The data files are in UTF-8
   tab delimited text. There is also a corpus directory, which contains the
   literature to build the vocabulary and word frequency from. These are
   Chinese texts from the Buddhist canon and related collections. They include
   [Buddhist terminology](https://github.com/alexamies/buddhist-dictionary/blob/master/data/dictionary/buddhist_terminology.txt),
   [Buddhist people, places, and texts](https://github.com/alexamies/buddhist-dictionary/blob/master/data/dictionary/buddhist_named_entities.txt),
   a [general Chinese-English dictionary](https://github.com/alexamies/buddhist-dictionary/blob/master/data/dictionary/cnotes_zh_en_dict.tsv),
   and other files.

3. Jupyter notebooks and other Python tools for building vocabulary.

The license for the web site and dictionary content is Creative Commons 
Attribution-Share Alike 3.0. The license for source code and markup templates, 
is Apache 2.0.

## Acknowldegements

1. The dictionary includes many terms from the [CC-CEDICT Chinese - English 
   dictionary](http://cc-cedict.org/wiki/), shared under the 
   [Creative Commons Attribution-Share Alike 3.0
   License](https://creativecommons.org/licenses/by-sa/3.0/).

2. Historic Buddhist texts from the Taishō Tripiṭaka are from
   [CBETA](https://cbeta.org).

3. Sources listed in the [References](https://ntireader.org/references.html) with
   citations for each term using a system of 
   [abbreviations](https://ntireader.org/abbreviations.html)

Humanistic Buddhism texts are now moved to the [Humanistic Buddhism
Reader](https://hbreader.org/).

## Getting Started

### Adding new vocabulary

To get started adding new vocabulary navigate to the 
[Add Entry Colab Sheet](https://colab.research.google.com/github/alexamies/chinesenotes-python/blob/master/add_mod_entry.ipynb)
and click Open in Colab. Colab works best with Chrome.

### Installing

To install the software follow instructions in the
[INSTALL-README.md](INSTALL-README.md)
file.

## Contributors

Thank you to the contributors who did not submit directly via GitHub:

1. Venerable You Zai
2. Michael Murphy - translation phrases from [Studies on Humanistic Buddhism](https://journal.nantien.edu.au/)
3. [Fo Guang Shan Institute of Humanistic Buddhism](https://www.fgsihb.org) - Glosary of Humanistic Buddhism

-------------------------------------------------------------------------------
Copyright Nan Tien Institute 2013-2022, http://www.nantien.edu.au.
