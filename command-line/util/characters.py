"""Command line utility for character-based analysis.

Reads and processes the characters.txt text file.
"""

DIR_NAME = '../data/dictionary/'

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
                entry['medium_resolution'] = tokens[0]
                if len(tokens) > 1:
                    entry['title_zh_cn'] = tokens[1]
                if len(tokens) > 2:
                    entry['title_en'] = tokens[2]
                if len(tokens) > 3:
                    entry['author'] = tokens[3]
                if len(tokens) > 4:
                    entry['license'] = tokens[4]
                if len(tokens) > 5:
                    entry['high_resolution'] = tokens[5]
                characters.append(entry)
    return characters


def main():
    characters = LoadCharacters()
    print('%d characters loaded.' % len(characters))


if __name__ == "__main__":
    main()

