*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

STOR-795 Storage area matching fails with COPY/MOVE
  [Tags]  webdav  copy
  [Setup]  Setup SA and VO  ${DAVSecureEndpoint}  ${SA.8}  ${defaultUser}  ${VO.2}
  Create working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${url2}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  Do CURL COPY and check success  ${url}  ${url2}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown SA and VO