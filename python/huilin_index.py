"""Index the headwords in Hui Lin's 一切經音義 (T 2128).

Reads the 100 fascicles of 'The Sounds and Meanings of all the Terms in the
Canonical Texts' 一切經音義, composed by Hui Lin, from
corpus/taisho/t2128_NN.txt and writes the entries to
data/dictionary/huilin_index.tsv in the NTI Reader dictionary format
documented in data/dictionary/dictionary-readme.md.

A typical entry looks like

  [0312a15]  覆載  (上敷務反見韻英秦音也 ...)  。

where 0312a15 is the location in volume 54 of the Taisho, 覆載 is the headword
and the text in parentheses is the body of the entry. The body may continue
over several lines.

Usage (from the top level directory of the project):

  python3 python/huilin_index.py
"""

import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS_DIR = os.path.join(BASE_DIR, 'corpus', 'taisho')
CNOTES_DICT = os.path.join(BASE_DIR, 'data', 'dictionary',
                           'cnotes_zh_en_dict.tsv')
OUTPUT_FILE = os.path.join(BASE_DIR, 'data', 'dictionary', 'huilin_index.tsv')

NUM_FASCICLES = 100
START_LUID = 9000002
TAISHO_NO = 2128
TAISHO_VOL = 54
TITLE = ("'The Sounds and Meanings of all the Terms in the Canonical Texts' "
         "一切經音義 composed by Hui Lin")
HEADER = ('# Copyright Fo Guang Shan 佛光山 2013-2025. May be reused under the '
          'Creative Commons Attribution-Share Alike 3.0 License (CCASE 3.0), '
          'https://creativecommons.org/licenses/by-sa/3.0/')
NULL = '\\N'

# Line beginning with a Taisho location, e.g. [0312a15]
LOCATION_RE = re.compile(r'^\[(\d{4}[a-c]\d{2})\](.*)$')
# A headword made up only of CJK characters (no gaiji or punctuation)
CJK_RE = re.compile(r'^[㐀-䶿一-鿿豈-﫿'
                    r'\U00020000-\U0003134f]+$')
# Sutra titles and notes on ranges of scrolls, e.g. 緣起聖道經一卷 or
# 從第一百六卷已下至一百二十六卷計二十一卷, rather than headwords
NOT_HEADWORD_RE = re.compile(r'[一二三四五六七八九十百兩]卷$')
# First entry in Fascicle 1 after the prefaces
FIRST_ENTRY_LOC = '0312a10'


def load_trad_to_simp(path):
  """Builds a map from traditional to simplified Chinese from the dictionary.
  """
  t2s = {}
  with open(path, 'r', encoding='utf-8') as f:
    for line in f:
      if line.startswith('#'):
        continue
      fields = line.rstrip('\n').split('\t')
      if len(fields) < 3:
        continue
      simp, trad = fields[1], fields[2]
      if trad == NULL or not trad:
        trad = simp
      if trad not in t2s:
        t2s[trad] = simp
  return t2s


def to_simplified(trad, t2s):
  """Looks up the simplified form of a traditional word.

  Uses the whole word if it is in the dictionary, otherwise converts character
  by character, leaving characters that are not found unchanged.
  """
  if trad in t2s:
    return t2s[trad]
  return ''.join(t2s.get(c, c) for c in trad)


def read_entries(path):
  """Yields (location, text) for each location-marked block in a fascicle.

  Continuation lines (non-blank lines without a location marker) are appended
  to the preceding block.
  """
  loc, parts = None, []
  with open(path, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.strip()
      m = LOCATION_RE.match(line)
      if m:
        if loc:
          yield loc, ''.join(parts)
        loc, parts = m.group(1), [m.group(2)]
      elif not line:
        if loc:
          yield loc, ''.join(parts)
        loc, parts = None, []
      elif loc:
        parts.append(line)
  if loc:
    yield loc, ''.join(parts)


def parse_entry(text):
  """Splits an entry into headword and body, or returns None if not an entry.
  """
  text = re.sub(r'\s+', '', text)
  start = text.find('(')
  end = text.rfind(')')
  if start <= 0 or end < start:
    return None
  headword = text[:start]
  body = text[start + 1:end]
  if not CJK_RE.match(headword) or not body:
    return None
  if NOT_HEADWORD_RE.search(headword):
    return None
  return headword, body


def main():
  t2s = load_trad_to_simp(CNOTES_DICT)
  luid = START_LUID
  skipped = 0
  hwids = {}  # Traditional headword -> headword number of its first entry
  with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
    out.write(HEADER + '\n')
    for n in range(1, NUM_FASCICLES + 1):
      path = os.path.join(CORPUS_DIR, 't2128_{:02d}.txt'.format(n))
      for loc, text in read_entries(path):
        if n == 1 and loc < FIRST_ENTRY_LOC:
          continue  # Introductory material
        entry = parse_entry(text)
        if not entry:
          if '(' in text:
            skipped += 1
          continue
        trad, body = entry
        simp = to_simplified(trad, t2s)
        hwid = hwids.setdefault(trad, luid)
        notes = '{}; from Fascicle {} of {} (T {}, {}.{})'.format(
            body, n, TITLE, TAISHO_NO, TAISHO_VOL, loc)
        fields = [
            str(luid),          # Lexical unit number
            simp,               # Simplified
            trad if trad != simp else NULL,  # Traditional
            NULL,               # Pinyin
            NULL,               # English
            'phrase',           # Part of speech
            NULL, NULL,         # Entry kind (Chinese, English)
            '佛教', 'Buddhism',  # Topic
            NULL, NULL,         # Sub-topic
            NULL,               # Image
            NULL,               # Pronunciation
            notes,              # Notes
            str(hwid),          # Headword number, shared by repeated headwords
        ]
        out.write('\t'.join(fields) + '\n')
        luid += 1
  print('Wrote {} entries to {}, skipped {} with non-standard headwords'.format(
      luid - START_LUID, OUTPUT_FILE, skipped), file=sys.stderr)


if __name__ == '__main__':
  main()
