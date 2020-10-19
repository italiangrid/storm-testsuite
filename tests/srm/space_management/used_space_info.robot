*** Settings ***

Resource   lib/import.robot

*** Variables ***

${REST_ENDPOINT}       ${backEndHost}:9998
${DIR_SIZE}            4096

*** Test Cases ***

Check db size update after srmPutDone
  [Tags]  info
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Check not exists using gfal-utils  ${surl}
  ${token}  Get SA Token
  ${free_space_before}  Get SA status info parameter  ${token}  free-space
  Copy-out file using gfal-utils  ${filename}  ${surl}
  ${free_space_after}  Get SA status info parameter  ${token}  free-space
  Should not be equal  ${free_space_before}  ${free_space_after}
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${free_space}  Get SA status info parameter  ${token}  free-space
  Should be equal  ${free_space_before}  ${free_space}
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Check db size update after srmRm
  [Tags]  info
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Check not exists using gfal-utils  ${surl}
  ${token}  Get SA Token
  ${free_space}  Get SA status info parameter  ${token}  free-space
  Copy-out file using gfal-utils  ${filename}  ${surl}
  ${free_space_before}  Get SA status info parameter  ${token}  free-space
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${free_space_after}  Get SA status info parameter  ${token}  free-space
  Should not be equal  ${free_space_before}  ${free_space_after}
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Check db size update after srmMkdir
  [Tags]  info  no-btrfs
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${token}  Get SA Token
  ${free_space_1}  Get SA status info parameter  ${token}  free-space
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${free_space_2}  Get SA status info parameter  ${token}  free-space
  Should not be equal  ${free_space_1}  ${free_space_2}
  ${diff}  Diff  ${free_space_1}  ${free_space_2}
  Should be equal as numbers  ${diff}  ${DIR_SIZE}
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${free_space_3}  Get SA status info parameter  ${token}  free-space
  Should be equal as numbers  ${free_space_3}  ${free_space_1}
  [Teardown]  Clear all credentials

Check db size update after a recursive srmRmdir
  [Tags]  info  no-btrfs
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${dsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${token}  Get SA Token
  ${free_space_1}  Get SA status info parameter  ${token}  free-space
  ${output}  Perform mkdir using clientSRM  ${dsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${free_space_2}  Get SA status info parameter  ${token}  free-space
  ${filename}  Create local file
  ${fsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${filename}
  Check not exists using gfal-utils  ${fsurl}
  Copy-out file using gfal-utils  ${filename}  ${fsurl}
  Check exists using gfal-utils  ${fsurl}
  ${free_space_3}  Get SA status info parameter  ${token}  free-space
  ${output}  Perform rmdir using clientSRM  ${dsurl}  -r
  ${free_space_4}  Get SA status info parameter  ${token}  free-space
  Should not be equal  ${free_space_1}  ${free_space_2}
  Should not be equal  ${free_space_2}  ${free_space_3}
  Should not be equal  ${free_space_3}  ${free_space_4}
  Should be equal as numbers  ${free_space_1}  ${free_space_4}
  ${diff}  Diff  ${free_space_2}  ${free_space_3}
  Should be equal as numbers  ${diff}  1048576
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Check db size update after srmRmdir of an empty directory
  [Tags]  info  no-btrfs
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${token}  Get SA Token
  ${free_space_1}  Get SA status info parameter  ${token}  free-space
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${free_space_2}  Get SA status info parameter  ${token}  free-space
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${free_space_3}  Get SA status info parameter  ${token}  free-space
  Should not be equal  ${free_space_1}  ${free_space_2}
  Should be equal as numbers  ${free_space_3}  ${free_space_1}
  ${diff}  Diff  ${free_space_3}  ${free_space_2}
  Should be equal as numbers  ${diff}  ${DIR_SIZE}
  [Teardown]  Clear all credentials

*** Keywords ***

Get From REST endpoint  [Arguments]  ${url}
    Create Http Context  ${REST_ENDPOINT}
    GET  ${url}
    ${status}=  Get Response Status
    Should Start With  ${status}  200
    ${result}=  Get Response Body
    Log Json  ${result}
    ${result}=   Parse Json  ${result}
    Log  ${result}
    [Return]  ${result}

Get VFS list
    ${url}  Set Variable  /configuration/1.3/VirtualFSList
    ${result}  Get From REST endpoint  ${url}
    [Return]  ${result}

Get SA status info  [Arguments]  ${SA}
    ${url}  Set Variable  /info/status/${SA}
    ${result}  Get From REST endpoint  ${url}
    [Return]  ${result}

Get SA status info parameter  [Arguments]  ${SA_TOKEN}  ${PARAM_NAME}
    ${SA_STATUS}  Get SA status info  ${SA_TOKEN}
    ${SA_STATUS}  Get From Dictionary  ${SA_STATUS}  sa-status
    ${PARAM_VALUE}  Get From Dictionary  ${SA_STATUS}  ${PARAM_NAME}
    Log  ${PARAM_VALUE}
    [Return]  ${PARAM_VALUE}

Sum  [Arguments]  ${e1}  ${e2}
    ${result}=  Evaluate  ${e1} + ${e2}
    [Return]  ${result}

Diff  [Arguments]  ${e1}  ${e2}
    ${result}=  Evaluate  ${e1} - ${e2}
    [Return]  ${result}
