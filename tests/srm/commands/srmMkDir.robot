*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Create new empty directory
  [Tags]  storm-client  mkdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Create directory with invalid path
  [Tags]  storm-client  mkdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  fakeVO  ${dirname}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_INVALID_PATH
  [Teardown]  Clear all credentials

Create directory that already exists
  [Tags]  storm-client  mkdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_DUPLICATION_ERROR
  Should Contain  ${output}  Path exists and it's a directory.
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Create directory that has no parent
  [Tags]  storm-client  mkdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform mkdir using clientSRM  ${surl}/a/b
  Should Contain  ${output}  SRM_INVALID_PATH
  Should Contain  ${output}  Parent directory does not exists. Recursive directory creation Not Allowed
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Create directory with parent as a file
  [Tags]  storm-client  mkdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Put without really putting using clientSRM  ${surl}/a
  ${output}  Perform mkdir using clientSRM  ${surl}/a/b
  Should Contain  ${output}  SRM_INVALID_PATH
  Should Contain  ${output}  Path specified exists as a file.
  ${output}  Perform rm using clientSRM  ${surl}/a
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Create directory over a file
  [Tags]  storm-client  mkdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  Put without really putting using clientSRM  ${surl}/a
  ${output}  Perform mkdir using clientSRM  ${surl}/a
  Should Contain  ${output}  SRM_INVALID_PATH
  Should Contain  ${output}  Path specified exists as a file.
  ${output}  Perform rm using clientSRM  ${surl}/a
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Create directory with unauthorized credentials
  [Tags]  storm-client  mkdir
  [Setup]  Use default grid proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  [Teardown]  Clear all credentials

Check directory creation on a different VO
  [Tags]  storm-client  ls  STOR-898
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${qsurl}  Build surl  ${SA.2}  ../${DEFAULT_SA}/${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${qsurl}
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  ${qsurl}  Build surl  ${DEFAULT_SA}  ../${SA.2}/${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${qsurl}
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  [Teardown]  Clear all credentials
