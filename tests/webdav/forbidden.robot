*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

######## GET / HEAD #########

WebDAV GET/HEAD VO file as anonymous user and anonymous http read disabled
  [Tags]  webdav  forbidden  get  head
  [Setup]  Setup default SA
  Create working directory
  ${url}  Build URL  ${DAVEndpoint}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL GET  ${url}
  Should Match Regexp  ${stdout}  (403|401 Unauthorized)
  ${stdout}  ${stderr}  Do CURL HEAD  ${url}
  Should Match Regexp  ${stdout}  (403|401 Unauthorized)
  [Teardown]  Teardown default SA

WebDAV GET/HEAD VO file as anonymous user and anonymous http read enabled
  [Tags]  webdav  forbidden  get  head
  [Setup]  Setup SA and VO  ${DAVSecureEndpoint}  ${SA.9}  ${DEFAULT_USER}  ${VO.1}
  Create working directory
  ${url}  Build URL  ${DAVEndpoint}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Do CURL GET and check success  ${url}
  Do CURL HEAD and check success  ${url}
  [Teardown]  Teardown SA and VO

WebDAV GET/HEAD VO file as authenticated user when authenticated http read is disabled
  [Tags]  webdav  forbidden  get  head  no-gridhttps
  [Setup]  Setup default SA
  Create working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${TEST_CURL_OPTIONS}  Get CURL default x509 options
  ${stdout}  ${stderr}  Do CURL GET  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  ${stdout}  ${stderr}  Do CURL HEAD  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA

WebDAV GET/HEAD VO file as anonymous user when anonymous http read is disabled
  [Tags]  webdav  forbidden  get  head
  [Setup]  Setup default SA
  Create working directory
  ${url}  Build URL  ${DAVEndpoint}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL GET  ${url}
  Should Match Regexp  ${stdout}  (403|401 Unauthorized)
  ${stdout}  ${stderr}  Do CURL HEAD  ${url}
  Should Match Regexp  ${stdout}  (403|401 Unauthorized)
  [Teardown]  Teardown default SA

######## PUT #########

WebDAV PUT VO file as anonymous
  [Tags]  webdav  forbidden  put
  [Setup]  Setup default SA
  Create empty working directory
  ${url}  Build URL  ${DAVEndpoint}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL PUT  ${url}  ${TEST_LOCAL_FILEPATH}
  Should Match Regexp  ${stdout}  (403|401 Unauthorized)
  [Teardown]  Teardown default SA

WebDAV PUT VO file as authenticated but not authorized user
  [Tags]  webdav  forbidden  put
  [Setup]  Setup default SA
  Create empty working directory
  ${TEST_CURL_OPTIONS}  Get CURL default x509 options
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL PUT  ${url}  ${TEST_LOCAL_FILEPATH}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA

WebDAV PUT VO file with the wrong proxy
  [Tags]  webdav  forbidden  put  no-gridhttps
  [Setup]  Setup default SA
  Create empty working directory
  ${TEST_CURL_OPTIONS}  Get CURL VOMS proxy options  ${DEFAULT_USER}  ${SA.2}
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL PUT  ${url}  ${TEST_LOCAL_FILEPATH}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA

######## DELETE #########

WebDAV DELETE VO file as anonymous
  [Tags]  webdav  forbidden  delete
  [Setup]  Setup default SA
  Create working directory
  ${url}  Build URL  ${DAVEndpoint}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL DELETE  ${url}
  Should Match Regexp  ${stdout}  (403|401 Unauthorized)
  [Teardown]  Teardown default SA

WebDAV DELETE VO file as authenticated but not authorized user
  [Tags]  webdav  forbidden  delete
  [Setup]  Setup default SA
  Create working directory
  ${TEST_CURL_OPTIONS}  Get CURL default x509 options
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL DELETE  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA

WebDAV DELETE VO file with the wrong proxy
  [Tags]  webdav  forbidden  delete  no-gridhttps
  [Setup]  Setup default SA
  Create working directory
  ${TEST_CURL_OPTIONS}  Get CURL VOMS proxy options  ${DEFAULT_USER}  ${SA.2}
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL DELETE  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA

######## MKCOL #########

WebDAV MKCOL VO directory as anonymous
  [Tags]  webdav  forbidden  mkcol
  [Setup]  Setup default SA
  Create empty working directory
  ${url}  Build URL  ${DAVEndpoint}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_REMOTE_DIRNAME}
  ${stdout}  ${stderr}  Do CURL MKCOL  ${url}
  Should Match Regexp  ${stdout}  (403|401 Unauthorized)
  [Teardown]  Teardown default SA

WebDAV MKCOL VO directory as authenticated but not authorized user
  [Tags]  webdav  forbidden  mkcol
  [Setup]  Setup default SA
  Create empty working directory
  ${TEST_CURL_OPTIONS}  Get CURL default x509 options
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_REMOTE_DIRNAME}
  ${stdout}  ${stderr}  Do CURL MKCOL  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA

