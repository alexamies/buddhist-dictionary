"""Command line to compile a vocabulary from a document. =====================

The vocabulary may be output to a document.
"""


def BuildVocabulary(infile, sdict):
    """Builds the list of known and unknown words from the input file.

    """
    f = open(infile, 'r')
    wc = 0
    known_words = set()
    new_words = set()
    for line in f:
        if line.find('---END---') != -1:
            break
        words = line.split()
        wc += len(words)
        for word in words:
            if word in sdict:
                known_words.add(word)
            else:
                new_words.add(word)
    print('Word count: %d, known words: %d, new words: %d' % 
          (wc, len(known_words), len(new_words)))
    print('Known words:')
    PrintVocab(known_words)
    print()
    print('New words')
   PrintVocab(new_words)


def PrintVocab(words):
    """Prints the set of words to the console
    """
    for word in words:
      print(word)

