#!/bin/bash
## Push changes from a build server to the production server
## PROD_SERVER should be set to the server name of the production system
if [ -n "$PROD_SERVER" ]; then
  echo "Copying to $PROD_SERVER"
  tar -czf tmp/taisho.tar.gz web/taisho web/analysis/taisho
  tar -czf tmp/words.tar.gz web/words web/analysis
  if [ -n "$PROJECT" -a -n "$ZONE" ]; then
      gcloud compute --project "$PROJECT" copy-files tmp/taisho.tar.gz $PROD_SERVER:/disk1/ntireadertest.org/tmp/ --zone "$ZONE" 
      gcloud compute --project "$PROJECT" copy-files tmp/words.tar.gz $PROD_SERVER:/disk1/ntireadertest.org/tmp/ --zone "$ZONE" 
  else
    echo "Either PROJECT or ZONE is not set"
    exit 1
  fi
else
  echo "PROD_SERVER is not set"
  exit 1
fi