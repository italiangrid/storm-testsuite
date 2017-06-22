*** Keywords ***

Get Access Token With Read Scope  [Arguments]  ${username}  ${password}
  ${token}  Get Access Token  ${cdmiClientId}  ${cdmiClientSecret}  ${username}  ${password}  openid profile testvo:read
  [Return]  ${token}

Get Access Token With Recall Scope
  ${token}  Get Access Token As Client  ${cdmiClientId}  ${cdmiClientSecret}  openid profile testvo:recall
  [Return]  ${token}

Get Access Token With All Scopes
  ${token}  Get Access Token As Client  ${cdmiClientId}  ${cdmiClientSecret}  openid profile testvo:read testvo:recall
  [Return]  ${token}

Get Access Token As User  [Arguments]  ${scopes}
  ${token}  Get Access Token As Client  ${cdmiClientId}  ${cdmiClientSecret}  ${scopes}
  [Return]  ${token}

Get CDMI Capabilities  [Arguments]  ${credentials}
  ${data}  Get Json Data  http://${cdmiEndpoint}/cdmi_capabilities/  -i ${credentials}
  [Return]  ${data}

Get CDMI Capability  [Arguments]  ${path}  ${credentials}
  ${data}  Get Json Data  http://${cdmiEndpoint}/cdmi_capabilities/${path}  -i ${credentials}
  [Return]  ${data}

Get CDMI Status  [Arguments]  ${path}  ${credentials}
  ${data}  Get Json Data  http://${cdmiEndpoint}/${path}  -i ${credentials}
  [Return]  ${data}

Get Json Data  [Arguments]  ${url}  ${options}
  ${output}  ${stderr}  Curl  GET  ${url}  ${options}
  ${jsonData} =  Get Line  ${output}  -1
  ${parsedData}  Parse Json  ${jsonData}
  [Return]  ${parsedData}
