Explanation of files used to describe the text collection.


corpus.txt
===============================================================================
The file is a tab delimited file listing the URL and other details of all the 
text documents. The fields are:

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

gloss_file: The name of the file for HTML mouse-over gloss. The bdicttil.py
            command line utility will generate a file with this name (optional).


Notes:
===============================================================================
(1) Only UTF-8 is supported
