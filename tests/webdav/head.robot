*** Settings ***

Resource   lib/import.robot

*** Test cases ***

WebDAV HEAD file
  [Tags]  webdav  head
  [Setup]  Setup default SA
  Create working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL HEAD and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV HEAD file and verify checksum
  [Tags]  webdav  head  no-gridhttps
  [Setup]  Setup default SA
  Create working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL HEAD and check success  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  Digest: adler32=1d3b039e
  [Teardown]  Teardown default SA

WebDAV HEAD directory
  [Tags]  webdav  head
  [Setup]  Setup default SA
  Create empty working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  Do CURL HEAD and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV HEAD root directory
  [Tags]  webdav  head
  [Setup]  Setup default SA
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}
  Do CURL HEAD and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV HEAD non existent resource
  [Tags]  webdav  head
  [Setup]  Setup default SA
  Create empty working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL HEAD  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  404 Not Found
  [Teardown]  Teardown default SA

WebDAV HEAD resource with missing parent
  [Tags]  webdav  head
  [Setup]  Setup default SA
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL HEAD  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  404 Not Found
  [Teardown]  Teardown default SA