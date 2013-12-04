Explanation of corpus.txt file
The file is a tab delimited file listing the URL and other details of corpus source documents. Fields:

ID: An identifier of the source document

Type: File for local files, url for web documents

Character set: iast - International Alphabet for Sanskrit Transcription, traditional - traditional Chinese

Document URL: Either the file name for local files or the URL for a web document

Start marker: Text to identify start of text to be analyzed. Used to exclude header information on web documents. Start marker itself is excluded. The text '\N' indicates the text starts at the top of the document. Any text before the start marker is ignored.

End marker: Similar to the start marker. Anything after the end marker will be ignored.

Name: A human friendly name for the document.

Description: A longer description for the document.

Notes:
(1) Only UTF-8 is supported
