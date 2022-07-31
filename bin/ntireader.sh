#!/bin/bash
## Generates the HTML pages for the web site
## Run this from the top level directory of the ntireader.org 
## directory tree

# Make the directory structure needed for generated files
export CNREADER_HOME=$PWD
export WEB_DIR=web-staging
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

# Combine bibliographic notes from different sections of the Taisho
BIB=data/bibliographical_notes
A=taisho_agama_section
AB=taisho_abhidharma_section
C=taisho_compilation_section
E=taisho_agama_section
H=taisho_history_bio_section
J=taisho_jataka_avadana_section
L=taisho_lotus_huayan_section
M=taisho_misc_section
MY=taisho_madhyamaka_section
P=taisho_prajnaparamita_section
R=taisho_ratnakuta_nirvana_section
S=taisho_sastra_section
SA=taisho_sastra_abhi_section
SC=taisho_sutra_commentary_section
SCS=taisho_sc_schools_section
SSC=taisho_sastra_commentary_section
T=taisho_treatises_section
V=taisho_vinaya_section
VC=taisho_various_schools_section
Y=taisho_yogacara_section
cat ${BIB}/${A}_ref2file.csv \
  ${BIB}/${J}_ref2file.csv \
  ${BIB}/${P}_ref2file.csv \
  ${BIB}/${L}_ref2file.csv \
  ${BIB}/${R}_ref2file.csv \
  ${BIB}/${C}_ref2file.csv \
  ${BIB}/${M}_ref2file.csv \
  ${BIB}/${E}_ref2file.csv \
  ${BIB}/${V}_ref2file.csv \
  ${BIB}/${S}_ref2file.csv \
  ${BIB}/${SA}_ref2file.csv \
  ${BIB}/${AB}_ref2file.csv \
  ${BIB}/${MY}_ref2file.csv \
  ${BIB}/${Y}_ref2file.csv \
  ${BIB}/${T}_ref2file.csv \
  ${BIB}/${SC}_ref2file.csv \
  ${BIB}/${SSC}_ref2file.csv \
  ${BIB}/${SCS}_ref2file.csv \
  ${BIB}/${VC}_ref2file.csv \
  ${BIB}/${H}_ref2file.csv > ${BIB}/ref2file.csv 
cat ${BIB}/${A}_english_translations.csv \
  ${BIB}/${J}_english_translations.csv \
  ${BIB}/${P}_english_translations.csv \
  ${BIB}/${L}_english_translations.csv \
  ${BIB}/${R}_english_translations.csv \
  ${BIB}/${C}_english_translations.csv \
  ${BIB}/${M}_english_translations.csv \
  ${BIB}/${E}_english_translations.csv \
  ${BIB}/${V}_english_translations.csv \
  ${BIB}/${S}_english_translations.csv \
  ${BIB}/${SA}_english_translations.csv \
  ${BIB}/${AB}_english_translations.csv \
  ${BIB}/${MY}_english_translations.csv \
  ${BIB}/${Y}_english_translations.csv \
  ${BIB}/${T}_english_translations.csv \
  ${BIB}/${SC}_english_translations.csv \
  ${BIB}/${SSC}_english_translations.csv \
  ${BIB}/${SCS}_english_translations.csv \
  ${BIB}/${VC}_english_translations.csv \
  ${BIB}/${H}_english_translations.csv > ${BIB}/english_translations.csv 
cat ${BIB}/${A}_parallels.csv \
  ${BIB}/${J}_parallels.csv \
  ${BIB}/${P}_parallels.csv \
  ${BIB}/${L}_parallels.csv \
  ${BIB}/${R}_parallels.csv \
  ${BIB}/${C}_parallels.csv \
  ${BIB}/${M}_parallels.csv \
  ${BIB}/${E}_parallels.csv \
  ${BIB}/${V}_parallels.csv \
  ${BIB}/${S}_parallels.csv \
  ${BIB}/${SA}_parallels.csv \
  ${BIB}/${AB}_parallels.csv \
  ${BIB}/${MY}_parallels.csv \
  ${BIB}/${Y}_parallels.csv \
  ${BIB}/${Y}_parallels.csv \
  ${BIB}/${SC}_parallels.csv \
  ${BIB}/${SSC}_parallels.csv > ${BIB}/parallels.csv 

# General HTML pages
go install github.com/alexamies/cnreader@latest
cnreader
cnreader -hwfiles
cnreader -html
cnreader -tmindex
# cnreader -titleindex
mkdir $WEB_DIR/dist
cp web-resources/dist/* $WEB_DIR/dist/.
cp web-resources/script/*.js $WEB_DIR/script/.
cp web-resources/*.js $WEB_DIR/.
cp web-resources/images/*.* $WEB_DIR/images/.
cp corpus/images/*.* $WEB_DIR/images/.

python3 bin/words2json.py "data/dictionary/cnotes_zh_en_dict.tsv,data/dictionary/fgs_mwe.txt,data/dictionary/translation_memory_buddhist.txt,data/dictionary/translation_memory_literary.txt,data/dictionary/buddhist_terminology.txt,data/dictionary/buddhist_named_entities.txt" $WEB_DIR/dist/ntireader.json
cd $WEB_DIR/dist && rm -f ntireader.json.gz && gzip ntireader.json && cd $CNREADER_HOME

python3 bin/tsv2json.py "data/dictionary/cnotes_zh_en_dict.tsv" $WEB_DIR/ntireader_words.json "NTI Reader dictionary" "NTI Reader" "Alex Amies" "Creative Commons Attribution-Share Alike 3.0"
python3 bin/tsv2json.py "data/dictionary/buddhist_named_entities.txt" $WEB_DIR/buddhist_named_entities.json "NTI Reader Buddhist named entities (people, places, text titles, etc)"  "Buddhist named entities" "Alex Amies" "Creative Commons Attribution-Share Alike 3.0"
python3 bin/tsv2json.py "data/dictionary/translation_memory_buddhist.txt" $WEB_DIR/translation_memory_buddhist.json "NTI Reader Buddhist quotations" "Literary Chinese quotations" "Alex Amies" "Creative Commons Attribution-Share Alike 3.0"
python3 bin/tsv2json.py "data/dictionary/fgs_mwe.txt" $WEB_DIR/fgs_mwe.json "Fo Guang Shan Glossary of Humnastic Buddhism" "HB Glossary" "FGS" "Copyright Fo Guang Shan"
python3 bin/tsv2json.py "data/dictionary/translation_memory_literary.txt" $WEB_DIR/translation_memory_literary.json "Chinese Notes literary Chinese quotations" "Literary Chinese quotations" "Alex Amies" "Creative Commons Attribution-Share Alike 3.0"

echo 'ntireader done'