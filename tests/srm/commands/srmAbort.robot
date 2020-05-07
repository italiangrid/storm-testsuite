*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

A user cannot abort the request of another user
  [Tags]  storm-client  abort
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Put without really putting using clientSRM  ${surl}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}
  Should Contain  ${output}  SRM_REQUEST_QUEUED
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}  -t ${token} -p
  Should Contain  ${output}  SRM_FILE_PINNED
  Use voms proxy  test1  ${DEFAULT_VO}
  ${output}  Perform abort request using clientSRM  ${token}
  Should Contain  ${output}   SRM_AUTHORIZATION_FAILURE
  [Teardown]  Clear all credentials

Abort of a prepare to get done on an existent file
  [Tags]  storm-client  abort
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Put without really putting using clientSRM  ${surl}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_FILE_PINNED
  ${output}  Perform abort request using clientSRM  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform sptg using clientSRM  ${surl}  ${token}
  Should Not Contain  ${output}  SRM_FILE_PINNED
  Should Contain  ${output}  SRM_ABORTED
  [Teardown]  Clear all credentials

Duplicated ptg abort
  [Tags]  storm-client  abort
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Put without really putting using clientSRM  ${surl}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_FILE_PINNED
  ${output}  Perform abort request using clientSRM  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform abort request using clientSRM  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform sptg using clientSRM  ${surl}  ${token}
  Should Not Contain  ${output}  SRM_FILE_PINNED
  Should Contain  ${output}  SRM_ABORTED
  [Teardown]  Clear all credentials

Abort multiple files
  [Tags]  storm-client  abort
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${filename}  Get a unique name
  ${surlDir}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${surlFile}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${filename}_1
  ${output}  Perform mkdir using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_SUCCESS
  ${surlFileList} =  Set Variable  ${surlFile}
  FOR  ${index}  IN RANGE  2  10
  	${current}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${filename}_${index}
  	${surlFileList}  Catenate  ${surlFileList}  ${current}
  END
  Log  ${surlFileList}
  ${output}  ${token}  Perform ptp using clientSRM  ${surlFileList}  -p
  Log  ${output}
  Should Contain  ${output}  SRM_SUCCESS
  Should Not Contain  ${output}  SRM_FAILURE
  ${output}  Perform abort file using clientSRM  ${surlFileList}  ${token}
  Log  ${output}
  Should Contain  ${output}  SRM_SUCCESS
  Should Not Contain  ${output}  SRM_ABORTED
  Should Not Contain  ${output}  SRM_FAILURE
  [Teardown]  Clear all credentials

Abort request with non existent fake token
  [Tags]  storm-client  abort
  [Setup]  Use default voms proxy
  ${output}  Perform abort request using clientSRM  fake_token
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  "invalid token: fake_token"
  [Teardown]  Clear all credentials

Abort request with non existent well-formed token
  [Tags]  storm-client  abort
  [Documentation]  Regression test for https://issues.infn.it/jira/browse/STOR-234. Storm BE does not manage correctly abort requests of expired tokens.
  [Setup]  Use default voms proxy
  ${output}  Perform abort request using clientSRM  992a7ecc-65df-4902-ae00-06a9691ad816
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  "No request found matching token 992a7ecc-65df-4902-ae00-06a9691ad816"
  [Teardown]  Clear all credentials

Abort after prepare to put
  [Tags]  storm-client  abort
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${output}  Perform abort request using clientSRM  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform ls using clientSRM  ${surl}
  Should Contain  ${output}  SRM_FAILURE
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_FAILURE
  [Teardown]  Clear all credentials

Abort after put done
  [Tags]  storm-client  abort
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform abort request using clientSRM  ${token}
  Should Contain  ${output}  SRM_FAILURE
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials
