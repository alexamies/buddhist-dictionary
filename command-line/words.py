"""Command line utility for analysis based on Chinese words. ==================

Reads and processes the words.txt text file. The words may be checked
for consistency and dumped out to file again.
"""

DIR_NAME = '../data/dictionary/'
FILE_NAME = 'words.txt'


def CheckWords(words):
    """Checks the words for consistency.
    
    The words may be loaded from the words.txt and checked for 
    consistency. For example, it has been necessary to remove geographic coordinates
    from place names.

    Args:
        words: List of words loaded from the words.txt file.
    """
    print('%d words being checked.' % len(words))
    problems = []
    for word in words:
        iden = word['id']
        simplified = word['simplified']
        if 'topic_en' not in word:
            print('(%d , "%s") does not have a topic.' % (iden, simplified))
            continue
        topic_en = word['topic_en']
        places = []
        if 'Places' == topic_en:
            # print('(%d , "%s") is a place.' % (iden, simplified))
            places.append(word)
    print('%d places found.' % len(places))


def LoadWords():
    """Loads the words text file into a list.
    
    Returns:
        A list of words entries.
    """
    fullpath = '%s%s' % (DIR_NAME, FILE_NAME)
    with open(fullpath, 'r') as f:
        words = []
        for line in f:
            tokens = line.split('\t')
            if tokens:
                entry = {}
                entry['id'] = int(tokens[0])
                if len(tokens) > 1:
                    entry['simplified'] = tokens[1]
                if len(tokens) > 2:
                    entry['traditional'] = tokens[2]
                if len(tokens) > 3:
                    entry['pinyin'] = tokens[3]
                if len(tokens) > 4:
                    entry['english'] = tokens[4]
                if len(tokens) > 5:
                    entry['grammar'] = tokens[5]
                if len(tokens) > 6:
                    entry['concept_cn'] = tokens[6]
                if len(tokens) > 7:
                    entry['concept_en'] = tokens[7]
                if len(tokens) > 8:
                    entry['topic_cn'] = tokens[8]
                if len(tokens) > 9:
                    entry['topic_en'] = tokens[9]
                if len(tokens) > 10:
                    entry['parent_cn'] = tokens[10]
                if len(tokens) > 11:
                    entry['parent_en'] = tokens[11]
                if len(tokens) > 12:
                    entry['image'] = tokens[12]
                if len(tokens) > 13:
                    entry['mp3'] = tokens[13]
                if len(tokens) > 14:
                    entry['notes'] = tokens[14]
                if len(tokens) > 15:
                    entry['hsk'] = tokens[15]
                if len(tokens) > 16:
                    entry['ll'] = tokens[16]
                if len(tokens) > 17:
                    entry['zoom'] = tokens[17]
                words.append(entry)
    return words


def main():
    words = LoadWords()
    CheckWords(words)

if __name__ == "__main__":
    main()

