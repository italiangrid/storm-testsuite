*** Settings ***

Resource   lib/import.robot

*** Keywords ***

Get random simple SURL
  ${filename}  Get a unique name
  ${surl}  Build simple surl  ${TAPE_SA}  ${TESTDIR}/${filename}
  [Return]  ${surl}

*** Test Cases ***

Bol online file
  [Tags]  storm-client  bol
  [Setup]  Use voms proxy  ${defaultUser}  ${TAPE_SA_VONAME}
  ${surl}  Get random simple SURL
  Put without really putting using clientSRM  ${surl}
  ${output}  ${token}  Perform bol using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Bol with invalid SURL
  [Tags]  storm-client  bol
  [Setup]  Use voms proxy  ${defaultUser}  ${TAPE_SA_VONAME}
  ${surl}  Get random simple SURL
  ${output}  ${token}  Perform bol using clientSRM  ${surl}  -p
  Should Not Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  SRM_FAILURE
  [Teardown]  Clear all credentials

Bol multiple invalid SURLs
  [Tags]  storm-client  bol
  [Setup]  Use voms proxy  ${defaultUser}  ${TAPE_SA_VONAME}
  ${surl}  Get random simple SURL
  ${surl2}  Get random simple SURL
  ${output}  ${token}  Perform bol using clientSRM  ${surl} ${surl2}  -p
  Should Contain  ${output}  SRM_FAILURE
  [Teardown]  Clear all credentials

Bol multiple online files
  [Tags]  storm-client  bol
  [Setup]  Use voms proxy  ${defaultUser}  ${TAPE_SA_VONAME}
  ${surl}  Get random simple SURL
  ${surl2}  Get random simple SURL
  Put without really putting using clientSRM  ${surl}
  Put without really putting using clientSRM  ${surl2}
  ${output}  ${token}  Perform bol using clientSRM  ${surl} ${surl2}  -p
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rm using clientSRM  ${surl2}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Bol multiple mixed files
  [Tags]  storm-client  bol
  [Setup]  Use voms proxy  ${defaultUser}  ${TAPE_SA_VONAME}
  ${surl}  Get random simple SURL
  ${surl2}  Get random simple SURL
  Put without really putting using clientSRM  ${surl}
  ${output}  ${token}  Perform bol using clientSRM  ${surl} ${surl2}  -p
  Should Contain  ${output}  SRM_PARTIAL_SUCCESS
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials