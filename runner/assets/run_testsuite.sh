#!/bin/bash
set -x

# Optional parameters
TESTSUITE="${TESTSUITE:-https://github.com/italiangrid/storm-testsuite.git}"
TESTSUITE_BRANCH="${TESTSUITE_BRANCH:-nightly}"
TESTSUITE_EXCLUDE="${TESTSUITE_EXCLUDE:-to-be-fixed}"
TESTSUITE_SUITE="${TESTSUITE_SUITE:-tests}"

STORM_BACKEND_HOSTNAME="${STORM_BACKEND_HOSTNAME:-storm.example}"
STORM_DAV_HOST="${STORM_WEBDAV_HOSTNAME:-storm-alias.example}"
STORM_STORAGE_ROOT_DIR="${STORM_STORAGE_ROOT_DIR:-/storage}"

STORM_GRIDFTP_HOSTNAME="${STORM_GRIDFTP_HOSTNAME:-storm-alias.example}"

STORM_FRONTEND_HOSTNAME=${STORM_FRONTEND_HOSTNAME:-${STORM_BACKEND_HOSTNAME}}

# Build variables
VARIABLES="--variable backEndHost:$STORM_BACKEND_HOSTNAME"
VARIABLES="$VARIABLES --variable storageAreaRoot:$STORM_STORAGE_ROOT_DIR"
VARIABLES="$VARIABLES --variable DAVHost:$STORM_WEBDAV_HOSTNAME"
VARIABLES="$VARIABLES --variable globusEndpoint:$STORM_GRIDFTP_HOSTNAME:2811"
VARIABLES="$VARIABLES --variable frontEndHost:$STORM_FRONTEND_HOSTNAME"

# Build exclude clause
if [ -z "$TESTSUITE_EXCLUDE" ]; then
  EXCLUDE=""
else
  EXCLUDE="--exclude $TESTSUITE_EXCLUDE"
fi

# Wait for StoRM services
WAIT_TIMEOUT=${WAIT_TIMEOUT:-600}

chmod +x /assets/scripts/wait-for-it.sh
/assets/scripts/wait-for-it.sh ${STORM_WEBDAV_HOSTNAME}:8443 --timeout=${WAIT_TIMEOUT}
/assets/scripts/wait-for-it.sh ${STORM_FRONTEND_HOSTNAME}:8444 --timeout=${WAIT_TIMEOUT}

cd /home/tester/

if [ -d "storm-testsuite" ]; then
  cd storm-testsuite
else
  git clone $TESTSUITE --branch $TESTSUITE_BRANCH
  cd storm-testsuite
fi

robot --pythonpath .:lib $VARIABLES $EXCLUDE -d reports -s $TESTSUITE_SUITE tests
