# -*- coding: utf-8 -*-

from urllib2 import urlopen
from StringIO import StringIO
import codecs
import gzip
import re

from char_util import ToSimplified


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
      # The following must be in order of lowest to highest index required, or else IndexError could be thrown too early
      if definitions[0].split()[1].lower() == 'county':
        return 'county'
      if definitions[0].split()[1].lower() == 'river':
        return 'river'
      if definitions[0].split()[1].lower() == 'lake' or definitions[0].split()[0] == 'Lake':
        return 'lake'
      if definitions[0].split()[2].lower() == 'level' and definitions[0].split()[3].lower() == 'city':
        return 'city'
      if definitions[0].split()[1].lower() == 'district' and definitions[0].split()[4].lower() == 'city':
        return 'district'
      if definitions[0].split()[1].lower() == 'university' and definitions[0].split()[4].lower() == 'university':
        return 'university'
  except IndexError as e:
    return 'other'
  return 'other'


def get_pinyin(trad):
  _, _, pinyin = ToSimplified(trad)
  return pinyin


def parse_entry(line):
  tokens = re.split(' ', line)
  entry = {}
  entry["traditional"] = tokens[0]
  entry["simplified"] = tokens[1]
  entry["pinyin"] = get_pinyin(tokens[0])
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
  if categ == "Buddhism":
    domain = u"佛教\tBuddhism"
  elif categ == "university":
    grammar = "proper noun"
    concept = u"大学\tUniversity"
    domain = u"教育\tEducation"
  elif categ == "county":
    grammar = "proper noun"
    concept = u"县\tCounty"
    domain = u"地方\tPlaces"
  elif categ == "district":
    grammar = "proper noun"
    concept = u"地区\District"
    domain = u"地方\tPlaces"
  categ != "other":
    grammar = "proper noun"
    domain = u"地方\tPlaces"
  entry["grammar"] = grammar
  entry["concept"] = concept
  entry["domain"] = domain
  return entry


def main():
  print "Looking for bigrams that are entries in cc-cedict"
  trad_list = []
  temp_dict = {}  # contains mutual bigram info except frequency
  mutual_bigram_info = {}
  luid = 66857
  with codecs.open('cedict_1_0_ts_utf-8_mdbg.txt', 'rt', "utf-8") as cedict, codecs.open('../index/ngram_frequencies.txt', 'rt', "utf-8") as bigram_file:
    for line in cedict:
      if line[0] == '#':
        continue
      trad = line.split()[0]
      trad_list.append(trad)
      temp_dict[trad] = parse_entry(line)
    words = set(trad_list) # bigrams is list, words is the same set
    with codecs.open('temp.txt', 'w', "utf-8") as f:
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
          english = entry["english"]
          grammar = entry["grammar"]
          concept = entry["concept"]
          domain = entry["domain"]
          f.write(u"{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t\\N\t\\N\t\\N\t\\N\t(CC-CEDICT '{8}')\t{9}\n".format(luid,
          	simplified, trad, pinyin, english, grammar, concept, domain, traditional, luid))


if __name__ == "__main__":
  main()
