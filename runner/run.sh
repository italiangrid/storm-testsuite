#!/bin/bash
set -ex

outputDir="./output"

COMPOSE_OPTS="--no-ansi"
TTY_OPTS="${TTY_OPTS:-}"

# Clear output directory
rm -rf ${outputDir}

# Create output directory
mkdir -p ${outputDir}/compose-logs

# Stop if compose is running
docker-compose ${COMPOSE_OPTS} down
# Pull images from dockerhub
docker-compose ${COMPOSE_OPTS} pull

# Run testsuite
set +e
docker-compose ${COMPOSE_OPTS} up --no-color storm-testsuite

kill %1 #kill the first background progress: tail

# Save logs
docker-compose ${COMPOSE_OPTS} logs --no-color storm-testsuite >${outputDir}/compose-logs/storm-testsuite.log

docker cp testsuite:/home/tester/storm-testsuite/reports ${outputDir}

# Exit Code
ts_ec=$(docker inspect testsuite -f '{{.State.ExitCode}}')

set -e
docker-compose ${COMPOSE_OPTS} rm -f -s storm-testsuite

exit ${ts_ec}
