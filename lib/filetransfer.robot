*** Keywords ***

##### URL BUILDING

Build FileTransfer URL  [Arguments]  ${endpoint}  ${path}
  ${output}  Set variable  ${endpoint}/${path}
  [Return]  ${output}

##### METHODS

FileTransfer GET  [Arguments]  ${endpoint}  ${storageArea}  ${relativePath}  ${credentials}=${EMPTY}
  ${url}  Build FileTransfer URL  ${endpoint}  ${storageArea}/${relativePath}
  ${output}  ${rc}  Curl  GET  ${url}  ${credentials} -iv
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}

FileTransfer PUT file  [Arguments]  ${endpoint}  ${storageArea}  ${relativePath}  ${localFilePath}  ${credentials}=${EMPTY}
  ${url}  Build FileTransfer URL  ${endpoint}  ${storageArea}/${relativePath}
  ${output}  ${rc}  Curl  PUT  ${url}  -T ${localFilePath} -iv ${credentials}
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}

FileTransfer PUT data  [Arguments]  ${endpoint}  ${storageArea}  ${relativePath}  ${data}  ${credentials}=${EMPTY}
  ${body}  Set body  ${data}
  ${url}  Build FileTransfer URL  ${endpoint}  ${storageArea}/${relativePath}
  ${output}  ${rc}  Curl  PUT  ${url}  ${body} -iv ${credentials}
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}
