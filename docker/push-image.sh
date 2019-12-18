#!/bin/bash
set -ex

if [ -n "${DOCKER_REGISTRY_HOST}" ]; then

    BRANCH_TAG=`git rev-parse --abbrev-ref HEAD`
    docker tag italiangrid/storm-testsuite:${BRANCH_TAG} ${DOCKER_REGISTRY_HOST}/italiangrid/storm-testsuite:${BRANCH_TAG}
    docker push ${DOCKER_REGISTRY_HOST}/italiangrid/storm-testsuite:${BRANCH_TAG}

fi
