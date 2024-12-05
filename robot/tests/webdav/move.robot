*** Settings ***

Resource   lib/import.robot

*** Test cases ***

WebDAV MOVE file
  [Tags]  webdav  move
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  Do CURL MOVE and check success  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA
  
WebDAV MOVE non empty directory
  [Tags]  webdav  move
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}_2
  Do CURL MOVE and check success  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA
  
WebDAV MOVE file overwrite
  [Tags]  webdav  move  to-be-fixed
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  Do CURL COPY and check success  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  Do CURL HEAD and check success  ${dstURL}  ${TEST_CURL_OPTIONS}
  ${overwriteHeader}  Get CURL header  Overwrite  T
  Do CURL MOVE and check overwrite success  ${srcURL}  ${dstURL}  ${overwriteHeader} ${TEST_CURL_OPTIONS}
  [Teardown]  Teardown default SA

WebDAV MOVE file not allowed overwrite
  [Tags]  webdav  move
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  Do CURL PUT and check success  ${dstURL}  ${TEST_LOCAL_FILEPATH}  ${TEST_CURL_OPTIONS}
  ${overwriteHeader}  Get CURL header  Overwrite  F
  ${stdout}  ${stderr}  Do CURL MOVE  ${srcURL}  ${dstURL}  ${overwriteHeader} ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  412 Precondition Failed
  [Teardown]  Teardown default SA

WebDAV MOVE not existent file
  [Tags]  webdav  move  no-gridhttps
  [Setup]  Setup default SA
  Create empty working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  ${stdout}  ${stderr}  Do CURL MOVE  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  404 Not Found
  [Teardown]  Teardown default SA

WebDAV MOVE with destination equals to source
  [Tags]  webdav  move
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${overwriteHeader}  Get CURL header  Overwrite  T
  ${stdout}  ${stderr}  Do CURL MOVE  ${srcURL}  ${dstURL}  ${overwriteHeader} ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA