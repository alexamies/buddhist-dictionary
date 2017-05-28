#!/bin/bash
## Push changes from staging environment $CNREADER_HOME to production $PROD
## PROD should be set to the location of the production system
## CNREADER_HOME should be set to the location of the staging system
## An assumption is that that this is all on the same server
if [ -n "$PROD" ]; then
  echo "Copying to $PROD"
  if [ -n "$CNREADER_HOME" ]; then
  	echo "Copying from $CNREADER_HOME"
  	cp $CNREADER_HOME/web/words/1*.html $PROD/web/words/.
    cp $CNREADER_HOME/web/words/2*.html $PROD/web/words/.
    cp $CNREADER_HOME/web/words/3*.html $PROD/web/words/.
    cp $CNREADER_HOME/web/words/4*.html $PROD/web/words/.
    cp $CNREADER_HOME/web/words/5*.html $PROD/web/words/.
    cp $CNREADER_HOME/web/words/6*.html $PROD/web/words/.
    cp $CNREADER_HOME/web/words/7*.html $PROD/web/words/.
    cp $CNREADER_HOME/web/words/8*.html $PROD/web/words/.
    cp $CNREADER_HOME/web/words/9*.html $PROD/web/words/.
  	cp $CNREADER_HOME/web/analysis/*.html $PROD/web/analysis/.
  	cp $CNREADER_HOME/web/analysis/taisho/*.html $PROD/web/analysis/taisho/.
  	cp $CNREADER_HOME/web/taisho/*.html $PROD/web/taisho/.
  	cp $CNREADER_HOME/data/dictionary/*.* $PROD/data/dictionary/.
    cp $CNREADER_HOME/web/*.html $PROD/web/.
    cp $CNREADER_HOME/web/*.css $PROD/web/.
    cp $CNREADER_HOME/web/script/*.js $PROD/web/script/.
  else
    echo "CNREADER_HOME is not set"
    exit 1
  fi
else
  echo "PROD is not set"
  exit 1
fi