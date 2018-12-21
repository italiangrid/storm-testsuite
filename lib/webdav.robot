*** Keywords ***

##### HTTP/WEBDAV METHODS - CURL KEYWORDS

Do CURL HEAD  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${rc}  Curl  HEAD  ${url}  --head ${options}
  [Return]  ${output}  ${rc}

Do CURL HEAD and check success  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${rc}  Do CURL HEAD  ${url}  ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  200 OK
  [Return]  ${output}  ${rc}

Do CURL GET  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${rc}  Curl  GET  ${url}  ${options}
  [Return]  ${output}  ${rc}

Do CURL GET and check success  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${rc}  Do CURL GET  ${url}  ${options}
  Should Contain  ${output}  200 OK
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}  ${rc}

Do CURL partial GET  [Arguments]  ${url}  ${rangelist}  ${options}=${EMPTY}
  ${rangeheader}  Get CURL header  Range  bytes=${rangelist}
  ${output}  ${rc}  Do CURL GET  ${url}  ${rangeheader} ${options}
  [Return]  ${output}  ${rc}

Do CURL partial GET and check success  [Arguments]  ${url}  ${rangelist}  ${options}=${EMPTY}
  ${output}  ${rc}  Do CURL partial GET  ${url}  ${rangelist}  ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  206 Partial Content
  [Return]  ${output}  ${rc}

Do CURL PUT  [Arguments]  ${url}  ${localFilePath}  ${options}=${EMPTY}
  ${output}  ${rc}  Curl  PUT  ${url}  -T ${localFilePath} ${options}
  [Return]  ${output}  ${rc}

Do CURL PUT and check success  [Arguments]  ${url}  ${localFilePath}  ${options}=${EMPTY}
  ${output}  ${rc}  Curl  PUT  ${url}  -T ${localFilePath} ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  201 Created
  [Return]  ${output}  ${rc}

Do CURL PUT and check overwrite success  [Arguments]  ${url}  ${localFilePath}  ${options}=${EMPTY}
  ${output}  ${rc}  Curl  PUT  ${url}  -T ${localFilePath} ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  204 No Content
  [Return]  ${output}  ${rc}

Do CURL MKCOL  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${rc}  Curl  MKCOL  ${url}  ${options}
  [Return]  ${output}  ${rc}

Do CURL MKCOL and check success  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${rc}  Do CURL MKCOL  ${url}  ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  201 Created
  [Return]  ${output}  ${rc}

Do CURL DELETE  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${rc}  Curl  DELETE  ${url}  ${options}
  [Return]  ${output}  ${rc}

Do CURL DELETE and check success  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${rc}  Do CURL DELETE  ${url}  ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  204 No Content
  [Return]  ${output}  ${rc}

Do CURL COPY  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${destHeader}  Get CURL header  Destination  ${destURL}
  ${output}  ${rc}  Curl  COPY  ${srcURL}  ${destHeader} ${options}
  [Return]  ${output}  ${rc}

Do CURL COPY and check success  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${output}  ${rc}  Do CURL COPY  ${srcURL}  ${destURL}  ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  201 Created
  [Return]  ${output}  ${rc}

Do CURL COPY and check overwrite success  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${output}  ${rc}  Do CURL COPY  ${srcURL}  ${destURL}  ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  204 No Content
  [Return]  ${output}  ${rc}

Do CURL MOVE  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${destHeader}  Get CURL header  Destination  ${destURL}
  ${output}  ${rc}  Curl  MOVE  ${srcURL}  ${destHeader} ${options}
  [Return]  ${output}  ${rc}

Do CURL MOVE and check success  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${output}  ${rc}  Do CURL MOVE  ${srcURL}  ${destURL}  ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  201 Created
  [Return]  ${output}  ${rc}

Do CURL MOVE and check overwrite success  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${output}  ${rc}  Do CURL MOVE  ${srcURL}  ${destURL}  ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  204 No Content
  [Return]  ${output}  ${rc}

Do CURL PROPFIND  [Arguments]  ${url}  ${bodyContent}  ${options}=${EMPTY}
  ${body}  Get CURL body  ${bodyContent}
  ${output}  ${rc}  Curl  PROPFIND  ${url}  ${body} ${options}
  [Return]  ${output}  ${rc}

Do CURL PROPFIND and check success  [Arguments]  ${url}  ${bodyContent}  ${options}=${EMPTY}
  ${output}  ${rc}  Do CURL PROPFIND  ${url}  ${bodyContent}  ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  207 Multi-status
  [Return]  ${output}  ${rc}

Do CURL OPTIONS  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${rc}  Curl  OPTIONS  ${url}  ${options}
  [Return]  ${output}  ${rc}

Do CURL OPTIONS and check success  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${rc}  Do CURL OPTIONS  ${url}  ${options}
  Should Be Equal As Integers  ${rc}  0
  Should Contain  ${output}  200 OK
  Should Contain  ${output}  DAV: 1
  [Return]  ${output}  ${rc}

