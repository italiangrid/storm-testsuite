*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Put done an existent file
  [Tags]  storm-client  pd
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  Perform rm using clientSRM  ${surl}
  [Teardown]  Clear all credentials

Duplicated put done
  [Tags]  storm-client  pd
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_DUPLICATION_ERROR
  Perform rm using clientSRM  ${surl}
  [Teardown]  Clear all credentials