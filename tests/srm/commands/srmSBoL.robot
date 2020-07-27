*** Settings ***

Resource   lib/import.robot

*** Test Cases **

Status of bring online using a non existent token
  [Tags]  regression  sbol
  [Documentation]  Regression test for https://issues.infn.it/browse/STOR-217. StoRM crashed when a status for an async request was requested but the service is not able to get the into out of the database (for example, the token does not exists). This test calls a status for bring online.
  [Setup]  Use default voms proxy
  ${output}  Execute clientSRM Command  bol -t abcde
  [Teardown]  Clear all credentials
