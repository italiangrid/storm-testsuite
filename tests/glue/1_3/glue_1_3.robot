*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Check the GlueServiceType value does not contain emi.storm
  [Tags]  information-system
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/143
  ${lurl}  Build lurl
  ${filterGlueService}  Define GlueService filter 
  ${output}  Get attribute value using ldapsearch  ${lurl}  ${baseDNGlue}  ${filterGlueService}  GlueServiceType
  Should Not Contain  ${output}  emi.storm

Check the GlueServiceName value does not contain emi.storm
  [Tags]  information-system
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/143
  ${lurl}  Build lurl
  ${filterGlueService}  Define GlueService filter
  ${output}  Get attribute value using ldapsearch  ${lurl}  ${baseDNGlue}  ${filterGlueService}  GlueServiceName
  Should Not Contain  ${output}  emi.storm