WebDAV MKCOL VO directory with the wrong proxy
  [Tags]  webdav  forbidden  mkcol  no-gridhttps
  [Setup]  Setup default SA
  Create empty working directory
  ${TEST_CURL_OPTIONS}  Get CURL VOMS proxy options  ${DEFAULT_USER}  ${SA.2}
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_REMOTE_DIRNAME}
  ${stdout}  ${stderr}  Do CURL MKCOL  ${url}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA

######## PROPFIND ##########

WebDAV PROPFIND allprop VO file as anonymous
  [Tags]  webdav  forbidden  propfind
  [Setup]  Setup default SA
  Create working directory
  ${body}  Get PROPFIND ALLPROP body
  ${url}  Build URL  ${DAVEndpoint}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL PROPFIND  ${url}  ${body}  ${TEST_LOCAL_FILEPATH}
  Should Match Regexp  ${stdout}  (403|401 Unauthorized)
  [Teardown]  Teardown default SA

WebDAV PROPFIND allprop VO file as authenticated but not authorized user
  [Tags]  webdav  forbidden  propfind
  [Setup]  Setup default SA
  Create working directory
  ${body}  Get PROPFIND ALLPROP body
  ${TEST_CURL_OPTIONS}  Get CURL default x509 options
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL PROPFIND  ${url}  ${body}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA

WebDAV PROPFIND allprop VO file with the wrong proxy
  [Tags]  webdav  forbidden  propfind  no-gridhttps
  [Setup]  Setup default SA
  Create working directory
  ${body}  Get PROPFIND ALLPROP body
  ${TEST_CURL_OPTIONS}  Get CURL VOMS proxy options  ${DEFAULT_USER}  ${SA.2}
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL PROPFIND  ${url}  ${body}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403
  [Teardown]  Teardown default SA

########## COPY ###########

WebDAV COPY VO file as anonymous
  [Tags]  webdav  forbidden  copy
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${DAVEndpoint}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${DAVEndpoint}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  ${stdout}  ${stderr}  Do CURL COPY  ${srcURL}  ${dstURL}
  Should Match Regexp  ${stdout}  (403|401 Unauthorized)
  [Teardown]  Teardown default SA

WebDAV COPY VO file to another VO SA with the wrong proxy
  [Tags]  webdav  forbidden  copy
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${SA.2}  ${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL COPY  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403 status code: 403, reason phrase: Forbidden
  [Teardown]  Teardown default SA

WebDAV COPY VO file to another VO SA with the right proxy
  [Documentation]  403 since v1.11.18
  [Tags]  webdav  forbidden  copy
  [Setup]  Setup SA and VO  ${DAVSecureEndpoint}  ${SA.7}  ${DEFAULT_USER}  ${VO.1}
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${SA.7}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_FILENAME}
  ${TEST_CURL_OPTIONS}  Get CURL default VOMS proxy options
  ${stdout}  ${stderr}  Do CURL COPY  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  403 status code: 403, reason phrase: Forbidden
  [Teardown]  Teardown default SA

########## MOVE ###########

WebDAV MOVE VO file as anonymous
  [Tags]  webdav  forbidden  move
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${DAVEndpoint}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${DAVEndpoint}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}_2
  ${stdout}  ${stderr}  Do CURL MOVE  ${srcURL}  ${dstURL}
  Should Match Regexp  ${stdout}  (403|401 Unauthorized)
  [Teardown]  Teardown default SA

WebDAV MOVE VO file to another VO SA with the wrong proxy
  [Documentation]  400 instead of 403 since v1.11.18
  [Tags]  webdav  forbidden  move
  [Setup]  Setup default SA
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${SA.2}  ${TEST_FILENAME}
  ${stdout}  ${stderr}  Do CURL MOVE  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  400
  Should Contain  ${stdout}  Move across storage areas is not supported
  [Teardown]  Teardown default SA

WebDAV MOVE VO file to another VO SA with the right proxy
  [Documentation]  400 since v1.11.18
  [Tags]  webdav  forbidden  move
  [Setup]  Setup SA and VO  ${DAVSecureEndpoint}  ${SA.7}  ${DEFAULT_USER}  ${VO.1}
  Create working directory
  ${srcURL}  Build URL  ${TEST_ENDPOINT}  ${SA.7}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  ${dstURL}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_FILENAME}
  ${TEST_CURL_OPTIONS}  Get CURL default VOMS proxy options
  ${stdout}  ${stderr}  Do CURL MOVE  ${srcURL}  ${dstURL}  ${TEST_CURL_OPTIONS}
  Should Contain  ${stdout}  400
  Should Contain  ${stdout}  Move across storage areas is not supported
  [Teardown]  Teardown default SA
