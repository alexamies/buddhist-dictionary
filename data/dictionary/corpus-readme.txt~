Explanation of files used by Python programs. See dictionary.ddl for other tables.


corpus.txt
===============================================================================
The file is a tab delimited file listing the URL and other details of corpus 
source documents. Fields:

id: An identifier of the text document

source_name: An identifier of the sutra or other source document. There may be 
  multiple versions of the same source document, including translations
  in different languages or multiple translations.

type: 'file' for local files, 'web' for web documents

language: Human language that the document was written in.

charset: iast - International Alphabet for Sanskrit Transcription, 
  traditional - traditional Chinese

doc_type: Raw text in the historic language, translated into a modern language, 
          or a commentary.

uri: Either the file name for local files or the URL for a web document (required).

source: A human friendly name for the document (required).

start: Text to identify start of text to be analyzed. Used to exclude 
  header information on web documents. Start marker itself is excluded. The text 
  '\N' indicates the text starts at the top of the document. Any text before the 
  start marker is ignored (optional).

end: Similar to the start marker. Anything after the end marker will be ignored
     (optional).

plain_text: The plain text source document that the markdown is based on. 
  Used for word frequency analysis. Could be a URL if the document is of type 'web'

translator: The original translator that translated the document from Sanskrit 
  or other language to Chinese (optional).

reference: The reference in the Tripitaka, usually Taisho, including volume,
           number, and scroll (optional).

genre: The genre of the text, such as Prajnaparamita, Jataka, etc.

period: The period that the text was translated to Chinese or created if 
        written in another language (optional).

pos_tagged: The name of a file with part-of-speech tagged text (optional).

analysis_file: The name of the file for vocabulary analysis. The bdicttil.py
               command line utility will generate a file with this name
                (optional).


phrases.txt
===============================================================================
This a phrase dataset. The fields are:

id: An id for the phrase.

chinese_phrase: Plain text in traditional Chinese

id: An id for the phrase entry

pos_tagged: the phrase tagged with Penn TreeBank style PoS tags, including word
            and phrase gloss

sanskrit: the Sanskrit equivalent, if known

source_no: The id of the corpus source document

source_name: The name of the source document. Included to make the phrase list 
             stand alone more easily. 

pos_penn.txt
===============================================================================
This table enumerates the part-of-speech tags used.  The Penn Treebank tag 
definitions are used for part-of-speech tags. The fields are:

tag: the text of the tag

name: a descriptive name of the tag

list: if the list is a closed set then the list of words is given. Both simplified
      and traditional are included.


unigram.txt
===============================================================================
This table is for word sense frequency derived from POS tagged documents.
The Penn Treebank tag definitions are used for part-of-speech tags. The fields are:

pos_tagged_text: The element text with POS tag and gloss in pinyin and English

element_text: The element text in traditional Chinese

word_id: Matching id in the word table

frequency: The frequency of occurence of the word sense


bigram.txt
===============================================================================
This table is for bigram frequency derived from POS tagged documents.
The Penn Treebank tag definitions are used for part-of-speech tags. The fields are:

pos_tagged_text: The element text with POS tag and gloss in pinyin and English

previous_text: The element text of the first word in traditional Chinese

element_text: The element text of the second (target) word in traditional Chinese

word_id: Matching id of the target word in the word table

frequency: The frequency of occurence of the bigram


Notes:
===============================================================================
(1) Only UTF-8 is supported
