*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

WebDAV MKCOL
  [Tags]  webdav  mkcol
  [Setup]  Setup default SA
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  Do CURL MKCOL and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV MKCOL with missing anchestor
  [Tags]  webdav  mkcol
  [Setup]  Setup default SA
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_REMOTE_DIRNAME}
  ${stdout}  ${stderr}  Do CURL MKCOL  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  409 Conflict
  [Teardown]  Teardown default SA

WebDAV MKCOL on existent resource
  [Tags]  webdav  mkcol
  [Setup]  Setup default SA
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  Do CURL MKCOL and check success  ${url}  ${TEST_CURL_OPTIONS}
  ${stdout}  ${stderr}  Do CURL MKCOL  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  405 Method Not Allowed
  [Teardown]  Teardown default SA

WebDAV MKCOL unauthorized
  [Tags]  webdav  mkcol  no-gridhttps
  [Setup]  Setup default SA
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  ${TEST_CURL_OPTIONS}  Get CURL VOMS proxy options  ${defaultUser}  ${VO.2}
  ${stdout}  ${stderr}  Do CURL MKCOL  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  401 Unauthorized
  [Teardown]  Teardown default SA
