*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Move file
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${srcsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${destsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}.moved
  Copy-out file using gfal-utils  ${filename}  ${srcsurl}
  ${output}  Perform mv using clientSRM  ${srcsurl}  ${destsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform ls using clientSRM  ${srcsurl}
  Should Not Contain  ${output}  SRM_SUCCESS
  ${output}  Perform ls using clientSRM  ${destsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rm using clientSRM  ${destsurl}
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Move file to a destination surl that already exists
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${srcsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${destsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}.moved
  Copy-out file using gfal-utils  ${filename}  ${srcsurl}
  Copy-out file using gfal-utils  ${filename}  ${destsurl}
  ${output}  Perform mv using clientSRM  ${srcsurl}  ${destsurl}
  Should Contain  ${output}  SRM_DUPLICATION_ERROR
  ${output}  Perform rm using clientSRM  ${srcsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rm using clientSRM  ${destsurl}
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Move file into directory
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${dstdirname}  Get a unique name
  ${srcfilesurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${destdirsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dstdirname}
  ${destfilesurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dstdirname}/${filename}
  Copy-out file using gfal-utils  ${filename}  ${srcfilesurl}
  ${output}  Perform mkdir using clientSRM  ${destdirsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform mv using clientSRM  ${srcfilesurl}  ${destdirsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform ls using clientSRM  ${destfilesurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${destdirsurl}  -r
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Move not empty directory on unexistent surl
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${filename}  Create local file
  ${dirsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${filesurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${filename}
  ${destdirsurl}  Build surl  ${DEFAULT_SA}  ${dirname}.moved
  ${output}  Perform mkdir using clientSRM  ${dirsurl}
  Should Contain  ${output}  SRM_SUCCESS
  Copy-out file using gfal-utils  ${filename}  ${filesurl}
  ${output}  Perform mv using clientSRM  ${dirsurl}  ${destdirsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${destdirsurl}  -r
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Move not empty directory on a existent empty directory
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${filename}  Create local file
  ${dirsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${filesurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${filename}
  ${destdirsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}.moved
  ${destfilesurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}.moved/${dirname}/${filename}
  ${output}  Perform mkdir using clientSRM  ${dirsurl}
  Should Contain  ${output}  SRM_SUCCESS  
  Copy-out file using gfal-utils  ${filename}  ${filesurl}
  ${output}  Perform mkdir using clientSRM  ${destdirsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform mv using clientSRM  ${dirsurl}  ${destdirsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform ls using clientSRM  ${destfilesurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${destdirsurl}  -r
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Move not empty directory on a existent surl
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${filename}  Create local file
  ${dirsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${filesurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${filename}
  ${destsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}.copied
  ${output}  Perform mkdir using clientSRM  ${dirsurl}
  Should Contain  ${output}  SRM_SUCCESS
  Copy-out file using gfal-utils  ${filename}  ${filesurl}
  Copy-out file using gfal-utils  ${filename}  ${destsurl}
  ${output}  Perform mv using clientSRM  ${dirsurl}  ${destsurl}
  Should Contain  ${output}  SRM_DUPLICATION_ERROR
  ${output}  Perform rmdir using clientSRM  ${dirsurl}  -r
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rm using clientSRM  ${destsurl}
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Move not empty directory on a existent not empty directory that contains an existent directory with same source name
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${filename}  Create local file
  ${dirsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${filesurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${filename}
  ${destdirsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}.moved
  ${destsubdirsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}.moved/${dirname}
  ${output}  Perform mkdir using clientSRM  ${dirsurl}
  Should Contain  ${output}  SRM_SUCCESS  
  Copy-out file using gfal-utils  ${filename}  ${filesurl}
  ${output}  Perform mkdir using clientSRM  ${destdirsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform mkdir using clientSRM  ${destsubdirsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform mv using clientSRM  ${dirsurl}  ${destdirsurl}
  Should Contain  ${output}  SRM_DUPLICATION_ERROR
  ${output}  Perform rmdir using clientSRM  ${dirsurl}  -r
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${destdirsurl}  -r
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Move file over itself
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${srcsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${destsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using gfal-utils  ${filename}  ${srcsurl}
  ${output}  Perform mv using clientSRM  ${srcsurl}  ${destsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rm using clientSRM  ${srcsurl}
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Move file with active ptg
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${srcsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${destsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}.moved
  Copy-out file using gfal-utils  ${filename}  ${srcsurl}
  ${output}  ${token}  Perform ptg using clientSRM  ${srcsurl}  -p
  Should Contain  ${output}  SRM_FILE_PINNED
  ${output}  Perform mv using clientSRM  ${srcsurl}  ${destsurl}
  Should Contain  ${output}  SRM_FILE_BUSY
  ${output}  Perform rf using clientSRM  ${srcsurl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rm using clientSRM  ${srcsurl}
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Move file with active ptp
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${srcsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${destsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}.moved
  ${output}  ${token}  Perform ptp using clientSRM  ${srcsurl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${output}  Perform mv using clientSRM  ${srcsurl}  ${destsurl}
  Should Contain  ${output}  SRM_FILE_BUSY
  ${output}  Perform pd using clientSRM  ${srcsurl}  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rm using clientSRM  ${srcsurl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Move file on an unauthorized destination
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${srcsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${destsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using gfal-utils  ${filename}  ${srcsurl}
  Use default grid proxy
  ${output}  Perform mv using clientSRM  ${srcsurl}  ${destsurl}
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  Use default voms proxy
  ${output}  Perform rm using clientSRM  ${srcsurl}
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Check unauthorized file move on a different VO
  [Tags]  storm-client  ls  STOR-898
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${srcsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${destsurl}  Build surl  ${DEFAULT_SA}  ../${SA.2}/${TESTDIR}/${filename}
  Copy-out file using gfal-utils  ${filename}  ${srcsurl}
  ${output}  Perform mv using clientSRM  ${srcsurl}  ${destsurl}
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  ${destsurl}  Build surl  ${SA.2}  ../${DEFAULT_SA}/${TESTDIR}/${filename}_2
  ${output}  Perform mv using clientSRM  ${srcsurl}  ${destsurl}
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  ${output}  Perform rm using clientSRM  ${srcsurl}
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials
