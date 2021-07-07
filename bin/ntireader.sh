#!/bin/bash
## Generates the HTML pages for the web site
## Run this from the top level directory of the ntireader.org 
## directory tree
## DEV_HOME should be set to the location of the chinesenotes.com
## CNREADER_HOME should be set to the location of the ntireader.org directory

export CNREADER_HOME=.
export WEB_DIR=web-staging
export DEV_HOME=../chinesenotes.com
export TEMPLATE_HOME=html/material-templates
PATH=$PATH:$HOME/go/bin
mkdir $WEB_DIR
mkdir $WEB_DIR/analysis
mkdir $WEB_DIR/analysis/manji
mkdir $WEB_DIR/analysis/taisho
mkdir $WEB_DIR/dist
mkdir $WEB_DIR/manji
mkdir $WEB_DIR/taisho
mkdir $WEB_DIR/images
mkdir $WEB_DIR/script
mkdir $WEB_DIR/words

go install github.com/alexamies/cnreader@latest
cnreader
cnreader -hwfiles
cnreader -html
cnreader -tmindex
cnreader -titleindex
mkdir $WEB_DIR/dist
cp web-resources/dist/* $WEB_DIR/dist/.
cp web-resources/script/*.js $WEB_DIR/script/.
cp web-resources/*.js $WEB_DIR/.
cp web-resources/images/*.* $WEB_DIR/images/.
cp corpus/images/*.* $WEB_DIR/images/.

python3 bin/words2json.py "data/dictionary/words.txt,data/dictionary/fgs_mwe.txt,data/dictionary/translation_memory_buddhist.txt,data/dictionary/translation_memory_literary.txt,data/dictionary/buddhist_terminology.txt,data/dictionary/buddhist_named_entities.txt" $WEB_DIR/dist/ntireader.json

python3 bin/tsv2json.py "data/dictionary/words.txt" $WEB_DIR/ntireader_words.json "NTI Reader dictionary" "NTI Reader" "Alex Amies" "Creative Commons Attribution-Share Alike 3.0"
python3 bin/tsv2json.py "data/dictionary/buddhist_named_entities.txt" $WEB_DIR/buddhist_named_entities.json "NTI Reader Buddhist named entities (people, places, text titles, etc)"  "Buddhist named entities" "Alex Amies" "Creative Commons Attribution-Share Alike 3.0"
python3 bin/tsv2json.py "data/dictionary/translation_memory_buddhist.txt" $WEB_DIR/translation_memory_buddhist.json "NTI Reader Buddhist quotations" "Literary Chinese quotations" "Alex Amies" "Creative Commons Attribution-Share Alike 3.0"
python3 bin/tsv2json.py "data/dictionary/fgs_mwe.txt" $WEB_DIR/fgs_mwe.json "Fo Guang Shan Glossary of Humnastic Buddhism" "HB Glossary" "FGS" "Copyright Fo Guang Shan"
python3 bin/tsv2json.py "data/dictionary/translation_memory_literary.txt" $WEB_DIR/translation_memory_literary.json "Chinese Notes literary Chinese quotations" "Literary Chinese quotations" "Alex Amies" "Creative Commons Attribution-Share Alike 3.0"

echo 'ntireader done'