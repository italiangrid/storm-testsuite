*** Keywords ***

Get metadata of  [Arguments]  ${sa}  ${path}
  ${output}  Request Metadata For  ${sa}  ${path}
  ${data}  Parse Metadata  ${output}
  [Return]  ${data}

Request Metadata For  [Arguments]  ${sa}  ${path}
  ${output}  ${rc}  Curl  GET  http://${recallEndpoint}/metadata/${sa}/${path}  -H "Token:${xmlrpcToken}"
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}

Unauthorized Request Metadata For  [Arguments]  ${sa}  ${path}
  ${output}  ${rc}  Curl  GET  http://${recallEndpoint}/metadata/${sa}/${path}
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}

Parse Metadata  [Arguments]  ${httpRepsonse}
  Should Contain  ${httpRepsonse}  200 OK
  ${jsonData} =  Get Line  ${httpRepsonse}  -1
  Log  ${jsonData}
  ${parsedData}   Convert String To Json  ${jsonData}
  Log  ${parsedData}
  [Return]  ${parsedData}
