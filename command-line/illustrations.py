"""Command line utility for illustration file management.

Copies files based on the entry in illustrations.txt.
"""
import os.path
import urllib2
from urllib2 import URLError

BASE_URL = 'http://chinesenotes.com/images/'
BASE_DIR = '../web/images/'


def CopyFiles(illustrations):
    """Copies files from the web site to the local system.

    Args:
      illustrations: an array of the illustrations
    """
    for i in illustrations:
        WriteFile(i['medium_resolution'])
        if 'high_resolution' in i:
            WriteFile(i['high_resolution'])


def LoadIllustrations():
    """Loads the illustrations text file into a list.
    
    Returns:
        A list of illustration entries.
    """
    dirname = '../data/dictionary/'
    filename = 'illustrations.txt'
    fullpath = '%s%s' % (dirname, filename)
    f = open(fullpath, 'r')
    illustrations = []
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
            illustrations.append(entry)
    return illustrations


def LoadIllustrationsAsDict():
    """Loads the illustrations text file into a dictionary.

    The medium_resolution field is used as the key for the entries.
    
    Returns:
        A dictionary of illustration entries.
    """
    dirname = '../data/dictionary/'
    filename = 'illustrations.txt'
    fullpath = '%s%s' % (dirname, filename)
    f = open(fullpath, 'r')
    image_dict = {}
    for line in f:
        tokens = line.split('\t')
        if tokens:
            entry = {}
            medium_resolution = tokens[0]
            entry['medium_resolution'] = medium_resolution
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
            image_dict[medium_resolution] = entry
    return image_dict


def WriteFile(imagename):
    if (imagename.find(r'\N') == -1) and (not os.path.isfile(imagename)):
        try:
            url = '%s%s' % (BASE_URL, imagename)
            filename = '%s%s' % (BASE_DIR, imagename)
            response = urllib2.urlopen(url)
            image = response.read()
            with open(filename, 'w') as f:
                f.write(image)
        except URLError as e:
            print("Problem copying imagename '%s', reason: %s" % (imagename, e.reason))

"""Command line entry point.

No command line arguments are supported yet.
"""
def main():
    illustrations = LoadIllustrations()
    CopyFiles(illustrations)


if __name__ == "__main__":
    main()

