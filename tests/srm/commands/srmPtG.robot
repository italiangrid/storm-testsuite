*** Settings ***

Resource   lib/import.robot

*** Keywords ***

getRandomSURL  [Arguments]  ${sa}=${DEFAULT_SA}
  ${filename}  Get a unique name
  ${surl}  Build surl  ${sa}  ${TESTDIR}/${filename}
  [Return]  ${surl}

createRemoteFile  [Arguments]  ${surl}
  Put without really putting using clientSRM  ${surl}

srmPtG  [Arguments]  ${surl}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}  -p
  [Return]  ${output}  ${token}

srmRf  [Arguments]  ${surl}  ${token}
  ${output}  Perform rf using clientSRM  ${surl}  ${token}
  [Return]  ${output}

check srmPtG success  [Arguments]  ${output}
  Should Contain  ${output}  SRM_FILE_PINNED
  Should Not Contain  ${output}  SRM_FAILURE

check srmPtG failure with  [Arguments]  ${output}  ${status}
  Should Contain  ${output}  ${status}
  Should Contain  ${output}  SRM_FAILURE
  Should Not Contain  ${output}  SRM_FILE_PINNED

check srmRf success  [Arguments]  ${output}
  Should Contain  ${output}  SRM_SUCCESS
  Should Not Contain  ${output}  SRM_RELEASED
  Should Not Contain  ${output}  SRM_FAILURE

deleteRemoteFile  [Arguments]  ${surl}
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS

get TURL from output  [Arguments]  ${output}
  ${result}  ${turl}=  Should Match Regexp  ${output}  transferURL=(\".+\")
  [Return]  ${turl}

*** Test Cases ***

srmPtG on an existent file
  [Tags]  storm-client  ptg
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  createRemoteFile  ${surl}
  ${outputPtG}  ${token}  srmPtG  ${surl}
  Log  ${outputPtG}
  check srmPtG success  ${outputPtG}
  ${outputRf}  srmRf  ${surl}  ${token}
  Log  ${outputRf}
  check srmRf success  ${outputRf}
  deleteRemoteFile  ${surl}
  [Teardown]  Clear all credentials

srmPtG on a non-existent file
  [Tags]  storm-client  ptg
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  ${outputPtG}  ${token}  srmPtG  ${surl}
  Log  ${outputPtG}
  check srmPtG failure with  ${outputPtG}  SRM_INVALID_PATH
  [Teardown]  Clear all credentials

Multiple srmPtG on a file
  [Tags]  regression  ptg
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  createRemoteFile  ${surl}
  ${outputPtG}  ${token1}  srmPtG  ${surl}
  Log  ${outputPtG}
  check srmPtG success  ${outputPtG}
  ${outputPtG}  ${token2}  srmPtG  ${surl}
  Log  ${outputPtG}
  check srmPtG success  ${outputPtG}
  ${outputRf}  srmRf  ${surl}  ${token1}
  Log  ${outputRf}
  check srmRf success  ${outputRf}
  ${outputRf}  srmRf  ${surl}  ${token2}
  Log  ${outputRf}
  check srmRf success  ${outputRf}
  deleteRemoteFile  ${surl}
  [Teardown]  Clear all credentials

MultiSURL srmPtG
  [Tags]  storm-client  ptg
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  createRemoteFile  ${surl}
  ${surllist} =  Set Variable  ${surl}
  FOR  ${index}  IN RANGE  2  10
  	${surl}  getRandomSURL  ${defaultVO}
  	createRemoteFile  ${surl}
  	${surllist}  Catenate  ${surllist}  ${surl}
  END
  Log  ${surllist}
  ${outputPtG}  ${token}  srmPtG  ${surllist}
  Log  ${outputPtG}
  check srmPtG success  ${outputPtG}
  ${outputRf}  srmRf  ${surl}  ${token}
  Log  ${outputRf}
  check srmRf success  ${outputRf}
  deleteRemoteFile  ${surllist}
  [Teardown]  Clear all credentials

srmPtG on a large file
  [Documentation]  Regression test for https://issues.infn.it/jira/browse/STOR-331
  [Tags]  storm-client  ptg  to-be-fixed
  [Setup]  Use default voms proxy
  ${filename}  Create local file with fake size  2049
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  Copy-out file using globus-utils  ${filename}  ${surl}
  ${output}  Perform pd using clientSRM  ${surl}  ${token}  -p
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_FILE_PINNED
  Log  ${output}
  Should Contain  ${output}  fileSize=2148532224
  Remove local file  ${filename}
  ${output}  Perform rf using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

srmPtG on another storage-area's file
  [Tags]  storm-client  ptg  STOR-898
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ../${SA.2}/${TESTDIR}/${filename}
  ${outputPtG}  ${token}  srmPtG  ${surl}
  Log  ${outputPtG}
  check srmPtG failure with  ${outputPtG}  SRM_AUTHORIZATION_FAILURE
  [Teardown]  Clear all credentials

srmPtG with xroot transfer protocol
  [Tags]  storm-client  ptg
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  createRemoteFile  ${surl}
  ${outputPtG}  ${token}  srmPtG  ${surl} -T -P xroot
  Log  ${outputPtG}
  check srmPtG success  ${outputPtG}
  ${turl}  get TURL from output  ${outputPtG}
  Should Contain  ${outputPtG}  root://${backEndHost}${storageAreaRoot}/${DEFAULT_SA}/${TESTDIR}/${filename}
  ${outputRf}  srmRf  ${surl}  ${token}
  check srmRf success  ${outputRf}
  deleteRemoteFile  ${surl}
  [Teardown]  Clear all credentials