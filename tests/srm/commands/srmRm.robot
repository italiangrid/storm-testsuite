*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Remove existent file
  [Tags]  storm-client  rm
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Put without really putting using clientSRM  ${surl}
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Remove unexistent file
  [Tags]  storm-client  rm
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_INVALID_PATH
  Should Contain  ${output}  File does not exist
  [Teardown]  Clear all credentials

Removing unauthorized file
  [Tags]  storm-client  rm
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Put without really putting using clientSRM  ${surl}
  Use default grid proxy
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  Use default voms proxy
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Partial success on removing multiple files
  [Tags]  storm-client  rm
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${filename2}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${surl2}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename2}
  Put without really putting using clientSRM  ${surl}
  Put without really putting using clientSRM  ${surl2}
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rm using clientSRM  ${surl} ${surl2}
  Should Contain  ${output}  SRM_PARTIAL_SUCCESS
  [Teardown]  Clear all credentials

Remove a pinned file must set aborted the ptg request
  [Tags]  storm-client  rm  ptg
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Put without really putting using clientSRM  ${surl}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_FILE_PINNED
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform sptg using clientSRM  ${surl}  ${token}
  Should Not Contain  ${output}  SRM_FILE_PINNED
  Should Contain  ${output}  SRM_ABORTED
  [Teardown]  Clear all credentials

Unauthorized remove on another VO's file
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ../${SA.2}/${TESTDIR}/${filename}
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  Log  ${output}
  [Teardown]  Clear all credentials


srmRm properly cleans up ongoing PtPs
  [Tags]  storm-client  rm  ptp  stor-779
  [Documentation]   Regression test for https://issues.infn.it/jira/browse/STOR-779
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Not Contain  ${output}  SRM_FAILURE
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${output}   Perform rm using clientSRM   ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Not Contain  ${output}  SRM_FAILURE
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  [Teardown]   Clear all credentials
