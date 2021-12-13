#!/bin/bash
set -ex

. .env

COMPOSE_OPTS="--ansi never"
TTY_OPTS="${TTY_OPTS:-}"
STORM_TESTSUITE_CONTAINER_NAME="${STORM_TESTSUITE_CONTAINER_NAME:-storm-testsuite}"
OUTPUT_DIRECTORY="${OUTPUT_DIRECTORY:-output}"
SKIP_DOCKER_IMAGES_PULL="${SKIP_DOCKER_IMAGES_PULL:-false}"

# Stop if compose is running
docker-compose ${COMPOSE_OPTS} down
# Pull images from dockerhub
if [[ ${SKIP_DOCKER_IMAGES_PULL} == "false" ]]
then
  docker-compose ${COMPOSE_OPTS} pull
fi

# Run testsuite
docker-compose ${COMPOSE_OPTS} up --no-color storm-testsuite

# Copy Reports
mkdir -p ${OUTPUT_DIRECTORY}
rm -rf ${OUTPUT_DIRECTORY}/*
docker cp ${STORM_TESTSUITE_CONTAINER_NAME}:/home/tester/storm-testsuite/reports ${OUTPUT_DIRECTORY}/

docker-compose ${COMPOSE_OPTS} rm -f -s trust storm-testsuite

docker-compose down
