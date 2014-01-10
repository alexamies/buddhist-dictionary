"""Module to parse documents in POS tagged format. ============================

These methods are used by different POS tagging modules
"""


def ParseLine(line):
    element = {'tagged_text': line}
    tokens = line.split('/')
    element_text = tokens[0]
    element['element_text'] = element_text
    if len(tokens) > 1:
        tokens = tokens[1].split('[')
        element['tag'] = tokens[0]
        if len(tokens) > 1:
            tokens = tokens[1].split('|')
            if len(tokens) > 1:
                english = tokens[1]
                pos = english.find(u']')
                if pos > -1:
                    english = english[0:pos]
                element['english'] = english.strip()
    return element

