*** Keywords ***

Get metadata of  [Arguments]  ${sa}  ${path}
  ${output}  Request Metadata For  ${sa}  ${path}
  ${data}  Parse Metadata  ${output}
  [Return]  ${data}

Request Metadata For  [Arguments]  ${sa}  ${path}
  ${output}  ${stderr}  Curl  GET  http://${recallEndpoint}/metadata/${sa}/${path}  -H "Token:${xmlrpcToken}"
  [Return]  ${output}

Unauthorized Request Metadata For  [Arguments]  ${sa}  ${path}
  ${output}  ${stderr}  Curl  GET  http://${recallEndpoint}/metadata/${sa}/${path}
  [Return]  ${output}

Parse Metadata  [Arguments]  ${httpRepsonse}
  Should Contain  ${httpRepsonse}  200 OK
  ${jsonData} =  Get Line  ${httpRepsonse}  -1
  Log  ${jsonData}
  ${parsedData}  Parse Json  ${jsonData}
  Log  ${parsedData}
  [Return]  ${parsedData}
