*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

WebDAV DELETE file
  [Tags]  webdav  delete
  [Setup]  Setup default SA
  Create working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Do CURL DELETE and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV DELETE non empty directory
  [Documentation]  Since v1.3.1 removing not empty directories is not allowed
  [Tags]  webdav  delete
  [Setup]  Setup default SA
  Create working directory
  ${urlDirectory}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  ${stdout}  ${stderr}  Do CURL DELETE  ${urlDirectory}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  412 Precondition Failed
  ${urlFile}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Do CURL DELETE and check success  ${urlFile}
  Do CURL DELETE and check success  ${urlDirectory}
  [Teardown]  Teardown default SA

WebDAV DELETE non existent resource
  [Tags]  webdav  delete  no-gridhttps
  [Setup]  Setup default SA
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  ${stdout}  ${stderr}  Do CURL DELETE  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  404 Not Found
  [Teardown]  Teardown default SA
