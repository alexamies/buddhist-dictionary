"""Module to loads the Chinese to English dictionary. =========================

The dictionary is loaded into a dict structure
"""
import codecs

DICT_FILE_NAME = '../data/dictionary/words.txt'


class ChineseEnglishDict:
    """loads the Chinese to English dictionary.

    """

    def _OpenDictionary(self):
        """Reads the dictionary into memory
        """
        wdict = {}
        with codecs.open(DICT_FILE_NAME, 'r', "utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                fields = line.split('\t')
                if fields and len(fields) >= 10:
                    entry = {}
                    entry['id'] = fields[0]
                    entry['simplified'] = fields[1]
                    entry['traditional'] = fields[2]
                    entry['pinyin'] = fields[3]
                    entry['english'] = fields[4]
                    entry['grammar'] = fields[5]
                    traditional = entry['traditional']
                    if traditional == '\\N':
                        traditional = entry['simplified']
                    wdict[traditional] = entry
        return wdict

