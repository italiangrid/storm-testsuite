*** Keywords ***

Get Access Token  [Arguments]  ${clientId}  ${clientSecret}  ${username}  ${password}  ${scopes}
  ${tokenUrl}=  Set Variable  ${iamEndpoint}/token
  ${contentType}=  Set Variable  -H "Content-Type: application/x-www-form-urlencoded"
  ${credentials}=  Set Variable  -u "${clientId}:${clientSecret}"
  ${data}=  Set Variable  -d "grant_type=password" -d "scope=${scopes}" -d "username=${username}" -d "password=${password}"
  ${out}  ${err}  Curl  POST  ${tokenUrl}  ${contentType} ${credentials} ${data}
  ${jsonData} =  Get Line  ${out}  -1
  ${parsedData}  Parse Json  ${jsonData}
  [Return]  ${parsedData["access_token"]}
