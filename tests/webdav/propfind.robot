*** Settings ***

Resource   lib/import.robot

*** Test cases ***

WebDAV PROPFIND allprop on file
  [Tags]  webdav  propfind  no-gridhttps
  [Setup]  Setup default SA
  Create working directory
  ${body}  Get PROPFIND ALLPROP body
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL PROPFIND and check success  ${url}  ${body}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  ${TESTDIR}/${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Should Contain  ${stdout}  <ns1:Checksum>
  Should Contain  ${stdout}  </ns1:Checksum>
  Should Contain  ${stdout}  <d:status>HTTP/1.1 200 OK</d:status>
  Should Contain  ${stdout}  <d:iscollection>FALSE</d:iscollection>
  [Teardown]  Teardown default SA

WebDAV PROPFIND allprop on non empty directory
  [Tags]  webdav  propfind  no-gridhttps
  [Setup]  Setup default SA
  Create working directory
  ${body}  Get PROPFIND ALLPROP body
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  ${stdout}  ${stderr}  Do CURL PROPFIND and check success  ${url}  ${body}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  ${TESTDIR}/${TEST_REMOTE_DIRNAME}
  Should Contain  ${stdout}  ${TESTDIR}/${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Should Contain  ${stdout}  <ns1:Checksum>
  Should Contain  ${stdout}  </ns1:Checksum>
  Should Contain  ${stdout}  <d:status>HTTP/1.1 200 OK</d:status>
  Should Contain  ${stdout}  <d:iscollection>FALSE</d:iscollection>
  Should Contain  ${stdout}  <d:iscollection>TRUE</d:iscollection>
  [Teardown]  Teardown default SA

WebDAV PROPFIND propname on file
  [Tags]  webdav  propfind
  [Setup]  Setup default SA
  Create working directory
  ${body}  Get PROPFIND PROPNAME body
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Do CURL PROPFIND and check success  ${url}  ${body}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV PROPFIND prop on file
  [Tags]  webdav  propfind
  [Setup]  Setup default SA
  Create working directory
  ${body}  Get PROPFIND PROP body  status
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Do CURL PROPFIND and check success  ${url}  ${body}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA
