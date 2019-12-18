#!/bin/bash
set -ex

BRANCH_TAG=`git rev-parse --abbrev-ref HEAD`

echo "Pushing italiangrid/storm-testsuite:${BRANCH_TAG} on dockerhub ..."
docker push italiangrid/storm-testsuite:${BRANCH_TAG}