"""Module to build a sequence of CJK characters from a corpus text file. =============

The corpus table is used to find the location of the text file and start and end 
markers. CJK punctuation is retained but other, non-CJK characters are removed.
Line breaks are removed.
"""
import codecs
import os.path

from bdict import app_exceptions
from bdict import chinesephrase
from bdict import configmanager
from bdict import htmldoc


class CJKTextReader:
    """Reads the text file into a string of CJK characters.

    """

    def __init__(self):
        """Constructor for CJKTextReader class.
        """
        manager = configmanager.ConfigurationManager()
        self.config = manager.LoadConfig()

    def ReadText(self, corpus_entry):
        """Reads the given corpus entry into memory.

        This method scans to the start of the document as defined by the start marker in
        the corpus table and ignores text including and after the end marker. Within
        the body of the text non-Chinese characters are stripped.

        Args:
          corpus_entry: the corpus entry that contains the source file and other
                        information
          
        Returns:
          A string of CJK characters.

        Raises:
          BDictException: If the input file does not exist
        """
        lines = []
        if 'type' in corpus_entry and corpus_entry['type'] == 'web':
            doc_url = corpus_entry['plain_text']
            print('Reading from URL %s ' % doc_url)
            strings = htmldoc.readWebToPlainStrings(doc_url)
            line = ''.join(strings)
            lines.append(line)
            print('Characters read %d ' % len(line))
        elif 'type' in corpus_entry and corpus_entry['type'] == 'file':
            directory = self.config['corpus_directory']
            infile = corpus_entry['plain_text']
            fullpath = '%s/%s' % (directory, infile)
            if not os.path.isfile(fullpath):
                raise app_exceptions.BDictException('%s is not a file' % infile)
            with codecs.open(fullpath, 'r', "utf-8") as f:
                # print('Reading input file %s ' % fullpath)
                for line in f:
                    lines.append(line)
        else:
            print('Not sure how to read entry %s with type %s.  ' % 
                  (corpus_entry['source_name'], corpus_entry['type']))
            raise app_exceptions.BDictException()

        found_start = False
        start_marker = None
        if 'start' in corpus_entry:
            start_marker = corpus_entry['start']
        else:
            found_start = True
        print('Start marker: %s ' % start_marker)
        end_marker = None
        if 'end' in corpus_entry:
            end_marker = corpus_entry['end']
        print('End marker: %s ' % end_marker)
        text = ''
        found_end = False

        for input_str in lines:
            if not found_start:
                # Look for start marker
                pos = input_str.find(start_marker)
                if pos != -1:
                    found_start = True
                    input_str = input_str[pos:]
                    print('CJKTextReader.ReadText start_marker: %s found' % start_marker)
                else:
                    continue
            if found_end:
                break;
            if end_marker:
                # print('CJKTextReader.ReadText scanning string %s' % input_str)
                end_pos = input_str.find(end_marker)
                if end_pos > -1:
                    input_str = input_str[0:end_pos]
                    found_end = True
                    # print('CJKTextReader.ReadText end_marker: %s found' % end_marker)
            cjk = ''
            for c in input_str:
                if chinesephrase.isCJKLetter(c) or chinesephrase.isCJKPunctuation(c):
                    cjk += c
            text += cjk
        return text

    def ReadWholeText(self, corpus_entry):
        """Reads whole text of the given corpus entry into memory.

        This method ignores the start and end markers in the corpus table, reading in the 
        whole text into memory. Non-Chinese characters within the body are retained.

        Args:
          corpus_entry: the corpus entry that contains the source file and other
                        information

        Returns:
          A string of text.

        Raises:
          BDictException: If the input file does not exist
        """
        strings = []
        if 'type' in corpus_entry and corpus_entry['type'] == 'web':
            doc_url = corpus_entry['plain_text']
            return htmldoc.readWebToPlainText(doc_url)

        directory = self.config['corpus_directory']
        infile = corpus_entry['plain_text']
        fullpath = '%s/%s' % (directory, infile)
        if not os.path.isfile(fullpath):
            raise app_exceptions.BDictException('%s is not a file' % infile)

        with codecs.open(fullpath, 'r', "utf-8") as f:
            # print('ReadWholeText: Reading input file %s ' % fullpath)
            text = ''
            for line in f:
                text += line
        return text

