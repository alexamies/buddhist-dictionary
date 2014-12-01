"""Module to generate output text with gloss from a Chinese text document. ====

The analysis is output in either HTML format with links back to the phrase 
memory and dictionary for each phrase and word in the Chinese text or POS tag 
format.
"""

import codecs
import os.path

from datetime import date

from bdict import app_exceptions
from bdict import cedict
from bdict import cjktextreader
from bdict import chinesephrase
from bdict import configmanager
from bdict import phrasematcher
from bdict import postagger

DEFAULT_OUTFILE_HTML = 'temp.html'
DEFAULT_OUTFILE_POS = 'temp.txt'
HTML_TYPE = 'html'  # Output type
POS_TAGGED_TYPE = 'pos_tagged'  # Output type


class GlossGenerator:
    """Generates a document annotated with English gloss and other information.
   """

    def __init__(self, output_type=HTML_TYPE, wholetext=False, charset='Traditional'):
        """Constructor for GlossGenerator class.

        Args:
          output_type: either 'html' (default) or 'pos_tagged' (tagged part of 
                       speech)
          wholetext: Whether to format the whole source text or only extract 
                     the Chinese characters between the start and end tags
                     (default)
          charset: The character set that the source document is written
                   in, either 'Traditional' (default) or 'Simplified'
        """
        manager = configmanager.ConfigurationManager()
        self.config = manager.LoadConfig()
        self.output_type = output_type
        self.wholetext = wholetext
        self.tagger = postagger.POSTagger(charset=charset)

    def GenerateDoc(self, corpus_entry):
        """Generates output text for the glossed version of the Chinese document.

        Args:
          corpus_entry: the corpus entry for the source document.

        Returns:
          A string with the generated output text.

        Raises:
          BDictException: If the input file does not exist
        """
        markup = ''
        if 'source_name' in corpus_entry:
            source_name = corpus_entry['source_name']
            markup += self._Title2(source_name)
        if self.output_type == HTML_TYPE:
            markup += self._Paragraph('Mouse over Chinese words for English gloss')
        if 'source_name' in corpus_entry:
            source = corpus_entry['source']
            markup += self._Paragraph('Source of document: %s' % source)
        if 'reference' in corpus_entry:
            reference = corpus_entry['reference']
            markup += self._Paragraph('Reference: %s\n' % reference)
        if 'translator' in corpus_entry:
            translator = corpus_entry['translator']
            markup += self._Paragraph('Translator: %s' % translator)
        if 'plain_text' in corpus_entry:
            plain_text = corpus_entry['plain_text']
            # markup += self._Paragraph('Source document: %s' % plain_text)

        reader = cjktextreader.CJKTextReader()
        text = None
        if self.wholetext:
            text = reader.ReadWholeText(corpus_entry)
        else:
            text = reader.ReadText(corpus_entry)
        dictionary = cedict.ChineseEnglishDict()
        wdict = dictionary.OpenDictionary(corpus_entry['charset']) # Word dictionary
        dataset = phrasematcher.PhraseDataset()
        pdict = dataset.Load()
        combined_dict = dict(wdict.items() + pdict.items())
        splitter = chinesephrase.ChineseWordExtractor(combined_dict)
        elements = splitter.ExtractWords(text, leave_punctuation=True, wholetext = self.wholetext)

        previous = None
        for element in elements:
            if element in combined_dict:
                entry = combined_dict[element]
                entry_id = entry['id']
                url = ''
                title = ''
                if 'pos_tagged' in entry: # Phrase
                    markup += self._Phrase(element, entry)
                else: # Word
                    markup += self._Word(element, entry, previous)
                    previous = entry['traditional']
            else:
                markup += self._Punctuation(element)
        markup += self._Timestamp()
        return markup

    def WriteDoc(self, corpus_entry):
        """Generates and writes output text for the glossed version of the Chinese document.

        Args:
          corpus_entry: the corpus entry for the source document.

        Returns:
          The file name that the output text was written to.

        Raises:
          BDictException: If the input file does not exist
        """
        infile = corpus_entry['plain_text']
        period_pos = infile.find('.')
        outfile = DEFAULT_OUTFILE_HTML
        if self.output_type == POS_TAGGED_TYPE:
            outfile = DEFAULT_OUTFILE_POS
            if infile.find('.') > -1:
                outfile = '%s-gen-tagged.txt' % infile[0:period_pos]
            if self._CheckTagDirectory():
                tagged_directory = self._CheckTagDirectory()
                outfile = '%s/%s' % (tagged_directory, outfile)
        elif 'gloss_file' in corpus_entry:
            outfile = corpus_entry['gloss_file']
            if self._CheckGlossDirectory():
                gloss_directory = self._CheckGlossDirectory()
                outfile = '%s/%s' % (gloss_directory, outfile)
        else:
            # Give information about possible problem in corpus entry
            print('gloss_file is not in corpus_entry')
            print('infile: %s' % infile)
            if 'source_name' in corpus_entry:
              print('source_name: %s' % corpus_entry['source_name'])
            else:
              print('source_name: none')
            if 'reference' in corpus_entry:
              print('reference: %s' % corpus_entry['reference'])
            else:
              print('reference: none')
        markup = self.GenerateDoc(corpus_entry)
        with codecs.open(outfile, 'w', "utf-8") as outf:
            outf.write(markup)
            outf.close()
        return outfile

    def _CheckGlossDirectory(self):
        """If the directory does not already exist it will be created.
        """
        dirname = self.config['gloss_directory']
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        return dirname

    def _CheckTagDirectory(self):
        """If the directory does not already exist it will be created.
        """
        dirname = self.config['tagged_directory']
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        return dirname

    def _Paragraph(self, text):
        """Generates output text formatted for a paragraph.
        """
        if self.output_type == POS_TAGGED_TYPE:
            #  return '%s\n\n' % text
            return ''
        return '<p>%s</p>\n' % text

    def _Phrase(self, element_text, phrase_entry):
        """Generates output text formatted for a phrase.
        """
        gloss = phrase_entry['pos_tagged']
        # print('Output for phrase "%s"' % gloss)
        if self.output_type == POS_TAGGED_TYPE:
            tagged_entries = self.tagger.GetTaggedWords(phrase_entry)
            text = ''
            for entry in tagged_entries:
                text += '%s\n' % entry
            return text
        entry_id = phrase_entry['id']
        url = 'phrase_detail.php?id=%s' % entry_id
        return '<a href="%s" \n title="%s">%s</a>' % (url, gloss, element_text)

    def _Punctuation(self, element_text):
        """Generates output text formatted for a punctuation element.
        """
        if self.output_type == POS_TAGGED_TYPE:
            pos = 'PU'
            return '%s/%s\n' % (element_text, pos)
        elif element_text == '\n':
            return '<br/>\n'
        return element_text

    def _Title2(self, text):
        """Generates output text formatted for a level 2 header.
        """
        if self.output_type == POS_TAGGED_TYPE:
            # return '## %s' % text
            return ''
        return '<h2>%s</h2>\n' % text

    def _Timestamp(self):
        """Creates a timestamp if the docs is HTML
        """
        if self.output_type == POS_TAGGED_TYPE:
            return ''
        return '<br/><p>Page last updated on %s.</p>\n' % date.isoformat(date.today())

    def _Word(self, element_text, entry, previous=None):
        """Generates output text formatted for a word.
        """
        # print('_Word element_text = %s' % element_text)
        if self.output_type == POS_TAGGED_TYPE:
            return self.tagger.TagWord(element_text) + '\n'
        most_freq_entry = self.tagger.MostFrequentWord(entry['traditional'], previous)
        if most_freq_entry != None:
            entry = most_freq_entry
        gloss = cedict.GetGloss(entry)
        if not 'id' in entry:
            return element_text
        entry_id = entry['id']
        # print('_Word entry_id = %s' % entry_id)
        url = 'word_detail.php?id=%s' % entry_id
        return '<a href="%s" title="%s">%s</a>' % (url, gloss, element_text)


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

