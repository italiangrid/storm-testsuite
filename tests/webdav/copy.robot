*** Settings ***

Resource   lib/import.robot

*** Test cases ***

WebDAV COPY file
  [Tags]  webdav  copy
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  Do CURL COPY and check success  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  Do CURL HEAD and check success  ${dstURL}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA
  
WebDAV COPY non empty directory
  [Tags]  webdav  copy
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}_2
  Do CURL COPY and check success  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  Do CURL HEAD and check success  ${dstURL}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA
  
WebDAV COPY file overwrite
  [Tags]  webdav  copy
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  Do CURL COPY and check success  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  ${overwriteHeader}  Get CURL header  Overwrite  T
  Do CURL COPY and check overwrite success  ${srcURL}  ${dstURL}  ${overwriteHeader} ${TEST_CURL_OPTIONS}
  Do CURL HEAD and check success  ${dstURL}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV COPY file not allowed overwrite
  [Tags]  webdav  copy
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  Do CURL PUT and check success  ${dstURL}  ${TEST_LOCAL_FILEPATH}  ${TEST_CURL_OPTIONS}
  ${overwriteHeader}  Get CURL header  Overwrite  F
  ${stdout}  ${stderr}  Do CURL COPY  ${srcURL}  ${dstURL}  ${overwriteHeader} ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  412 Precondition Failed
  [Teardown]  Teardown default SA

WebDAV COPY not existent file
  [Tags]  webdav  copy  no-gridhttps
  [Setup]  Setup default SA
  Create empty working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  ${stdout}  ${stderr}  Do CURL COPY  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  404 Not Found
  [Teardown]  Teardown default SA

WebDAV COPY with destination equals to source
  [Tags]  webdav  copy
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${overwriteHeader}  Get CURL header  Overwrite  T
  ${stdout}  ${stderr}  Do CURL COPY  ${srcURL}  ${dstURL}  ${overwriteHeader} ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA

WebDAV COPY unauthorized
  [Tags]  webdav  copy  no-gridhttps
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  ${TEST_CURL_OPTIONS}  Get CURL VOMS proxy options  ${DEFAULT_USER}  ${VO.2}
  ${stdout}  ${stderr}  Do CURL COPY  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA
