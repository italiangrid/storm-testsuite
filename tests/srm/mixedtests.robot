*** Settings ***

Resource   lib/import.robot

*** Keywords ***

Is SRM_SPACE_AVAILABLE  [Arguments]  ${surl}  ${token}
  ${output}  Perform sptp using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SPACE_AVAILABLE

Is SRM_FILE_PINNED  [Arguments]  ${surl}  ${token}
  ${output}  Perform sptg using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_FILE_PINNED

Create remote directory  [Arguments]  ${surl}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS

Create file with synch ptp and pd  [Arguments]  ${surl}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS

Upload file with gfal utils  [Arguments]  ${localfilename}  ${surl}
  Copy-out file using gfal-utils  ${localfilename}  ${surl}

Upload file with asynch ptp and globus file transfer  [Arguments]  ${surl}  ${localfilename}  ${turl}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}
  Should Contain  ${output}  SRM_REQUEST_QUEUED
  Wait Until Keyword Succeeds  1 min  2 sec  Is SRM_SPACE_AVAILABLE  ${surl}  ${token}
  Copy-out file using globus-utils  ${localfilename}  ${turl}
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS

Get file with synch ptg and globus file transfer  [Arguments]  ${surl}  ${turl}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_FILE_PINNED
  ${localfilename}  Get a unique name
  Copy-in file using globus-utils  ${turl}  ${localfilename}
  ${output}  Perform rf using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS

Get file with asynch ptg and globus file transfer  [Arguments]  ${surl}  ${turl}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}
  Should Contain  ${output}  SRM_REQUEST_QUEUED
  Wait Until Keyword Succeeds  1 min  2 sec  Is SRM_FILE_PINNED  ${surl}  ${token}
  ${localfilename}  Get a unique name
  Copy-in file using globus-utils  ${turl}  ${localfilename}
  ${output}  Perform rf using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS

Do a synch ptg on file  [Arguments]  ${surl}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_FILE_PINNED
  [Return]  ${token}

Abort request  [Arguments]  ${token}
  ${output}  Perform abort request using clientSRM  ${token}
  Should Contain  ${output}  SRM_SUCCESS

Release file  [Arguments]  ${surl}  ${token}
  ${output}  Perform rf using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS

Copy file  [Arguments]  ${srcsurl}  ${destsurl}
  Copy file using gfal-utils  ${srcSurl}  ${destSurl}

Move file  [Arguments]  ${srcsurl}  ${destsurl}
  ${output}  Perform mv using clientSRM  ${srcsurl}  ${destsurl}
  Should Contain  ${output}  SRM_SUCCESS

List Directory  [Arguments]  ${surl}
  ${output}  Perform ls using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Return]  ${output}

Remove file  [Arguments]  ${surl}
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS

Mixed tests  [Arguments]  ${storageArea}  ${storageAreaRealRoot}
  ${dirname}  Get a unique name
  ${filename}  Create local file
  ${surlDir}  Build surl  ${storageArea}  ${TESTDIR}/${dirname}
  ${surlFile1}  Build surl  ${storageArea}  ${TESTDIR}/${dirname}/${filename}_1
  ${surlFile2}  Build surl  ${storageArea}  ${TESTDIR}/${dirname}/${filename}_2
  ${surlFile3}  Build surl  ${storageArea}  ${TESTDIR}/${dirname}/${filename}_3
  ${surlFile4}  Build surl  ${storageArea}  ${TESTDIR}/${dirname}/${filename}_4
  ${surlFile5}  Build surl  ${storageArea}  ${TESTDIR}/${dirname}/${filename}_5
  ${turlFile3}  Build gsiftp TURL  ${storageAreaRealRoot}  ${TESTDIR}/${dirname}/${filename}_3
  Create remote directory  ${surlDir}
  Create file with synch ptp and pd  ${surlFile1}
  Upload file with gfal utils  ${filename}  ${surlFile2}
  Upload file with asynch ptp and globus file transfer  ${surlFile3}  ${filename}  ${turlFile3}
  Get file with synch ptg and globus file transfer  ${surlFile3}  ${turlFile3}
  Get file with asynch ptg and globus file transfer  ${surlFile3}  ${turlFile3}
  ${token1}  Do a synch ptg on file  ${surlFile1}
  ${token2}  Do a synch ptg on file  ${surlFile2} ${surlFile3}
  Abort request  ${token1}
  Release file  ${surlFile2} ${surlFile3}  ${token2}
  Copy file  ${surlFile3}  ${surlFile4}
  Move file  ${surlFile4}  ${surlFile5}
  ${output}  List Directory  ${surlDir}
  Should Contain  ${output}  /${storageArea}/${TESTDIR}/${dirname}/${filename}_1
  Should Contain  ${output}  /${storageArea}/${TESTDIR}/${dirname}/${filename}_2
  Should Contain  ${output}  /${storageArea}/${TESTDIR}/${dirname}/${filename}_3
  Should Contain  ${output}  /${storageArea}/${TESTDIR}/${dirname}/${filename}_5
  Remove File  ${surlFile5}
  Remove File  ${surlFile3} ${surlFile2}
  ${output}  Perform rmdir using clientSRM  ${surlDir}
  Should Not Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${surlDir}  -r
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}

*** Test Cases ***

Mixed tests on DEFAULT SA
  [Setup]  Use default voms proxy
  Mixed tests  ${DEFAULT_SA}  ${DEFAULT_SA}
  [Teardown]  Clear all credentials

Mixed tests on igi SA
  [Setup]  Use default voms proxy
  Mixed tests  ${SA.7}  ${SA.7}
  [Teardown]  Clear all credentials

Mixed tests on noauth SA
  [Setup]  Use default voms proxy
  Mixed tests  ${SA.9}  ${SA.9}
  [Teardown]  Clear all credentials

Mixed tests on NESTED SA
  [Setup]  Use voms proxy  ${DEFAULT_USER}  ${VO.2}
  Mixed tests  ${SA.4}  nested
  [Teardown]  Clear all credentials

Mixed tests on ALIASED SA
  [Setup]  Use voms proxy  ${DEFAULT_USER}  ${VO.2}
  Mixed tests  ${SA.5}  nested
  [Teardown]  Clear all credentials
