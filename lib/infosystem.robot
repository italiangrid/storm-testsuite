*** Keywords ***

Build lurl
  RETURN  ldap://${ldapEndpoint}

Define expression with objectclass  [Arguments]  ${objectClass}
  RETURN  objectclass=${objectClass}

Define expression with attribute and value  [Arguments]  ${attribute}  ${value}
  RETURN  ${attribute}={value}

Define GlueService filter
  ${expr}  Define expression with objectclass  GlueService
  RETURN  '(${expr})'

Define GLUE2StorageService filter
  ${expr}  Define expression with objectclass  GLUE2StorageService
  RETURN  '(${expr})'

Define GLUE2Endpoint filter
  ${expr}  Define expression with objectclass  GLUE2Endpoint
  RETURN  '(${expr})'

Define filter that checks GLUE2EndpointInterfaceName is not set to  [Arguments]  ${value}
  ${expr}  Define expression with objectclass  GLUE2Endpoint
  RETURN  '(&(${expr})(GLUE2EndpointInterfaceName=${value}))'

Define filter that checks GLUE2EndpointCapability is not set to  [Arguments]  ${value} 
  ${expr}  Define expression with objectclass  GLUE2Endpoint
  RETURN  '(&(${expr})(GLUE2EndpointCapability=${value}))'

Define filter that checks GLUE2EndpointServingState is not set to  [Arguments]  ${value}
  ${expr}  Define expression with objectclass  GLUE2Endpoint
  RETURN  '(&(${expr})(GLUE2EndpointServingState=${value}))'

Define filter that checks GLUE2EndpointQualityLevel is not set to  [Arguments]  ${value}
  ${expr}  Define expression with objectclass  GLUE2Endpoint
  RETURN  '(&(${expr})(GLUE2EndpointQualityLevel=${value}))'

Define GLUE2StorageShare filter
  ${expr}  Define expression with objectclass  GLUE2StorageShare
  RETURN  '(${expr})'

Define filter to get GLUE2StorageServiceCapacity size  [Arguments]  ${line}
  ${expr}  Define expression with objectclass  GLUE2StorageServiceCapacity
  RETURN  '(&(${expr})(GLUE2StorageServiceCapacityType=${line}))'

Get attribute value using ldapsearch  [Arguments]  ${lurl}  ${baseDN}  ${filter}  ${attribute}
  ${output}  Run  ldapsearch -x -H ${lurl} -b ${baseDN} ${filter} ${attribute}
  RETURN  ${output}

Get values using ldapsearch  [Arguments]  ${lurl}  ${baseDN}  ${filter}
  ${output}  Run  ldapsearch -x -H ${lurl} -b ${baseDN} ${filter}
  RETURN  ${output}
