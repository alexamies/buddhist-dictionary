#!/bin/bash
## Push changes from staging environment $CNREADER_HOME to production $PROD
if [ -n "$PROD" ]; then
  echo "Copying to $PROD"
  if [ -n "$CNREADER_HOME" ]; then
  	echo "Copying from $CNREADER_HOME"
  	cp $CNREADER_HOME/web/words/*.html $PROD/web/words/.
  	cp $CNREADER_HOME/web/analysis/*.html $PROD/web/analysis/.
  	cp $CNREADER_HOME/web/analysis/taisho/*.html $PROD/web/analysis/taisho/.
  	cp $CNREADER_HOME/web/taisho/*.html $PROD/web/taisho/.
  	cp $CNREADER_HOME/data/dictionary/*.txt $PROD/data/dictionary/.
  else
    echo "CNREADER_HOME is not set"
    exit 1
  fi
else
  echo "PROD is not set"
  exit 1
fi