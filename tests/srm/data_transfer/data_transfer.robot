*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Test that the SRM service is able to transfer a file on the SRM endpoint
  [Tags]  storm-client  globus-utils
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${turl}  Build gsiftp TURL  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using globus-utils  ${filename}  ${turl}
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform ls using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Transfer empty file
  [Tags]  regression  ptp  to-be-fixed
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/241. If a client tries to transfer an empty file to a valid gsiftp TURL the transfer fails.
  [Setup]  Use default voms proxy
  ${filename}  Create local empty file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${turl}  Build gsiftp TURL  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  Try to copy-out file using globus-utils  ${filename}  ${turl}
  Should not contain  ${output}  globus_xio: An end of file occurred
  [Teardown]  Clear all credentials

Test that the SRM service is able to transfer a file from the SRM endpoint
  [Tags]  storm-client  ptg
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using gfal-utils  ${filename}  ${surl}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}  -p -T -P gsiftp
  ${result}  ${turl}=  Should Match Regexp  ${output}  transferURL=(\".+\")
  Copy-in file using gsiftp protocol  ${turl}  ${filename}
  [Teardown]  Clear all credentials

Check checksum of copied file
  [Tags]  checksum  gridftp
  [Documentation]  StoRM BE must be configured with GRIDFTP_WITH_DSI="yes" to pass this test
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${srcsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${srcsurl}  -p
  ${turl}  Build gsiftp TURL  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using globus-utils  ${filename}  ${turl}
  ${output}  Perform pd using clientSRM  ${srcsurl}  ${token}  -p
  ${destsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}_copied
  ${output}  Copy file using gfal-utils  ${srcsurl}  ${destsurl}
  ${checksum1}  Get checksum of remote file using gfal-utils  ${srcsurl}
  ${checksum2}  Get checksum of remote file using gfal-utils  ${destsurl}
  Log  ${checksum1}
  Log  ${checksum2}
  Should Be Equal As Strings  ${checksum1}  ${checksum2}
  [Teardown]  Clear all credentials
