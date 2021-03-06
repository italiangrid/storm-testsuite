*** Settings ***

Resource   lib/import.robot

*** Test cases ***

WebDAV PUT
  [Tags]  webdav  put
  [Setup]  Setup default SA
  Create empty working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Do CURL PUT and check success  ${url}  ${TEST_LOCAL_FILEPATH}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV PUT overwrite
  [Tags]  webdav  put
  [Setup]  Setup default SA
  Create empty working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Do CURL PUT and check success  ${url}  ${TEST_LOCAL_FILEPATH}  ${TEST_CURL_OPTIONS}
  Do CURL PUT and check overwrite success  ${url}  ${TEST_LOCAL_FILEPATH}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV PUT with missing anchestor
  [Tags]  webdav  put  no-gridhttps
  [Setup]  Setup default SA
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Do CURL PUT and check success  ${url}  ${TEST_LOCAL_FILEPATH}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV PUT over collection
  [Tags]  webdav  put  to-be-fixed
  [Setup]  Setup default SA
  Create empty working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  ${stdout}  ${stderr}  Do CURL PUT  ${url}  ${TEST_LOCAL_FILEPATH}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  405 Method not allowed
  [Teardown]  Teardown default SA
