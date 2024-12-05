#!/bin/bash
set -x

# Build variables
VARIABLES="--variable backendHost:${STORM_BACKEND_HOSTNAME}"
VARIABLES="$VARIABLES --variable storageAreaRoot:${STORM_STORAGE_ROOT_DIRECTORY}"
VARIABLES="$VARIABLES --variable webdavHost:${STORM_WEBDAV_HOSTNAME}"
VARIABLES="$VARIABLES --variable webdavPort:${STORM_WEBDAV_PORT}"
VARIABLES="$VARIABLES --variable webdavSecurePort:${STORM_WEBDAV_SECURE_PORT}"
VARIABLES="$VARIABLES --variable frontendHost:${STORM_FRONTEND_HOSTNAME}"
VARIABLES="$VARIABLES --variable frontendPort:${STORM_FRONTEND_PORT}"

# Wait for StoRM services
WAIT_TIMEOUT=${WAIT_TIMEOUT:-600}

chmod +x /assets/scripts/wait-for-it.sh
/assets/scripts/wait-for-it.sh ${STORM_WEBDAV_HOSTNAME}:${STORM_WEBDAV_PORT} --timeout=${WAIT_TIMEOUT}
/assets/scripts/wait-for-it.sh ${STORM_FRONTEND_HOSTNAME}:${STORM_FRONTEND_PORT} --timeout=${WAIT_TIMEOUT}

cd /home/tester/robot

robot --pythonpath .:lib ${VARIABLES} --exclude ${TESTSUITE_EXCLUDE} -s ${TESTSUITE_SUITE} tests
