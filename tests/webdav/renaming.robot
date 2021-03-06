*** Settings ***

Resource   lib/import.robot

*** Keywords ***

Setup Renaming on particular SA and VO  [Arguments]  ${endpoint}=${DAVSecureEndpoint}  ${sa}=${DEFAULT_SA}  ${user}=${defaultUser}  ${voname}=${DEFAULT_VO}
  Use voms proxy  ${user}  ${voname}
  ${options}  Get CURL VOMS proxy options  ${user}  ${voname}
  ${destL1dir}  Get a unique name
  ${destL2dir}  Get a unique name
  Set Test Variable  ${TEST_CURL_OPTIONS}  ${options}
  Set Test Variable  ${TEST_REMOTE_DIR1}  ${destL1dir}
  Set Test Variable  ${TEST_REMOTE_DIR2}  ${destL2dir}
  Set Test Variable  ${TEST_SA}  ${sa}
  Set Test Variable  ${TEST_ENDPOINT}  ${endpoint}
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}
  ${filename}  Upload file with CURL  ${url}  ${TEST_CURL_OPTIONS}
  Set Test Variable  ${TEST_FILENAME}  ${filename}

*** Test Cases ***

File renaming
  [Tags]  webdav  renaming
  [Setup]  Setup Renaming on particular SA and VO
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_FILENAME}
  Do CURL HEAD and check success  ${srcURL}  ${TEST_CURL_OPTIONS}
  ${destURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIR1}/${TEST_REMOTE_DIR2}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL HEAD  ${destURL}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  404 Not Found
  ${l2URL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIR1}/${TEST_REMOTE_DIR2}
  ${stdout}  ${stderr}  Do CURL HEAD  ${l2URL}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  404 Not Found
  ${l1URL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIR1}
  ${stdout}  ${stderr}  Do CURL HEAD  ${l1URL}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  404 Not Found
  Do CURL MKCOL and check success  ${l1URL}  ${TEST_CURL_OPTIONS}
  Do CURL MKCOL and check success  ${l2URL}  ${TEST_CURL_OPTIONS}
  Do CURL MOVE and check success  ${srcURL}  ${destURL}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA