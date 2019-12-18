#!/bin/bash
set -ex

BRANCH_TAG=`git rev-parse --abbrev-ref HEAD`
docker build --pull=false --rm=true -t italiangrid/storm-testsuite:${BRANCH_TAG} .
