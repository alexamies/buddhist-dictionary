#!/bin/bash
## Pull changes from a GCS bucket
## BUCKET should be set to the name of the GCS bucket to store the generated
if [ -n "$BUCKET" ]; then
  echo "Copying from GCS bucket $BUCKET"
  gsutil cp gs://$BUCKET/taisho.tar.gz tmp/.
  tar -xzf tmp/taisho.tar.gz web/taisho web/analysis/taisho
  mv tmp/web/taisho/*.html web/taisho/.
  gsutil cp gs://$BUCKET/words.tar.gz tmp/.
  tar -xzf tmp/words.tar.gz web/words web/analysis
  mv tmp/web/words/*.html web/words/.
  mv tmp/web/analysis/*.html web/analysis/.
else
  echo "Failed: BUCKET is not set, please set it to the name of the GCS bucket"
  exit 1
fi