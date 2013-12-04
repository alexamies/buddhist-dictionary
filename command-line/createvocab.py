"""Command line to compile a vocabulary from a text file.

"""
def main():
    dirname = '../data/dictionary/'
    filename = 'sanskrit.txt'
    print('Compiling vocabulary from file: %s%s' % (dirname, filename))
    fullpath = '%s%s' % (dirname, filename)
    f = open(fullpath, 'r')
    count = 0
    for line in f:
        count += 1
    print('Sanskrit entries: %d' % count)

if __name__ == "__main__":
    main()

