*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Remove existent empty directory
  [Tags]  storm-client  rmdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Remove a non existent directory
  [Tags]  storm-client  rmdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_INVALID_PATH
  Should Contain  ${output}  Directory does not exists
  [Teardown]  Clear all credentials

Remove existent non empty directory without recursion
  [Tags]  storm-client  rmdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${filename}  Get a unique name
  ${surlDir}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${surlFile}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${filename}
  ${output}  Perform mkdir using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_SUCCESS
  Put without really putting using clientSRM  ${surlFile}
  ${output}  Perform rmdir using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_NON_EMPTY_DIRECTORY
  ${output}  Perform rmdir using clientSRM  ${surlDir}  -r
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Remove existent non empty directory with recursion
  [Tags]  storm-client  rmdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${filename}  Get a unique name
  ${surlDir}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${surlFile}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${filename}
  ${output}  Perform mkdir using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_SUCCESS
  Put without really putting using clientSRM  ${surlFile}
  ${output}  Perform rmdir using clientSRM  ${surlDir}  -r
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Remove invalid path
  [Tags]  storm-client  rmdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_INVALID_PATH
  [Teardown]  Clear all credentials

Removing unauthorized directory
  [Tags]  storm-client  rmdir
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Use default grid proxy
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  Use default voms proxy
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials
