# -*- coding: utf-8 -*-
"""
Tests utility for Korean canon metadata management
"""

from taisho import saveScrollFromWeb


def main():
  saveScrollFromWeb(14, "541", 1, u"佛說佛大僧大經")


if __name__ == "__main__": main()