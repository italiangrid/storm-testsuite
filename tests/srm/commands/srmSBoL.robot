*** Settings ***

Resource   lib/import.robot

*** Test Cases **

Status of bring online of a migrated and not already recalled file
  [Tags]  sbol
  [Setup]  Use voms proxy  ${defaultUser}  ${TAPE_SA_VONAME}
  ${surl}  Build surl  ${TAPE_SA}  test_metadata/tapeonly.txt
  ${output}  ${token}  Perform a BoL with polling  ${surl}
  ${data}  Get first recall task
  ${taskId} =  Get Substring  ${data}  1  37
  Log  ${taskId}
  ${output}  Perform sbol using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_REQUEST_INPROGRESS
  Should Contain  ${output}  Recalling file from tape
  Set success for taskid  ${taskId}
  [Teardown]  Clear all credentials

Status of bring online using a non existent token
  [Tags]  regression  sbol
  [Documentation]  Regression test for https://issues.infn.it/browse/STOR-217. StoRM crashed when a status for an async request was requested but the service is not able to get the into out of the database (for example, the token does not exists). This test calls a status for bring online.
  [Setup]  Use default voms proxy
  ${output}  Execute clientSRM Command  bol -t abcde
  [Teardown]  Clear all credentials

*** Keywords ***

Perform a BoL with polling  [Arguments]  ${surl}
  ${output}  ${token}  Perform bol using clientSRM  ${surl}
  Should Contain  ${output}  SRM_REQUEST_QUEUED
  :FOR  ${i}  IN RANGE  1  100
    \    ${output}  Perform sbol using clientSRM  ${surl}  ${token}
    \    Log  ${output}
    \    ${status}  ${value}=  Run keyword and ignore error  Should Contain  ${output}  SRM_REQUEST_QUEUED
    \    Log  ${status}
    \    Log  ${value}
    \    Run Keyword If    '${status}' == 'FAIL'    Exit For Loop
  Should Contain  ${output}  SRM_REQUEST_INPROGRESS
  [Return]  ${output}  ${token}