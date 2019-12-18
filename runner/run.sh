#!/bin/bash
set -ex

outputDir="reports"
COMPOSE_OPTS="--no-ansi"
STORM_TESTSUITE_CONTAINER_NAME="${STORM_TESTSUITE_CONTAINER_NAME:-storm-testsuite}"
TTY_OPTS="${TTY_OPTS:-}"

# Stop if compose is running
docker-compose ${COMPOSE_OPTS} down
# Pull images from dockerhub
docker-compose ${COMPOSE_OPTS} pull

# Run testsuite
docker-compose ${COMPOSE_OPTS} up --no-color storm-testsuite

# Copy Reports
mkdir ${OUTPUT_DIRECTORY}
docker cp ${STORM_TESTSUITE_CONTAINER_NAME}:/home/tester/storm-testsuite/reports ${OUTPUT_DIRECTORY}/

docker-compose ${COMPOSE_OPTS} rm -f -s trust storm-testsuite
