*** Keywords ***

Build lurl
  [Return]  ldap://${ldapEndpoint}

Define expression with objectclass  [Arguments]  ${objectClass}
  [Return]  objectclass=${objectClass}

Define expression with attribute and value  [Arguments]  ${attribute}  ${value}
  [Return]  ${attribute}={value}

Define GlueService filter
  ${expr}  Define expression with objectclass  GlueService
  [Return]  '(${expr})'

Define GLUE2StorageService filter
  ${expr}  Define expression with objectclass  GLUE2StorageService
  [Return]  '(${expr})'

Define GLUE2Endpoint filter
  ${expr}  Define expression with objectclass  GLUE2Endpoint
  [Return]  '(${expr})'

Define filter that checks GLUE2EndpointInterfaceName is not set to  [Arguments]  ${value}
  ${expr}  Define expression with objectclass  GLUE2Endpoint
  [Return]  '(&(${expr})(GLUE2EndpointInterfaceName=${value}))'

Define filter that checks GLUE2EndpointCapability is not set to  [Arguments]  ${value} 
  ${expr}  Define expression with objectclass  GLUE2Endpoint
  [Return]  '(&(${expr})(GLUE2EndpointCapability=${value}))'

Define filter that checks GLUE2EndpointServingState is not set to  [Arguments]  ${value}
  ${expr}  Define expression with objectclass  GLUE2Endpoint
  [Return]  '(&(${expr})(GLUE2EndpointServingState=${value}))'

Define filter that checks GLUE2EndpointQualityLevel is not set to  [Arguments]  ${value}
  ${expr}  Define expression with objectclass  GLUE2Endpoint
  [Return]  '(&(${expr})(GLUE2EndpointQualityLevel=${value}))'

Define GLUE2StorageShare filter
  ${expr}  Define expression with objectclass  GLUE2StorageShare
  [Return]  '(${expr})'

Define filter to get GLUE2StorageServiceCapacity size  [Arguments]  ${line}
  ${expr}  Define expression with objectclass  GLUE2StorageServiceCapacity
  [Return]  '(&(${expr})(GLUE2StorageServiceCapacityType=${line}))'

Get attribute value using ldapsearch  [Arguments]  ${lurl}  ${baseDN}  ${filter}  ${attribute}
  ${output}  Run  ldapsearch -x -H ${lurl} -b ${baseDN} ${filter} ${attribute}
  [Return]  ${output}

Get values using ldapsearch  [Arguments]  ${lurl}  ${baseDN}  ${filter}
  ${output}  Run  ldapsearch -x -H ${lurl} -b ${baseDN} ${filter}
  [Return]  ${output}
