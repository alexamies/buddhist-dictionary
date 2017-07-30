#!/bin/bash
## Push changes from a build server to either GCS or the production server
## PROD_SERVER should be set to the server name of the production system OR
## BUCKET should be set to the name of the GCS bucket to store the generated
## files
if [ -n "$PROD_SERVER" ]; then
  echo "Copying to server $PROD_SERVER"
  mkdir -p tmp
  tar -czf tmp/taisho.tar.gz web/taisho web/analysis/taisho
  tar -czf tmp/words.tar.gz web/words web/analysis
  if [ -n "$PROJECT" -a -n "$ZONE" ]; then
      gcloud compute --project "$PROJECT" scp tmp/taisho.tar.gz $PROD_SERVER:/disk1/ntireadertest.org/tmp/ --zone "$ZONE" 
      gcloud compute --project "$PROJECT" scp tmp/words.tar.gz $PROD_SERVER:/disk1/ntireadertest.org/tmp/ --zone "$ZONE" 
  else
    echo "Failed: Either PROJECT or ZONE is not set, please set both"
    exit 1
  fi
elif [ -n "$BUCKET" ]; then
  echo "Copying to GCS bucket $BUCKET"
  mkdir -p tmp
  tar -czf tmp/taisho.tar.gz web/taisho web/analysis/taisho
  tar -czf tmp/words.tar.gz web/words web/analysis
  gsutil cp tmp/taisho.tar.gz gs://$BUCKET
  gsutil cp tmp/words.tar.gz gs://$BUCKET
  gsutil cp index/ngram_frequencies.txt gs://$BUCKET
else
  echo "Failed: Both BUCKET and PROD_SERVER are not set, please set either one"
  exit 1
fi