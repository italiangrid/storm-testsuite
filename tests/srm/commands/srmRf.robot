*** Settings ***

Resource   lib/import.robot

*** Keywords ***

Get random simple SURL
  ${filename}  Get a unique name
  ${surl}  Build simple surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  [Return]  ${surl}

Get random query SURL
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  [Return]  ${surl}

Create remote file  [Arguments]  ${surl}
  Put without really putting using clientSRM  ${surl}

Do PTG  [Arguments]  ${surl}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_FILE_PINNED
  [Return]  ${token}

Remove remote file  [Arguments]  ${surl}
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS

Release file with SURL and TOKEN  [Arguments]  ${surl}  ${token}
  ${output}  Perform rf using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  Should Not Contain  ${output}  SRM_RELEASED
  Should Not Contain  ${output}  SRM_FAILURE

Release file with SURL  [Arguments]  ${surl}
  ${output}  Perform rf using clientSRM without token  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  Should Not Contain  ${output}  SRM_RELEASED
  Should Not Contain  ${output}  SRM_FAILURE

Release file with TOKEN  [Arguments]  ${token}
  ${output}  Perform rf using clientSRM without surl  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  Should Not Contain  ${output}  SRM_RELEASED
  Should Not Contain  ${output}  SRM_FAILURE

Invalid release file with TOKEN  [Arguments]  ${token}
  ${output}  Perform rf using clientSRM without surl  ${token}
  Should Not Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  SRM_INVALID_PATH
  Should Contain  ${output}  SRM_FAILURE


*** Test Cases ***

Release file using SURL and TOKEN
  [Tags]  storm-client  rf
  [Setup]  Use default voms proxy
  ${surl}  Get random simple SURL
  Create remote file  ${surl}
  ${token}  Do PTG  ${surl}
  Release file with SURL and TOKEN  ${surl}  ${token}
  Remove remote file  ${surl}
  [Teardown]  Clear all credentials

Release file using only SURL
  [Tags]  storm-client  rf
  [Setup]  Use default voms proxy
  ${surl}  Get random simple SURL
  Create remote file  ${surl}
  Do PTG  ${surl}
  Release file with SURL  ${surl}
  Remove remote file  ${surl}
  [Teardown]  Clear all credentials

Release file using only TOKEN
  [Tags]  storm-client  rf
  [Setup]  Use default voms proxy
  ${surl}  Get random simple SURL
  Create remote file  ${surl}
  ${token}  Do PTG  ${surl}
  Release file with TOKEN  ${token}
  Remove remote file  ${surl}
  [Teardown]  Clear all credentials

Release file using SURL and TOKEN with SURL in query form
  [Tags]  storm-client  rf
  [Setup]  Use default voms proxy
  ${surl}  Get random query SURL
  Create remote file  ${surl}
  ${token}  Do PTG  ${surl}
  Release file with SURL and TOKEN  ${surl}  ${token}
  Remove remote file  ${surl}
  [Teardown]  Clear all credentials

Release file using only SURL with SURL in query form
  [Tags]  storm-client  rf
  [Setup]  Use default voms proxy
  ${surl}  Get random query SURL
  Create remote file  ${surl}
  Do PTG  ${surl}
  Release file with SURL  ${surl}
  Remove remote file  ${surl}
  [Teardown]  Clear all credentials

Release file using only TOKEN with SURL in query form
  [Tags]  storm-client  rf
  [Setup]  Use default voms proxy
  ${surl}  Get random query SURL
  Create remote file  ${surl}
  ${token}  Do PTG  ${surl}
  Release file with TOKEN  ${token}
  Remove remote file  ${surl}
  [Teardown]  Clear all credentials

Release multiple ptg requests specifying only SURL
  [Tags]  storm-client  rf
  [Documentation]  Regression test for https://issues.infn.it/jira/browse/STOR-305 srmReleaseFiles doesn't release multiple files at once.
  [Setup]  Use default voms proxy
  ${surl}  Get random simple SURL
  Create remote file  ${surl}
  Do PTG  ${surl}
  Do PTG  ${surl}
  Release file with SURL  ${surl}
  Remove remote file  ${surl}
  [Teardown]  Clear all credentials

Release multiple ptg requests specifying only SURL in query form
  [Tags]  storm-client  rf
  [Documentation]  Regression test for https://issues.infn.it/jira/browse/STOR-305 srmReleaseFiles doesn't release multiple files at once.
  [Setup]  Use default voms proxy
  ${surl}  Get random query SURL
  Create remote file  ${surl}
  Do PTG  ${surl}
  Do PTG  ${surl}
  Release file with SURL  ${surl}
  Remove remote file  ${surl}
  [Teardown]  Clear all credentials

Release multiple files specifying only TOKEN
  [Tags]  storm-client  rf
  [Setup]  Use default voms proxy
  ${surl}  Get random simple SURL
  Create remote file  ${surl}
  ${surl2}  Get random simple SURL
  Create remote file  ${surl2}
  ${token}  Do PTG  ${surl} ${surl2}
  Release file with TOKEN  ${token}
  Remove remote file  ${surl}
  Remove remote file  ${surl2}
  [Teardown]  Clear all credentials