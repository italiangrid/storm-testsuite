#!/bin/bash
set -e

echo 'export X509_USER_PROXY="/tmp/x509up_u$(id -u)"'>/etc/profile.d/x509_user_proxy.sh

puppet apply --detailed-exitcodes /setup/manifest.pp
ec=$?
if $ec == 4 || $ec == 6; then
  echo "Puppet apply exited with $ec"
  exit 1
else

fi

# Add tester user
adduser -d /home/tester tester

# .globus
mkdir /home/tester/.globus
chown tester:tester /home/tester/.globus
