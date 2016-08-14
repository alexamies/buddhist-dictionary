#!/bin/bash
## Push changes from staging environment $CNREADER_HOME to production $PROD
## PROD should be set to the location of the production system
## CNREADER_HOME should be set to the location of the staging system
if [ -n "$PROD" ]; then
  echo "Copying to $PROD"
  if [ -n "$CNREADER_HOME" ]; then
  	echo "Copying from $CNREADER_HOME"
  	cp $CNREADER_HOME/web/words/*.html $PROD/web/words/.
  	cp $CNREADER_HOME/web/analysis/*.html $PROD/web/analysis/.
  	cp $CNREADER_HOME/web/analysis/taisho/*.html $PROD/web/analysis/taisho/.
  	cp $CNREADER_HOME/web/taisho/*.html $PROD/web/taisho/.
  	cp $CNREADER_HOME/data/dictionary/*.txt $PROD/data/dictionary/.
    cp $CNREADER_HOME/web/abbreviations.html $PROD/web/.
    cp $CNREADER_HOME/web/corpus.html $PROD/web/.
    cp $CNREADER_HOME/web/references.html $PROD/web/.
    cp $CNREADER_HOME/web/syllables_ipa.html $PROD/web/.
    cp $CNREADER_HOME/web/whatsnew.html $PROD/web/.
  else
    echo "CNREADER_HOME is not set"
    exit 1
  fi
else
  echo "PROD is not set"
  exit 1
fi