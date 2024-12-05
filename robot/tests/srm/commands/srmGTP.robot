*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Verify gtp operation by using the StoRM client
  [Tags]  gtp  storm-client
  [Setup]  Use default voms proxy
  ${output}  Execute clientSRM Command  gtp
  Should Contain  ${output}  transferProtocol="file"
  Should Contain  ${output}  transferProtocol="http"
  Should Contain  ${output}  transferProtocol="https"
  [Teardown]  Clear all credentials