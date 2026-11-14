# DICTIONARY DATABASE README
===============================================================================
These instructions are for setting the dictionary data.

## Dictionary Schema

The dictionary files are stored in tab separated variable (TSV) files with the schema:

1. Lexical unit number (integer, required) - each word sense has a lexical units, one headword may have multiple lexical units for each word sense. These should be in sequential order.
2. Headword in simplified characters (string, required)
3. Headword in traditional characters (string, optional) - omit if traditional is the same
4. Hanyu pinyin of headword (string, optional) - only omit if the pronunciation is not known
5. English equivalent (string, optional) - omit if not known
6. Part of speech (string) - must be one of the values in the file grammar.txt or empty.
7. Headword kind in simplified Chinese (string, optional) - mostly empty, except if the entry is a person ('人') or another well known kind
8. Headword kind in English (string, optional) - matches the previous field, for example person ('Person') or another well known kind
9. Topic or dictionary kind in Chinese (string, required) - must match one of the topics in the file topics.txt.
10. Topic dictionary kind in English (string, required) - must match the Chinese of the previous entry.
11. Sub-topic in simplified Chinese (string, optional) - mostly empty but may be a sub-category of the dictionary topic. For example, '中国' if the Dictionary kind is 历史, indicating Chinese history.
12. Sub-topic in Enlgish (string, optional), matching the Chinese of the previous field.
13. Image (string, optional) - the name of a file for the image, usually empty
14. Pronunciation (string, optional) - file name for a recording of the pronunciation, usually empty
15. Notes (string, optional) - Notes on the entry that explain or illustrate the entry. The source of the entry should be given in parentheses '()'.
16. Headword number (integer, required) - each headword should have a unique headword number. If there is only one lexical unit then the headword number must match the lexical unit number.

For empty fields use the value `\N` (a null value in a SQL database).