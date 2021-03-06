*** Settings ***

Resource   lib/import.robot

*** Test cases ***

WebDAV OPTIONS on storage area root directory
  [Tags]  webdav  options
  [Setup]  Setup default SA
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}
  Do CURL OPTIONS and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV OPTIONS on file
  [Tags]  webdav  options
  [Setup]  Setup default SA
  Create working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Do CURL OPTIONS and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV OPTIONS on directory
  [Tags]  webdav  options
  [Setup]  Setup default SA
  Create empty working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  Do CURL OPTIONS and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA