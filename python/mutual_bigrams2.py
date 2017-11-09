# -*- coding: utf-8 -*-

# Check bigrams for presence in CC-CEDICT

from urllib2 import urlopen
from StringIO import StringIO
import codecs
import gzip
import re

from char_util import ToSimplified

line_exp = u"([\w|，|·|、]+)\s([\w|，|·|、]+)\s\[(.*)\]\s"
line_pattern = re.compile(line_exp, re.UNICODE)
sq_brackets_pattern = r"(.+)\[.+\](.*)"
sq_brackets_replace = r"\1 \2"
delimiter_exp = r"[\d\s]*"
delimiter_pattern = re.compile(delimiter_exp)


def get_cedict_definitions(line):
  for i, char in enumerate(line):
    if char == '/':
      begin_index = i + 1
      break
  for i, char in reversed(list(enumerate(line))):
    if char == '/':
      end_index = i
      break
  x = line[begin_index:end_index]
  definitions = x.split('/')
  return definitions


def get_cedict_categ(line):
  definitions = get_cedict_definitions(line)
  try:
    for definition in definitions:
      # This can be expanded to other formats where Buddhism can appear in definitions
      if '(Buddhism)' in definition.split():
        return 'Buddhism'
      if 'disciple' in definition.split():
        return 'person'
      if 'general' in definition.split():
        return 'person'
      if 'King' in definition.split():
        return 'person'
      if 'Emperor' in definition.split():
        return 'person'
      if 'Duke' in definition.split():
        return 'person'
      if 'Prince' in definition.split():
        return 'person'
      if 'statesman' in definition.split():
        return 'person'
      if 'philosopher' in definition.split():
        return 'person'
      if 'chancellor' in definition.split():
        return 'person'
      if 'minister' in definition.split():
        return 'person'
      if 'official' in definition.split():
        return 'person'
      if 'officials' in definition.split():
        return 'person'
      if 'poet' in definition.split():
        return 'person'
      if 'sage' in definition.split():
        return 'person'
      if 'figure' in definition.split():
        return 'person'
      if 'lived' in definition.split():
        return 'person'
      if 'personal name' in definition.split():
        return 'person'
      if 'leader' in definition.split():
        return 'person'
      if 'concubine' in definition.split():
        return 'person'
      if 'wife' in definition.split():
        return 'person'
      if 'actor' in definition.split():
        return 'actor'
      if 'literary' in definition.split():
        return 'literary'
      if 'level' in definition.split() and 'city' in definition.split() :
        return 'lake'
      if 'county' in definition.split():
        return 'county'
      if 'river' in definition.split():
        return 'river'
      if 'lake' in definition.split():
        return 'lake'
      if 'district' in definition.split():
        return 'district'
      if 'university' in definition.split():
        return 'university'
  except IndexError as e:
    return 'other'
  return 'other'


def get_pinyin(trad):
  _, _, pinyin = ToSimplified(trad)
  return pinyin


def get_pinyin_unaccented(pinyin_numbers):
  pinyin = []
  for syllable in delimiter_pattern.split(pinyin_numbers):
    pinyin.append(syllable)
  return (" ").join(pinyin).strip()


def get_wiki_headwords():
  headwords = []
  with codecs.open("zhwiki_hw_trad.txt", "rt", "utf-8") as zhwiki:
    for hw in zhwiki:
      headwords.append(hw.strip())
  print("get_wiki_headwords: found %d wikipedia headwords" % len(headwords))
  return set(headwords)


