*** Settings ***

Resource   lib/import.robot

*** Test Cases **

Status of a prepare to get with file pinned
  [Tags]  storm-client  sptg
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Put without really putting using clientSRM  ${surl}
  ${output}  ${token1}  Perform ptg using clientSRM  ${surl}
  Should Contain  ${output}  SRM_REQUEST_QUEUED
  ${output}  ${token2}  Perform ptg using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_FILE_PINNED
  ${output}  Perform sptg using clientSRM  ${surl}  ${token2}
  Should Contain  ${output}  SRM_FILE_PINNED
  ${output}  Perform rf using clientSRM  ${surl}  ${token2}
  Should Contain  ${output}  SRM_SUCCESS
  Should Not Contain  ${output}  SRM_RELEASED
  Should Not Contain  ${output}  SRM_FAILURE
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Status of a prepare to get on a unexistent file
  [Tags]  storm-client  sptg
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}  -p
  ${output}  Perform sptg using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_FAILURE
  [Teardown]  Clear all credentials

Status of prepare to get using a non existent token
  [Tags]  regression  sptg
  [Documentation]  Regression test for https://issues.infn.it/browse/STOR-217. StoRM crashed when a status for an async request was requested but the service is not able to get the into out of the database (for example, the token does not exists). This test calls a status for a prepare to get.
  [Setup]  Use default voms proxy
  ${output}  Execute clientSRM Command  sptg -t abcde
  [Teardown]  Clear all credentials
