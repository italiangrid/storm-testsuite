*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Ping using clientSRM
  [Tags]  ping  storm-client
  [Setup]  Use default voms proxy
  ${output}  Perform ping using clientSRM
  Should contain  ${output}  SRM server successfully contacted
  [Teardown]  Clear all credentials

Ping returns a wrong backend age
  [Tags]  ping  storm-client
  [Setup]  Use default voms proxy
  ${output}  Perform ping using clientSRM
  ${matched}  Should Match Regexp  ${output}  <BE:.+>
  Should Not Contain  ${matched}  age
  [Teardown]  Clear all credentials

Verify asynch request with non-ascii characters
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/137. 
  ...    Given a StoRM endpoint, verify that an SRM asynchronous call providing a string 
  ...    parameter containing non ASCII characters does not put StoRM Frontend offline.
  [Tags]  storm-client  ping  regression
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${bytes}  Encode String To Bytes  ${TESTDIR}/${filename}_òàòà  UTF-8
  ${surl}  Build surl  ${DEFAULT_SA}  ${bytes}
  ${output}  Perform ls using clientSRM  ${surl}  -c 1
  Should Not Contain  ${output}  SRM_SUCCESS
  ${output}  Perform ping using clientSRM
  Should contain  ${output}  SRM server successfully contacted
  [Teardown]  Clear all credentials