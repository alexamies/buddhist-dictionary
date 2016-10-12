#!/bin/bash
## Push changes from a build server to the production server
## PROD_SERVER should be set to the server name of the production system
if [ -n "$PROD_SERVER" ]; then
  echo "Copying to $PROD_SERVER"
  tar -czf tmp/taishi.tar.gz web/taisho
  tar -czf tmp/words.tar.gz web/words
  if [ -n "$PROJECT" -a -n "$ZONE" ]; then
      gcloud compute --project "$PROJECT" copy-files tmp/taishi.tar.gz $PROD_SERVER: --zone "$ZONE" 
      gcloud compute --project "$PROJECT" copy-files tmp/words.tar.gz $PROD_SERVER: --zone "$ZONE" 
  else
    echo "Either PROJECT or ZONE is not set"
    exit 1
  fi
else
  echo "PROD_SERVER is not set"
  exit 1
fi