# -*- coding: utf-8 -*-
"""
Tests utility for Taisho canon metadata management script
"""

import taisho_contents


def test_convert_to_csv():
  taisho_contents.convert_to_csv()
  tcontents = taisho_contents.load_contents()
  print "Number of entries is %d" % len(tcontents)
  entry = tcontents[u"585"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls" % (entry["volume"],
  	    entry["tid"], entry["title"], entry["nscrolls"])
  entry = tcontents[u"983B"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls" % (entry["volume"],
  	    entry["tid"], entry["title"], entry["nscrolls"])
  entry = tcontents[u"1505"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, compiled_how_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["compiled_how_cn"])
  entry = tcontents[u"1509"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, compiled_how_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["compiled_how_cn"])
  entry = tcontents[u"1512"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, explainedby_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["explainedby_cn"])
  entry = tcontents[u"1519"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, attribution_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["attribution_cn"])
  entry = tcontents[u"1527"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, attribution_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["attribution_cn"])
  entry = tcontents[u"1536"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, attribution_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["attribution_cn"])
  entry = tcontents[u"1566"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, attribution_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["attribution_cn"])
  entry = tcontents[u"1567"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, attribution_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["attribution_cn"])
  entry = tcontents[u"1571"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, attribution_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["attribution_cn"])
  entry = tcontents[u"1572"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, attribution_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["attribution_cn"])
  entry = tcontents[u"1584"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, attribution_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["attribution_cn"])
  entry = tcontents[u"1627"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, attribution_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["attribution_cn"])
  entry = tcontents[u"1606"]
  print u"Title for Volume %d No. %s is %s, in %d scrolls, how_cn %s, attribution_cn %s" % (entry["volume"],
        entry["tid"], entry["title"], entry["nscrolls"], entry["how_cn"], entry["attribution_cn"])


def main():
  test_convert_to_csv()

if __name__ == "__main__": main()