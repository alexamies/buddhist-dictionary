buddhist-dictionary
===============================================================================
NTI Buddhist Text Reader

A text reader, including a Chinese-English Buddhist dictionary and tools, for
analyzing and managing Buddhist Chinese texts. This is a non-profit, open
source project.

Goals:

1. Create a dictionary that is easy to use for everybody interested in Buddhism, 
   including lay people reading Buddhist texts, students, translators, and
   academics. Importantly, the goal is to create useful tools rather than
   authoritative definitions of terms.

2. Create tools that are useful for lingustic analysis of Buddhist texts,
   including identification of specialist Buddhist terms and comparison of
   Chinese texts.

3. Use the tools to analyze and annotate a number of texts and share the content 
   with the general public.

There are three parts to the project:

1. The web user interface. This includes HTML, PHP, and JavaScript files.

2. The data. This is the dictionary and text files. The data files are in UTF-8
   tab delimited text. There is also a corpus directory, which contains the
   literature to build the vocabulary and word sense frequency from. These are
   Chinese texts from the Buddhist canon and related collections. The corpus 
   files include part-of-speech (POS) tagged documents and untagged documents.

3. Command line tools. For building vocabulary. These are in Python. This
   includes a POS tagger and HTML annotation tool.

The license for the web site and dictionary content is Creative Commons 
Attribution-Share Alike 3.0. The license for source code and markup templates, 
is Apache 2.0.

Acknowldegements:
1. The dictionary is based on the the [CC-CEDICT Chinese - English dictionary]
   (http://cc-cedict.org/wiki/), shared under the 
   [Creative Commons Attribution-Share Alike 3.0 License]
   (http://creativecommons.org/licenses/by-sa/3.0/).

2. Historic Buddhist texts from the Taishō Tripiṭaka are from [CBETA]
   (http://cbeta.org).
   
3. Humanistic Buddhism texts are reproduced from Fo Guang Shan with permission.

-------------------------------------------------------------------------------
Copyright Nan Tien Institute 2013, http://www.nantien.edu.au.
