*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Check the Glue2Service contains objectClass: GLUE2StorageService
  [Tags]  information-system
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/245
  ${lurl}  Build lurl
  ${filterGlue2StorageService}  Define GLUE2StorageService filter
  ${output}  Get values using ldapsearch  ${lurl}  ${baseDNGlue2}  ${filterGlue2StorageService}
  Should Contain  ${output}  objectClass: GLUE2StorageService

Check that GLUE2EndpointCapability does not contain information.*
  [Tags]  information-system
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/208
  ${lurl}  Build lurl
  ${filterGlue2EndpointCapability}  Define filter that checks GLUE2EndpointCapability is not set to  information.*
  ${output}  Get values using ldapsearch  ${lurl}  ${baseDNGlue2}  ${filterGlue2EndpointCapability}
  Should Contain  ${output}  result: 0 Success
  Should Not Contain  ${output}  numEntries

Check that GLUE2EndpointInterfaceName does not contain emi.storm
  [Tags]  information-system
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/208
  ${lurl}  Build lurl
  ${filterGlue2EndpointInterfaceName}  Define filter that checks GLUE2EndpointInterfaceName is not set to  emi.storm
  ${output}  Get values using ldapsearch  ${lurl}  ${baseDNGlue2}  ${filterGlue2EndpointInterfaceName}
  Should Contain  ${output}  result: 0 Success
  Should Not Contain  ${output}  numEntries

Check that GLUE2StorageShareAccessMode is not returned
  [Tags]  information-system
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/207
  ${lurl}  Build lurl
  ${filterGlue2StorageShare}  Define GLUE2StorageShare filter
  ${output}  Get attribute value using ldapsearch  ${lurl}  ${baseDNGlue2}  ${filterGlue2StorageShare}  GLUE2StorageShareAccessMode
  Should Contain  ${output}  result: 0 Success
  Should Not Contain  ${output}  GLUE2StorageShareAccessMode:

Check that GLUE2EndpointSupportedProfile is not returned
  [Tags]  information-system
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/207
  ${lurl}  Build lurl
  ${filterGlue2Endpoint}  Define GLUE2Endpoint filter
  ${output}  Get attribute value using ldapsearch  ${lurl}  ${baseDNGlue2}  ${filterGlue2Endpoint}  GLUE2EndpointSupportedProfile
  Should Contain  ${output}  result: 0 Success
  Should Not Contain  ${output}  GLUE2EndpointSupportedProfile:

Check that GLUE2EndpointInterfaceExtension is not returned
  [Tags]  information-system
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/207
  ${lurl}  Build lurl
  ${filterGlue2Endpoint}  Define GLUE2Endpoint filter
  ${output}  Get attribute value using ldapsearch  ${lurl}  ${baseDNGlue2}  ${filterGlue2Endpoint}  GLUE2EndpointInterfaceExtension
  Should Contain  ${output}  result: 0 Success
  Should Not Contain  ${output}  GLUE2EndpointInterfaceExtension:

Check that GLUE2EndpointIssuerCA is not returned
  [Tags]  information-system
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/207
  ${lurl}  Build lurl
  ${filterGlue2Endpoint}  Define GLUE2Endpoint filter
  ${output}  Get attribute value using ldapsearch  ${lurl}  ${baseDNGlue2}  ${filterGlue2Endpoint}  GLUE2EndpointIssuerCA
  Should Contain  ${output}  result: 0 Success

Check that GLUE2EndpointTrustedCA is not returned
  [Tags]  information-system
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/207
  ${lurl}  Build lurl
  ${filterGlue2Endpoint}  Define GLUE2Endpoint filter
  ${output}  Get attribute value using ldapsearch  ${lurl}  ${baseDNGlue2}  ${filterGlue2Endpoint}  GLUE2EndpointTrustedCA
  Should Contain  ${output}  result: 0 Success

Check that GLUE2StorageServiceCapacityTotalSize for the online capacity type is not zero
  [Tags]  information-system
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/147
  ${lurl}  Build lurl
  ${filterGlue2StorageServiceCapacity}  Define filter to get GLUE2StorageServiceCapacity size  online
  ${output}  Get attribute value using ldapsearch  ${lurl}  ${baseDNGlue2}  ${filterGlue2StorageServiceCapacity}  GLUE2StorageServiceCapacityTotalSize
  ${lines}  Get Lines Containing String  ${output}  GLUE2StorageServiceCapacityTotalSize: 
  FOR  ${line}  IN  ${lines}
    ${others}  ${last}=  Split String From Right  ${line}
    Should Not Be Equal  '${last}'  '0'
  END

Check that GLUE2EndpointServingState does not contain emi.storm.backend
  [Tags]  information-system
  [Documentation]  Regression test for https://issues.infn.it/jira/browse/STOR-103
  ${lurl}  Build lurl
  ${filterGlue2EndpointServingState}  Define filter that checks GLUE2EndpointServingState is not set to  emi.storm.backend
  ${output}  Get values using ldapsearch  ${lurl}  ${baseDNGlue2}  ${filterGlue2EndpointServingState}
  Should Contain  ${output}  result: 0 Success
  Should Not Contain  ${output}  numEntries

Check that GLUE2EndpointQualityLevel does not contain Testing
  [Tags]  information-system
  [Documentation]  Regression test for https://issues.infn.it/jira/browse/STOR-103
  ${lurl}  Build lurl
  ${filterGlue2EndpointQualityLevel}  Define filter that checks GLUE2EndpointQualityLevel is not set to  Testing
  ${output}  Get values using ldapsearch  ${lurl}  ${baseDNGlue2}  ${filterGlue2EndpointQualityLevel}
  Should Contain  ${output}  result: 0 Success
  Should Not Contain  ${output}  numEntries
