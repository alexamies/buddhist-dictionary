#!/bin/bash
## Generates the HTML pages for the web site
## Run this from the top level directory of the ntireader.org 
## directory tree
## DEV_HOME should be set to the location of the chinesenotes.com Go lang
## software
## CNREADER_HOME should be set to the location of the ntireader.org directory

export DEV_HOME=../chinesenotes.com
export CNREADER_HOME=`pwd`
export WEB_DIR=web-staging
export TEMPLATE_HOME=html/material-templates
python $DEV_HOME/python/doc_list.py
mkdir $WEB_DIR
mkdir $WEB_DIR/analysis
mkdir $WEB_DIR/analysis/taisho
mkdir $WEB_DIR/dist
mkdir $WEB_DIR/taisho
mkdir $WEB_DIR/images
mkdir $WEB_DIR/script
mkdir $WEB_DIR/words

cd $DEV_HOME/go
source 'path.bash.inc'
cd src/cnreader
./cnreader
./cnreader -hwfiles
./cnreader -html
cd $CNREADER_HOME
mkdir $WEB_DIR/dist
cp web-resources/dist/*.css $WEB_DIR/dist/.
cp web-resources/dist/*.js $WEB_DIR/dist/.
cp web-resources/dist/*.json $WEB_DIR/dist/.
cp web-resources/*.css $WEB_DIR/.
cp web-resources/script/*.js $WEB_DIR/script/.
cp web-resources/*.js $WEB_DIR/.
cp web-resources/images/*.* $WEB_DIR/images/.
