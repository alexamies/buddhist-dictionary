"""Module to HTML with mouseover gloss from a Chinese text document. ==========

The analysis is output in HTML format with links back to the phrase memory and
dictionary for each phrase and word in the Chinese text.
"""

import codecs

from bdict import app_exceptions
from bdict import cedict
from bdict import cjktextreader
from bdict import chinesephrase
from bdict import phrasematcher

DEFAULT_OUTFILE = 'temp.html'


class HTMLGlossGenerator:
    """Generates the HTML document.
   """

    def GenerateDoc(self, corpus_entry):
        """Generates HTML text for the glossed version of the Chinese document.

        Args:
          corpus_entry: the corpus entry for the source document.

        Returns:
          A string with the generated HTML

        Raises:
          BDictException: If the input file does not exist
        """
        html = ''
        if 'source_name' in corpus_entry:
            source_name = corpus_entry['source_name']
            html += '<h2>English gloss for source document %s</h2>\n' % source_name
        if 'source_name' in corpus_entry:
            source = corpus_entry['source']
            html += '<p>Source of document: %s</p>\n' % source
        if 'reference' in corpus_entry:
            reference = corpus_entry['reference']
            html += '<p>Reference: %s</p>\n' % reference
        if 'translator' in corpus_entry:
            translator = corpus_entry['translator']
            html += '<p>Translator: %s</p>\n' % translator

        reader = cjktextreader.CJKTextReader()
        text = reader.ReadText(corpus_entry)
        dictionary = cedict.ChineseEnglishDict()
        wdict = dictionary.OpenDictionary() # Word dictionary
        dataset = phrasematcher.PhraseDataset()
        pdict = dataset.Load()
        combined_dict = dict(wdict.items() + pdict.items())
        splitter = chinesephrase.ChineseWordExtractor(combined_dict)
        elements = splitter.ExtractWords(text)

        html += '<script>elements = ' + _GenerateJSON(elements, combined_dict) + ';</script>'

        for element in elements:
            entry = combined_dict[element]
            entry_id = entry['id']
            cname = 'word'
            if 'chinese_phrase' in entry:
                cname = 'phrase'
            html += '<span id="%s" \nclass="%s">%s</span>' % (entry_id, cname, element)

        return html

    def WriteDoc(self, corpus_entry, outfile=DEFAULT_OUTFILE):
        """Generates and writes HTML text for the glossed version of the Chinese document.

        Args:
          corpus_entry: the corpus entry for the source document.
          outfile: the file to write the HTML to

        Returns:
          A string with the generated HTML

        Raises:
          BDictException: If the input file does not exist
        """
        print('Writing HTML output to file %s' % outfile)
        html = self.GenerateDoc(corpus_entry)
        with codecs.open(outfile, 'w', "utf-8") as outf:
            outf.write(html)
            outf.close()


def _GenerateJSON(elements, combined_dict):
    """Generates dictionary data out in json format.
 
    Args:
        entries: a list of word and phrase entries
        combined_dict: combined dictionary of words and phrases

    Returns:
        A JSON formatted string
    """
    json = '['
    for i in range(len(elements)):
        entry = combined_dict[elements[i]]
        json += '{'
        j = 0
        for key in entry.keys():
            if entry[key] == '\\N':
                json += '"%s": ""' % (key)
            else:
                json += '"%s": "%s"' % (key, entry[key])
            if j != len(entry.keys()) - 1:
                json += ','
            j += 1
        json += '}\n'
        if i != len(elements) - 1:
            json += ',\n'
    json += ']'
    return json

