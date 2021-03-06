*** Settings ***

Resource   lib/import.robot

*** Keywords ***

Do a prepareToPut  [Arguments]  ${surl}  ${tprotocol}
  ${output}  ${token}  ${turl}  Perform ptp with transfer protocol using clientSRM  ${surl}  ${tprotocol}  -p
  Should contain  ${output}  SRM_SPACE_AVAILABLE
  [Return]  ${token}  ${turl}

Do a putDone  [Arguments]  ${surl}  ${token}
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  Should contain  ${output}  SRM_SUCCESS

*** Test Cases ***

File-Transfer put VO file with proxy
  [Tags]  filetransfer  put
  [Setup]  Setup default SA
  Create empty working directory
  ${surl}  Build surl  ${TEST_SA}  ${TESTDIR}/${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${token}  ${turl}  Do a prepareToPut  ${surl}  https
  ${out}  ${err}  Do CURL PUT  ${turl}  ${TEST_LOCAL_FILEPATH}  ${TEST_CURL_OPTIONS}
  Should Contain  ${out}  204 No Content
  Do a putDone  ${surl}  ${token}
  [Teardown]  Clear all credentials

File-Transfer PUT VO file as anonymous
  [Tags]  filetransfer  put
  [Setup]  Setup default SA
  Create empty working directory
  ${surl}  Build surl  ${TEST_SA}  ${TESTDIR}/${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${token}  ${turl}  Do a prepareToPut  ${surl}  http
  ${out}  ${err}  Do CURL PUT  ${turl}  ${TEST_LOCAL_FILEPATH}
  Should Not Contain  ${out}  200 OK
  Should Match Regexp  ${out}  (403|401 Unauthorized)
  Do a putDone  ${surl}  ${token}
  [Teardown]  Clear all credentials
