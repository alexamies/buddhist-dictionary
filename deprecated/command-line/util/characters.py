"""Command line utility for character-based analysis. =========================

Reads and processes the characters.txt text file. The characters may be checked
for consistency and dumped out to file again.
"""

DIR_NAME = '../data/dictionary/'


def CheckCharacters(characters):
    """Checks the characters for consistency.
    
    The characters may be loaded from the characters.txt and checked for 
    consistency. For example, each character string should have a length of one.

    Args:
        characters: List of characters loaded from the characters.txt file.
    """
    print('%d characters being checked.' % len(characters))
    problems = []
    for character in characters:
        c = character['c'].decode("utf-8")
        uni = character['unicode']
        if len(c) > 1:
            print('(%d , "%s") has a string length of %d.' % (uni, c, len(c)))
            problems.append(c)
    print('%d problems found.' % len(problems))


def LoadCharacters():
    """Loads the characters text file into a list.
    
    Returns:
        A list of characters entries.
    """
    filename = 'characters.txt'
    fullpath = '%s%s' % (DIR_NAME, filename)
    with open(fullpath, 'r') as f:
        characters = []
        for line in f:
            tokens = line.split('\t')
            if tokens:
                entry = {}
                entry['unicode'] = int(tokens[0])
                if len(tokens) > 1:
                    entry['c'] = tokens[1]
                if len(tokens) > 2:
                    entry['pinyin'] = tokens[2]
                if len(tokens) > 3:
                    entry['radical'] = tokens[3]
                if len(tokens) > 4:
                    entry['strokes'] = tokens[4]
                if len(tokens) > 5:
                    entry['other_strokes'] = tokens[5]
                if len(tokens) > 6:
                    entry['english'] = tokens[6]
                if len(tokens) > 7:
                    entry['notes'] = tokens[7]
                if len(tokens) > 8:
                    entry['type'] = tokens[8]
                characters.append(entry)
    return characters


def main():
    characters = LoadCharacters()
    CheckCharacters(characters)

if __name__ == "__main__":
    main()

