*** Settings ***

Resource   lib/import.robot

*** Keywords ***

getRandomSURL  [Arguments]  ${sa}=${DEFAULT_SA}
  ${filename}  Get a unique name
  ${surl}  Build surl  ${sa}  ${TESTDIR}/${filename}
  [Return]  ${surl}

createRemoteFile  [Arguments]  ${surl}
  Put without really putting using clientSRM  ${surl}

srmPtP  [Arguments]  ${surl}  ${options}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  ${options}
  Log  ${output}
  [Return]  ${output}  ${token}

srmPd  [Arguments]  ${surl}  ${token}
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  Log  ${output}
  [Return]  ${output}

srmSPtP  [Arguments]  ${surl}  ${token}
  ${output}  Perform sptp using clientSRM  ${surl}  ${token}
  Log  ${output}
  [Return]  ${output}

check srmPtP success  [Arguments]  ${output}
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  Should Not Contain  ${output}  SRM_FAILURE

check srmSPtP success  [Arguments]  ${output}
  Should Contain  ${output}  SRM_SUCCESS
  Should Not Contain  ${output}  SRM_FAILURE

check srmPtP failure with  [Arguments]  ${output}  ${status}
  Should Contain  ${output}  ${status}
  Should Contain  ${output}  SRM_FAILURE
  Should Not Contain  ${output}  SRM_SPACE_AVAILABLE

check srmSPtP failure with  [Arguments]  ${output}  ${status}
  Should Contain  ${output}  ${status}
  Should Contain  ${output}  SRM_FAILURE

check srmPd success  [Arguments]  ${output}
  Should Contain  ${output}  SRM_SUCCESS
  Should Not Contain  ${output}  SRM_FAILURE

deleteRemoteFile  [Arguments]  ${surl}
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS

