*** Settings ***

Resource   lib/import.robot

*** Keywords ***

Do a prepareToPut  [Arguments]  ${surl}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should contain  ${output}  SRM_SPACE_AVAILABLE
  [Return]  ${token}

Do a putDone  [Arguments]  ${surl}  ${token}
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  Should contain  ${output}  SRM_SUCCESS

Do a prepareToGet  [Arguments]  ${surl}  ${tprotocol}
  ${output}  ${token}  ${turl}  Perform ptg with transfer protocol using clientSRM  ${surl}  ${tprotocol}  -p
  Should contain  ${output}  SRM_FILE_PINNED
  [Return]  ${token}  ${turl}

Do a releaseFile  [Arguments]  ${surl}  ${token}
  ${output}  Perform rf using clientSRM  ${surl}  ${token}
  Should contain  ${output}  SRM_SUCCESS

*** Test Cases ***

File-Transfer get VO file with proxy
  [Tags]  filetransfer  get
  [Setup]  Setup default SA
  Create working directory
  ${surl}  Build surl  ${TEST_SA}  ${TESTDIR}/${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${token}  ${turl}  Do a prepareToGet  ${surl}  https
  Do CURL GET and check success  ${turl}  ${TEST_CURL_OPTIONS}
  Do a releaseFile  ${surl}  ${token}
  [Teardown]  Clear all credentials

File-Transfer get VO file as anonymous with anonymous http read disabled
  [Tags]  filetransfer  get
  [Setup]  Setup default SA
  Create working directory
  ${surl}  Build surl  ${TEST_SA}  ${TESTDIR}/${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${token}  ${turl}  Do a prepareToGet  ${surl}  http
  ${out}  ${err}  Do CURL GET  ${turl}
  Should Not Contain  ${out}  200 OK
  Should Match Regexp  ${out}  (403|401 Unauthorized)
  [Teardown]  Clear all credentials
