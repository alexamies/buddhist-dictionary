#!/bin/bash
## Push changes from a staging environment to production
if -z $PROD
then
  echo "PROD not set"
  exit 1
else
  echo "Copying to $PROD"
fi