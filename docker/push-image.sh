#!/bin/bash
set -ex

if [ -n "${DOCKER_REGISTRY_HOST}" ]; then

    docker tag italiangrid/storm-testsuite:${BRANCH_NAME} ${DOCKER_REGISTRY_HOST}/italiangrid/storm-testsuite:${BRANCH_NAME}
    docker push ${DOCKER_REGISTRY_HOST}/italiangrid/storm-testsuite:${BRANCH_NAME}

fi
