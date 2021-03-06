*** Settings ***

Resource   lib/import.robot

*** Test cases ***

WebDAV GET file
  [Tags]  webdav  get
  [Setup]  Setup default SA
  Create working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL GET and check success  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  test123456789
  [Teardown]  Teardown default SA

WebDAV GET file and verify checksum
  [Tags]  webdav  get  no-gridhttps
  [Setup]  Setup default SA
  Create working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL GET and check success  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  test123456789
  Should Contain  ${stdout}  Digest: adler32=1d3b039e
  [Teardown]  Teardown default SA

WebDAV GET directory
  [Tags]  webdav  get
  [Setup]  Setup default SA
  Create empty working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  Do CURL GET and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV GET root directory
  [Tags]  webdav  get
  [Setup]  Setup default SA
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}
  Do CURL GET and check success  ${url}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV GET non existent resource
  [Tags]  webdav  get
  [Setup]  Setup default SA
  Create empty working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL GET  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  404 Not Found
  [Teardown]  Teardown default SA

WebDAV GET resource with missing parent
  [Tags]  webdav  get
  [Setup]  Setup default SA
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL GET  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  404 Not Found
  [Teardown]  Teardown default SA

WebDAV partial GET
  [Tags]  webdav  get  no-gridhttps
  [Setup]  Setup default SA
  Create working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL partial GET and check success  ${url}  0-3  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  test
  Should Contain  ${stdout}  Content-Length: 4
  Should Not Contain  ${stdout}  test1
  ${stdout}  ${stderr}  Do CURL partial GET and check success  ${url}  4-7  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  1234
  Should Contain  ${stdout}  Content-Length: 4
  ${stdout}  ${stderr}  Do CURL partial GET and check success  ${url}  9-12  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  6789
  Should Contain  ${stdout}  Content-Length: 4
  ${stdout}  ${stderr}  Do CURL partial GET and check success  ${url}  1-3,5-7,10-11  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  Content-Range: bytes 1-3/13
  Should Contain  ${stdout}  est
  Should Contain  ${stdout}  Content-Range: bytes 5-7/13
  Should Contain  ${stdout}  234
  Should Contain  ${stdout}  Content-Range: bytes 10-11/13
  Should Contain  ${stdout}  78
  ${stdout}  ${stderr}  Do CURL partial GET and check success  ${url}  11-13  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  89
  Should Contain  ${stdout}  Content-Range: bytes 11-12/13
  Should Contain  ${stdout}  Content-Length: 2
  ${stdout}  ${stderr}  Do CURL partial GET  ${url}  20-24  ${TEST_CURL_OPTIONS}
  Should Match Regexp  ${stdout}  (416 Requested Range Not Satisfiable|416 Range Not Satisfiable)
  ${stdout}  ${stderr}  Do CURL partial GET and check success  ${url}  1-3,20-24  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  Content-Range: bytes 1-3/13
  Should Contain  ${stdout}  est
  Should Contain  ${stdout}  Content-Length: 3
  [Teardown]  Teardown default SA
