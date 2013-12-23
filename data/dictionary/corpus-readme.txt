Explanation of corpus.txt and phrases.txt files

corpus.txt
===============================================================================
The file is a tab delimited file listing the URL and other details of corpus 
source documents. Fields:

ID: An identifier of the text document

Document Name: An identifier of the sutra or other source document. There may be 
  multiple versions of the same source document, including translations
  in different languages or multiple translations.

Type: File for local files, url for web documents

Language: Human language that the document was written in.

Character set: iast - International Alphabet for Sanskrit Transcription, 
  traditional - traditional Chinese

Document Tyle: Raw text in the historic language, translated into a modern language, or a commentary.

Document URI: Either the file name for local files or the URL for a web document
  or a book ISBN.

Source: A human friendly name for the document.

Start marker: Text to identify start of text to be analyzed. Used to exclude 
  header information on web documents. Start marker itself is excluded. The text 
  '\N' indicates the text starts at the top of the document. Any text before the 
  start marker is ignored.

End marker: Similar to the start marker. Anything after the end marker will be 
  ignored.

Plain Text: The plain text source document that the markdown is based on. 
  Used for word frequency analysis.

Translator: The original translator that translated the document from Sanskrit 
  or other language to Chinese.

Reference: The reference in the Tripitaka, usually Taisho, including volume, number, and scroll.

Genre: The genre of the text, such as Prajnaparamita, Jataka, etc.

phrases.txt
===============================================================================
This a phrase dataset. The fields are:

chinese_phrase: Plain text in traditional Chinese

pos_tagged: the phrase tagged with Penn TreeBank style PoS tags, including word and phrase gloss

sanskrit: the Sanskrit equivalent, if known

source_no: The id of the corpus source document

source_name: The name of the source document. Included to make the phrase list stand alone more easily.

Notes:
(1) Only UTF-8 is supported
