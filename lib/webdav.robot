*** Keywords ***

##### HTTP/WEBDAV METHODS - CURL KEYWORDS

Do CURL HEAD  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${stderr}  Curl  HEAD  ${url}  --head ${options}
  [Return]  ${output}  ${stderr}

Do CURL HEAD and check success  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${stderr}  Do CURL HEAD  ${url}  ${options}
  Should Contain  ${output}  200 OK
  [Return]  ${output}  ${stderr}

Do CURL GET  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${stderr}  Curl  GET  ${url}  ${options}
  [Return]  ${output}  ${stderr}

Do CURL GET and check success  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${stderr}  Do CURL GET  ${url}  ${options}
  Should Contain  ${output}  200 OK
  [Return]  ${output}  ${stderr}

Do CURL partial GET  [Arguments]  ${url}  ${rangelist}  ${options}=${EMPTY}
  ${rangeheader}  Get CURL header  Range  bytes=${rangelist}
  ${output}  ${stderr}  Do CURL GET  ${url}  ${rangeheader} ${options}
  [Return]  ${output}  ${stderr}

Do CURL partial GET and check success  [Arguments]  ${url}  ${rangelist}  ${options}=${EMPTY}
  ${output}  ${stderr}  Do CURL partial GET  ${url}  ${rangelist}  ${options}
  Should Contain  ${output}  206 Partial Content
  [Return]  ${output}  ${stderr}

Do CURL PUT  [Arguments]  ${url}  ${localFilePath}  ${options}=${EMPTY}
  ${output}  ${stderr}  Curl  PUT  ${url}  -T ${localFilePath} ${options}
  [Return]  ${output}  ${stderr}

Do CURL PUT and check success  [Arguments]  ${url}  ${localFilePath}  ${options}=${EMPTY}
  ${output}  ${stderr}  Curl  PUT  ${url}  -T ${localFilePath} ${options}
  Should Contain  ${output}  201 Created
  [Return]  ${output}  ${stderr}

Do CURL PUT and check overwrite success  [Arguments]  ${url}  ${localFilePath}  ${options}=${EMPTY}
  ${output}  ${stderr}  Curl  PUT  ${url}  -T ${localFilePath} ${options}
  Should Contain  ${output}  204 No Content
  [Return]  ${output}  ${stderr}

Do CURL MKCOL  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${stderr}  Curl  MKCOL  ${url}  ${options}
  [Return]  ${output}  ${stderr}

Do CURL MKCOL and check success  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${stderr}  Do CURL MKCOL  ${url}  ${options}
  Should Contain  ${output}  201 Created
  [Return]  ${output}  ${stderr}

Do CURL DELETE  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${stderr}  Curl  DELETE  ${url}  ${options}
  [Return]  ${output}  ${stderr}

Do CURL DELETE and check success  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${stderr}  Do CURL DELETE  ${url}  ${options}
  Should Contain  ${output}  204 No Content
  [Return]  ${output}  ${stderr}

Do CURL COPY  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${destHeader}  Get CURL header  Destination  ${destURL}
  ${output}  ${stderr}  Curl  COPY  ${srcURL}  ${destHeader} ${options}
  [Return]  ${output}  ${stderr}

Do CURL COPY and check success  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${output}  ${stderr}  Do CURL COPY  ${srcURL}  ${destURL}  ${options}
  Should Contain  ${output}  201 Created
  [Return]  ${output}  ${stderr}

Do CURL COPY and check overwrite success  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${output}  ${stderr}  Do CURL COPY  ${srcURL}  ${destURL}  ${options}
  Should Contain  ${output}  204 No Content
  [Return]  ${output}  ${stderr}

Do CURL MOVE  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${destHeader}  Get CURL header  Destination  ${destURL}
  ${output}  ${stderr}  Curl  MOVE  ${srcURL}  ${destHeader} ${options}
  [Return]  ${output}  ${stderr}

Do CURL MOVE and check success  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${output}  ${stderr}  Do CURL MOVE  ${srcURL}  ${destURL}  ${options}
  Should Contain  ${output}  201 Created
  [Return]  ${output}  ${stderr}

Do CURL MOVE and check overwrite success  [Arguments]  ${srcURL}  ${destURL}  ${options}=${EMPTY}
  ${output}  ${stderr}  Do CURL MOVE  ${srcURL}  ${destURL}  ${options}
  Should Contain  ${output}  204 No Content
  [Return]  ${output}  ${stderr}

Do CURL PROPFIND  [Arguments]  ${url}  ${bodyContent}  ${options}=${EMPTY}
  ${body}  Get CURL body  ${bodyContent}
  ${output}  ${stderr}  Curl  PROPFIND  ${url}  ${body} ${options}
  [Return]  ${output}  ${stderr}

Do CURL PROPFIND and check success  [Arguments]  ${url}  ${bodyContent}  ${options}=${EMPTY}
  ${output}  ${stderr}  Do CURL PROPFIND  ${url}  ${bodyContent}  ${options}
  Should Contain  ${output}  207 Multi-status
  [Return]  ${output}  ${stderr}

Do CURL OPTIONS  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${stderr}  Curl  OPTIONS  ${url}  ${options}
  [Return]  ${output}  ${stderr}

Do CURL OPTIONS and check success  [Arguments]  ${url}  ${options}=${EMPTY}
  ${output}  ${stderr}  Do CURL OPTIONS  ${url}  ${options}
  Should Contain  ${output}  200 OK
  Should Contain  ${output}  DAV: 1
  [Return]  ${output}  ${stderr}