get TURL from output  [Arguments]  ${output}
  ${result}  ${turl}=  Should Match Regexp  ${output}  TURL=(\".+\")
  [Return]  ${turl}

*** Test Cases ***

srmPtP of a non-existent file
  [Tags]  storm-client  ptp
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  ${outputPtP}  ${token}  srmPtP  ${surl}  -p
  check srmPtP success  ${outputPtP}
  ${outputPd}  srmPd  ${surl}  ${token}
  check srmPd success  ${outputPd}
  deleteRemoteFile  ${surl}
  [Teardown]  Clear all credentials

srmPtP of an existent file with no overwrite
  [Tags]  storm-client  ptp  regression
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  createRemoteFile  ${surl}
  ${outputPtP}  ${token}  srmPtP  ${surl}  -p
  check srmPtP failure with  ${outputPtP}  SRM_DUPLICATION_ERROR
  deleteRemoteFile  ${surl}
  [Teardown]  Clear all credentials

srmPtP of an existent file with overwrite
  [Tags]  storm-client  ptp
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  createRemoteFile  ${surl}
  ${outputPtP}  ${token}  srmPtP  ${surl}  -p -w 1
  check srmPtP success  ${outputPtP}
  ${outputPd}  srmPd  ${surl}  ${token}
  check srmPd success  ${outputPd}
  deleteRemoteFile  ${surl}
  [Teardown]  Clear all credentials

check file content after a srmPtP with overwrite
  [Documentation]  Test introduced for https://issues.infn.it/jira/browse/STOR-1102
  [Tags]  storm-client  ptp  gfal
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  ${name}  Create local file with text  Hello World
  ${output}  Copy-out file using gfal-utils  ${name}  ${surl}
  ${outputPtP}  ${token}  srmPtP  ${surl}  -p -w 1
  check srmPtP success  ${outputPtP}
  ${outputPd}  srmPd  ${surl}  ${token}
  check srmPd success  ${outputPd}
  Copy-in file using gfal-utils  ${surl}  ${name}_2
  ${output}  Cat local file  ${name}_2
  Should Contain  ${output}  Hello World
  deleteRemoteFile  ${surl}
  Remove local file  ${name}
  Remove local file  ${name}_2
  [Teardown]  Clear all credentials

srmPtP with unsupported transfer protocol
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/127
  [Tags]  storm-client  ptp  regression
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  ${outputPtP}  ${token}  srmPtP  ${surl}  -p -T -P unknownprotocol
  check srmPtP failure with  ${outputPtP}  SRM_NOT_SUPPORTED
  [Teardown]  Clear all credentials

srmPtP using a non existent space token
  [Tags]  storm-client  ptp  regression
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/282. StoRM used to return the wrong error (SRM_SPACE_LIFETIME_EXPIRED instead of SRM_INVALID_REQUEST) for a sptp when a ptp was given a non existent space token.
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  ${outputPtP}  ${token}  srmPtP  ${surl}  -p -t whatever
  check srmPtP failure with  ${outputPtP}  SRM_INVALID_REQUEST
  ${outputSPtP}  srmSPtP  ${surl}  ${token}
  check srmSPtP failure with  ${outputSPtP}  SRM_INVALID_REQUEST
  Should Contain  ${outputSPtP}  The provided Space Token does not exists
  [Teardown]  Clear all credentials

srmPtP with sa token as space token
  [Tags]  storm-client  regression  ptp
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/354 A call of the srmPrepareToPut command providing the space token parameter of a storage area fails.
  [Setup]  Use default voms proxy
  ${sa_token}  Get SA Token  ${defaultVO}
  ${sp_token}  Get space token using clientSRM  ${sa_token}
  ${surl}  getRandomSURL
  ${outputPtP}  ${token}  srmPtP  ${surl}  -p -t ${sp_token}
  check srmPtP success  ${outputPtP}
  ${outputPd}  srmPd  ${surl}  ${token}
  check srmPd success  ${outputPd}
  deleteRemoteFile  ${surl}
  [Teardown]  Clear all credentials

srmPtP with expectedFileSize not empty
  [Tags]  storm-client  regression  ptp
  [Documentation]  Regression test for https://issues.infn.it/jira/browse/STOR-306 StoRM returns NULL fileSize for ptp with expected size
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  ${surl_with_size}  Catenate  SEPARATOR=,  ${surl}  12345
  ${outputPtP}  ${token}  srmPtP  ${surl_with_size}  -p
  check srmPtP success  ${outputPtP}
  Should Contain  ${outputPtP}  fileSize=12345
  ${outputPd}  srmPd  ${surl}  ${token}
  check srmPd success  ${outputPd}
  deleteRemoteFile  ${surl}
  [Teardown]  Clear all credentials

srmPtP with multiple surls
  [Tags]  storm-client  ptp
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  ${surllist} =  Set Variable  ${surl}
  :FOR  ${index}  IN RANGE  2  10
  \		${surl}  getRandomSURL  ${defaultVO}
  \		${surllist}  Catenate  ${surllist}  ${surl}
  Log  ${surllist}
  ${outputPtP}  ${token}  srmPtP  ${surllist}  -p
  check srmPtP success  ${outputPtP}
  ${outputSPtP}  srmSPtP  ${surllist}  ${token}
  check srmSPtP success  ${outputSPtP}
  ${outputPd}  srmPd  ${surllist}  ${token}
  check srmPd success  ${outputPd}
  deleteRemoteFile  ${surllist}
  [Teardown]  Clear all credentials

srmPtP on a busy file
  [Tags]  storm-client  ptp  regression
  [Setup]  Use default voms proxy
  ${surl}  getRandomSURL
  ${outputPtP}  ${token}  srmPtP  ${surl}  -p
  check srmPtP success  ${outputPtP}
  ${outputPtP}  ${token2}  srmPtP  ${surl}  -p
  check srmPtP failure with  ${outputPtP}  SRM_FILE_BUSY
  ${outputPd}  srmPd  ${surl}  ${token}
  check srmPd success  ${outputPd}
  deleteRemoteFile  ${surl}
  [Teardown]  Clear all credentials

srmPtP with xroot transfer protocol
  [Tags]  storm-client  ptg
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${defaultVO}  ${TESTDIR}/${filename}
  ${outputPtP}  ${token}  srmPtP  ${surl}  -p -T -P xroot
  Log  ${outputPtP}
  check srmPtP success  ${outputPtP}
  ${turl}  get TURL from output  ${outputPtP}
  Should Contain  ${outputPtP}  root://${backEndHost}${storageAreaRoot}/${defaultVO}/${TESTDIR}/${filename}
  ${outputPd}  srmPd  ${surl}  ${token}
  check srmPd success  ${outputPd}
  deleteRemoteFile  ${surl}
  [Teardown]  Clear all credentials