def parse_entry(line):
  m = line_pattern.match(line)
  entry = {}
  if m == None or len(m.groups()) < 3:
    print(u"parse_entry, not enough fields in {0}".format(line))
    return entry
  entry["traditional"] = m.group(1)
  entry["simplified"] = m.group(2)
  entry["pinyin_unaccented"] = get_pinyin_unaccented(m.group(3))
  entry["pinyin"] = get_pinyin(m.group(1))
  entry["english"] = " / ".join(get_cedict_definitions(line))
  grammar = "noun"
  concept = u"\\N\t\\N"
  domain = u"现代汉语\tModern Chinese"
  if len(entry["traditional"]) > 2:
    grammar = "phrase"
  if len(entry["traditional"]) == 4:
    grammar = "set phrase"
    domain = u"成语\tIdiom"
  if entry["english"].startswith("to "):
  	grammar = "verb"
  categ = get_cedict_categ(line)
  subdomain = u"\\N\t\\N"
  if categ == "Buddhism":
    domain = u"佛教\tBuddhism"
  elif categ == "university":
    grammar = "proper noun"
    concept = u"大学\tUniversity"
    domain = u"教育\tEducation"
    subdomain = u"中国\tChina"
  elif categ == "county":
    grammar = "proper noun"
    concept = u"县\tCounty"
    domain = u"地方\tPlaces"
    subdomain = u"中国\tChina"
  elif categ == "district":
    grammar = "proper noun"
    concept = u"地区\tDistrict"
    domain = u"地方\tPlaces"
    subdomain = u"中国\tChina"
  elif categ == "actor":
    grammar = "proper noun"
    concept = u"人\tPerson"
    domain = u"戏剧\tDrama"
  elif categ == "person":
    grammar = "proper noun"
    concept = u"人\tPerson"
    domain = u"历史\tHistory"
    subdomain = u"中国\tChina"
  elif categ == "literary":
    grammar = "noun"
    domain = u"古文\tClassical Chinese"
  elif categ != "other":
    grammar = "proper noun"
    domain = u"地方\tPlaces"
  entry["grammar"] = grammar
  entry["concept"] = concept
  entry["domain"] = domain
  entry["subdomain"] = subdomain
  return entry

# Process English text definition
#
# Return: a stripped down equivalent
def process_english(english, pinyin_unaccented, grammar):
  english = remove_sq_brackets(english)
  if "(literary)" in english:
    english = english.replace("(literary)","")
  notes = ""
  if grammar == "proper noun":
    # If pinyin_unaccented is a substring of english, split
    index =  english.lower().find(pinyin_unaccented.lower())
    #print(u"process_english {0}, {1}, {2}".format(english, pinyin_unaccented, index))
    if index > -1:
      pos = index + len(pinyin_unaccented)
      notes = english[pos:].lstrip().title()
      #print(u"process_english {0}, {1}, {2}, {3}".format(english, pinyin_unaccented, index, notes))
      return pinyin_unaccented, notes
    pinyin_nospaces = pinyin_unaccented.replace(" ","")
    index =  english.lower().find(pinyin_nospaces.lower())
    if index > -1:
      pos = index + len(pinyin_nospaces)
      notes = english[pos:].lstrip().title()
      #print(u"process_english {0}, {1}, {2}, {3}".format(english, pinyin_nospaces, index, notes))
      return pinyin_nospaces, notes
  return english, ""

# Remove square brackets from the English equivalent
def remove_sq_brackets(english):
  if "[" in english:
    english = re.sub(sq_brackets_pattern, sq_brackets_replace, english)
  if "[" in english:
    english = re.sub(sq_brackets_pattern, sq_brackets_replace, english)
  return english


def main():
  print "Looking for bigrams that are entries in cc-cedict"
  trad_list = []
  temp_dict = {}  # contains mutual bigram info except frequency
  mutual_bigram_info = {}
  luid = 75938
  with codecs.open('cedict_1_0_ts_utf-8_mdbg.txt', 'rt', "utf-8") as cedict, codecs.open('../../hbreader/index/ngram_frequencies.txt', 'rt', "utf-8") as bigram_file:
    for line in cedict:
      if line[0] == '#':
        continue
      trad = line.split()[0]
      trad_list.append(trad)
      temp_dict[trad] = parse_entry(line)
    words = set(trad_list) # bigrams is list, words is the same set
    wiki_hw = get_wiki_headwords()
    with codecs.open("temp.tsv", "w", "utf-8") as f:
      for line in bigram_file:
        info = line.split()
        if info[0] in words:
          luid += 1
          entry = temp_dict[info[0]]
          traditional = info[0]
          simplified = entry["simplified"]
          trad = traditional
          if traditional == simplified:
            trad = "\\N"
          pinyin = entry["pinyin"]
          grammar = entry["grammar"]
          pinyin_unaccented = entry["pinyin_unaccented"]
          english, notes = process_english(entry["english"], pinyin_unaccented, grammar)
          concept = entry["concept"]
          domain = entry["domain"]
          subdomain = entry["subdomain"]
          ref = ""
          if traditional in wiki_hw:
            ref = u"(CC-CEDICT '{0}'; Wikipedia '{1}')".format(traditional, traditional)
          else:
            ref = u"(CC-CEDICT '{0}')".format(traditional)
          if notes != "":
            notes = u"{0} {1}".format(notes, ref)
          else:
            notes = u"{0}".format(ref)
          f.write(u"{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t\\N\t\\N\t{9}\t{10}\n".format(luid,
          	simplified, trad, pinyin, english, grammar, concept, domain, subdomain, notes, luid))


if __name__ == "__main__":
  main()
