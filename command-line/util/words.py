"""Command line utility for analysis based on Chinese words. ==================

Reads and processes the words.txt text file. The words may be checked
for consistency and dumped out to file again.
"""
import getopt
import sys

import illustrations


DIR_NAME = '../data/dictionary/'
WORDS_FILE = 'words.txt'
PLACES_FILE = 'places.txt'
HSK_FILE = 'hsk_words.txt'
NEW_WORDS_FILE = 'new_words.txt'


def ExportHSK(entries):
    """Writes HSK words out to the hsk_words file.

    Args:
        entries: List of words have HSK levels.
    """
    fullpath = '%s%s' % (DIR_NAME, HSK_FILE)
    print('Writing %d entries to file %s.' % (len(entries), fullpath))
    with open(fullpath, 'w') as f:
        for entry in entries:
            iden = entry['id']
            simplified = entry['simplified']
            traditional = entry['traditional']
            english = entry['english']
            hsk = entry['hsk']
            f.write('%d\t%s\t%s\t%s\t%s\n' % (iden, simplified, traditional, 
                                                  english, hsk))
        f.close()


def ExportPlaces(places):
    """Writes words that are places out to the place file.

    Args:
        places: List of words that are places.
    """
    print('Writing %d places to file.' % len(places))
    fullpath = '%s%s' % (DIR_NAME, PLACES_FILE)
    with open(fullpath, 'w') as f:
        for place in places:
            iden = place['id']
            simplified = place['simplified']
            traditional = place['traditional']
            english = place['english']
            ll = r'\N'
            zoom = r'\N'
            if 'll' in place and place['ll'].strip():
                ll = place['ll']
            if 'zoom' in place and place['zoom'].strip():
                zoom = place['zoom']
            f.write('%d\t%s\t%s\t%s\t%s\t%s\n' % (iden, simplified, traditional, 
                                                  english, ll, zoom))
        f.close()


def ExportWords(words, image_dict):
    """Exports the words to a file.
    
    Removes additional fields for words (hsk, ll, zoom) and unwanted images. 

    Args:
        words: List of words loaded to write to the file.
        illustrations: List of image entries to cross-check against values in words list
    """
    fullpath = '%s%s' % (DIR_NAME, NEW_WORDS_FILE)
    print('%d words being exported to file %s.' % (len(words), fullpath))
    with open(fullpath, 'w') as f:
        for word in words:
            iden = word['id']
            simplified = word['simplified']
            traditional = word['traditional']
            pinyin = word['pinyin']
            english = word['english']
            grammar = word['grammar']
            concept_cn = word['concept_cn']
            concept_en = word['concept_en']
            topic_cn = word['topic_cn']
            topic_en = word['topic_en']
            parent_cn = word['parent_cn']
            parent_en = word['parent_en']
            image = word['image']
            mp3 = word['mp3']
            notes = word['notes']
            if image not in image_dict:
                image = '\\N'
            f.write('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (iden, simplified, traditional, 
                                                  pinyin, english, grammar, concept_cn,
                                                  concept_en, topic_cn, topic_en,
                                                  parent_cn, parent_en, image, mp3,
                                                  notes))
        f.close()


def GetHSK(words):
    """Get all the words that have a HSK level.
    
    I am in the process of extracting HSK from the main table into a secondary
    table because most of the entries do not have a HSK level, which
    makes it cumbersome to maintain.

    Args:
        words: List of words loaded from the words.txt file.

    Return:
        A list of words that have HSK levels.
    """
    print('%d words being checked.' % len(words))
    entries = []
    for word in words:
        iden = word['id']
        simplified = word['simplified']
        if 'hsk' in word:
            hsk = word['hsk']
            if hsk not in ['1', '2', '3', '4']:
                print('(%d , "%s") has hsk level %s.' % (iden, simplified, hsk))
            else:
                entries.append(word)
    print('Got %d words with HSK levels' % len(entries))
    return entries


def GetPlaces(words):
    """Gets all the words that represent a place.
    
    Determine whether the word is a place based on topic and grammar (proper noun).
    from place names.

    Args:
        words: List of words loaded from the words.txt file.

    Return:
        A list of words that are places.
    """
    print('%d words being checked.' % len(words))
    places = []
    for word in words:
        iden = word['id']
        simplified = word['simplified']
        grammar = word['grammar']
        if 'topic_en' not in word:
            print('(%d , "%s") does not have a topic.' % (iden, simplified))
            continue
        topic_en = word['topic_en']
        if  topic_en in ['Places', 'Geography'] and grammar == 'proper noun':
            # print('(%d , "%s") is a place.' % (iden, simplified))
            places.append(word)
    return places


def LoadWords():
    """Loads the words text file into a list.
    
    Returns:
        A list of words entries.
    """
    fullpath = '%s%s' % (DIR_NAME, WORDS_FILE)
    with open(fullpath, 'r') as f:
        words = []
        for line in f:
            tokens = line.split('\t')
            if tokens:
                entry = {}
                if len(tokens) < 2:
                    continue
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
                    hsk = tokens[15].strip()
                    if hsk and hsk != r'\N':
                        entry['hsk'] = hsk
                if len(tokens) > 16:
                    entry['ll'] = tokens[16]
                if len(tokens) > 17:
                    entry['zoom'] = tokens[17]
                words.append(entry)
    return words


def PrintUsage():
    print('Usage: python words.py command')
    print('where command is one of:')
    print('    export_places: Exports places from word file to %s' % PLACES_FILE)
    print('    export_hsk: Exports words with HSK levels from word file to %s' % HSK_FILE)
    print('    export_words: Exporting words to file %s, cleaning up in the process.' % NEW_WORDS_FILE)


def main():
    """Accepts commands as arguments after the program name.
    """
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["help", "output="])
        if 'export_places' in args:
            print('Exporting places file')
            words = LoadWords()
            places = GetPlaces(words)
            ExportPlaces(places)
        elif 'export_hsk' in args:
            print('Exporting hsk file')
            words = LoadWords()
            entries = GetHSK(words)
            ExportHSK(entries)
        elif 'export_words' in args:
            print('Exporting words to new file')
            words = LoadWords()
            image_dict = illustrations.LoadIllustrationsAsDict()
            ExportWords(words, image_dict)
        else:
            PrintUsage()
            sys.exit(2)
    except getopt.GetoptError as err:
        print str(err)
        PrintUsage()
        sys.exit(2)


if __name__ == "__main__":
    main()

