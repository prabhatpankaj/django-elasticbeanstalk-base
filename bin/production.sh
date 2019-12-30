#!/bin/bash

ts=`date +%s`
fn="$EB_APP_NAME_PROD-$ts.zip"
find ./  -path '*/\.git*' -prune -o -type f -print | zip $fn -@
S3_KEY="$S3_KEY_PROD/$fn"
# Copy the app to S3
aws s3 cp $fn "s3://$S3_BUCKET_PROD/$S3_KEY"

# Create a new version in eb
echo "Creating ElasticBeanstalk Application Version ..."
aws elasticbeanstalk create-application-version \
  --application-name $EB_APP_NAME_PROD \
  --version-label "$EB_APP_NAME_PROD-$ts" \
  --description "$EB_APP_NAME_PROD-$ts" \
  --source-bundle S3Bucket="$S3_BUCKET_PROD",S3Key="$S3_KEY" --auto-create-application

# Update to that version
echo "Updating ElasticBeanstalk Application Version ..."
aws elasticbeanstalk update-environment \
  --application-name $EB_APP_NAME_PROD \
  --environment-name $EB_APP_ENV_PROD \
  --version-label "$EB_APP_NAME_PROD-$ts"

echo "Done! Deployed version $EB_APP_NAME_PROD-$ts"