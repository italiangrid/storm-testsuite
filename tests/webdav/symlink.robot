*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

WebDAV GET dotted path to another SA with unauthorized credentials
  [Tags]  webdav  symlink
  [Setup]  Setup default SA
  ${url}  Set Variable  ${TEST_ENDPOINT}/${TEST_SA}/../${SA.2}
  Log  ${url}
  ${stdout}  ${stderr}  Do CURL GET  ${url}  ${TEST_CURL_OPTIONS}
  Should Not Contain  ${stdout}  200 OK
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA

WebDAV GET dotted path to another SA with authorized HTTP READ
  [Tags]  webdav  symlink
  [Setup]  Setup default SA
  ${url}  Set Variable  ${TEST_ENDPOINT}/${TEST_SA}/../${SA.7}
  Log  ${url}
  Do CURL GET and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV GET dotted path to another SA with anonymous HTTP READ
  [Tags]  webdav  symlink
  [Setup]  Setup default SA
  ${url}  Set Variable  ${TEST_ENDPOINT}/${TEST_SA}/../${SA.9}
  Log  ${url}
  Do CURL GET and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA