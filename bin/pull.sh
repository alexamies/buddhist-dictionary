#!/bin/bash
## Pull changes from a GCS bucket
## BUCKET should be set to the name of the GCS bucket to store the generated
if [ -n "$BUCKET" ]; then
  echo "Copying to GCS bucket $BUCKET"
  tar -xzf tmp/taisho.tar.gz web/taisho web/analysis/taisho
  mv tmp/web/taisho/*.html web/taisho/.
  tar -xzf tmp/words.tar.gz web/words web/analysis
  mv tmp/web/words/*.html web/words/.
else
  echo "Failed: BUCKET is not set, please set it to the name of the GCS bucket"
  exit 1
fi