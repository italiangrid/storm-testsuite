#!/bin/bash
set -ex

echo "Pushing italiangrid/storm-testsuite:${BRANCH_NAME} on dockerhub ..."
docker push italiangrid/storm-testsuite:${BRANCH_NAME}
