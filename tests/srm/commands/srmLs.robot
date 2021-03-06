*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

List files in storage area root
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${surl}  Build surl  ${DEFAULT_SA}  ${EMPTY}
  ${output}  Perform ls using clientSRM  ${surl}  -c 1
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

List existent directory
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surlDir}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform ls using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${dirname}"
  Should Contain  ${output}  size=0
  ${fileName}  Get a unique name
  ${surlFile}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${fileName}
  Put without really putting using clientSRM  ${surlFile}
  ${output}  Perform ls using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${dirname}"
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${dirname}/${filename}"
  Should Contain  ${output}  size=1
  ${output}  Perform rmdir using clientSRM  ${surlDir}  -r
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

List unexistent directory
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform ls using clientSRM  ${surl}
  Should Contain  ${output}  SRM_FAILURE
  Should Contain  ${output}  SRM_INVALID_PATH
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${dirname}"
  Should Not Contain  ${output}  size=0
  [Teardown]  Clear all credentials

List existent file
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using gfal-utils  ${filename}  ${surl}
  ${output}  Perform ls using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${filename}"
  log  ${output}
  Should Contain  ${output}  size=1048576
  Should Not Contain  ${output}  size=0
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

List unexistent file
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  Perform ls using clientSRM  ${surl}
  Should Contain  ${output}  SRM_FAILURE
  Should Contain  ${output}  SRM_INVALID_PATH
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${filename}"
  Should Not Contain  ${output}  size=0
  [Teardown]  Clear all credentials

Full detailed list of existent directory
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform ls using clientSRM  ${surl}  -l 1 -n 1
  Should Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${dirname}"
  Should Contain  ${output}  size=0
  Should Contain  ${output}  ownerPermission
  Should Contain  ${output}  groupPermission
  Should Contain  ${output}  type=Directory
  Should Contain  ${output}  lastModificationTime
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Full detailed list of existent file
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using gfal-utils  ${filename}  ${surl}
  ${output}  Perform ls using clientSRM  ${surl}  -l 1 -n 0
  Should Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${filename}"
  Should Contain  ${output}  size
  Should Not Contain  ${output}  size=0
  Should Contain  ${output}  ownerPermission
  Should Contain  ${output}  groupPermission
  Should Contain  ${output}  type=File
  Should Contain  ${output}  lastModificationTime
  Should Contain  ${output}  lifetimeAssigned
  Should Contain  ${output}  lifetimeLeft
  Should Contain  ${output}  fileLocality
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Full detailed and recursive list of existent files and directories
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${dirname}  Get a unique name
  ${dirsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${filesurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${filename}
  ${subdirsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${dirname}
  ${subdirfilesurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${dirname}/${filename}
  ${output}  Perform mkdir using clientSRM  ${dirsurl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform mkdir using clientSRM  ${subdirsurl}
  Should Contain  ${output}  SRM_SUCCESS
  Copy-out file using gfal-utils  ${filename}  ${filesurl}
  Copy-out file using gfal-utils  ${filename}  ${subdirfilesurl}
  ${output}  Perform ls using clientSRM  ${dirsurl}  -r -l 1
  Should Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${dirname}"
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${dirname}/${filename}"
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${dirname}/${dirname}"
  Should Contain  ${output}  path="/${DEFAULT_SA}/${TESTDIR}/${dirname}/${dirname}/${filename}"
  Should Contain  ${output}  size
  Should Contain  ${output}  ownerPermission
  Should Contain  ${output}  groupPermission
  Should Contain  ${output}  type=File
  Should Contain  ${output}  lastModificationTime
  Should Contain  ${output}  lifetimeAssigned
  Should Contain  ${output}  lifetimeLeft
  Should Contain  ${output}  fileLocality
  ${output}  Perform rmdir using clientSRM  ${dirsurl}  -r
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Ls on a surl that points to another storage area
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${qsurl}  Build surl  ${VO.2}  ../${DEFAULT_SA}
  ${ssurl}  Build simple surl  ${VO.2}  ../${DEFAULT_SA}
  ${output}  Perform ls using clientSRM  ${qsurl}
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  ${output}  Perform ls using clientSRM  ${ssurl}
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  [Teardown]  Clear all credentials

Ls on a surl with a valid dots segment
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${dirname2}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${surl2}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname2}
  ${surl3}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/../${dirname2}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform mkdir using clientSRM  ${surl2}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform ls using clientSRM  ${surl3}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${surl2}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Ls on a surl with a valid dots segment with simple surls
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${dirname2}  Get a unique name
  ${surl}  Build simple surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${surl2}  Build simple surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname2}
  ${surl3}  Build simple surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/../${dirname2}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform mkdir using clientSRM  ${surl2}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform ls using clientSRM  ${surl3}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Perform rmdir using clientSRM  ${surl2}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Ls on a surl that points to a reserved area
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${surl}  Build surl  ${DEFAULT_SA}  ../../etc/grid-security
  ${output}  Perform ls using clientSRM  ${surl}
  Should Not Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  SRM_INTERNAL_ERROR
  ${surl}  Build simple surl  ${DEFAULT_SA}  ../../etc/grid-security
  ${output}  Perform ls using clientSRM  ${surl}
  Should Not Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  SRM_INTERNAL_ERROR
  [Teardown]  Clear all credentials

Ls on some symlinks that point to other storage-areas
  [Tags]  storm-client  ls  symlink  STOR-898
  [Setup]  Use default voms proxy
  ${symlinkSURL}  Build surl  ${DEFAULT_SA}  ${SYMLINK.1}
  ${output}  Perform ls using clientSRM  ${symlinkSURL}
  Should Contain  ${output}  SRM_FAILURE
  Should Contain  ${output}  SRM_AUTHORIZATION_FAILURE
  Should Not Contain  ${output}  SRM_SUCCESS
  Log  ${output}
  [Teardown]  Clear all credentials

Check approached VFS with nested accesspoints
  [Tags]  ls  nested  storm-client
  [Setup]  Use voms proxy  ${defaultUser}  ${NESTED_SA_VONAME}
  ${dirname}  Get a unique name
  ${filename}  Create local file
  ${surlDir}  Build surl  ${NESTED_SA}  ${TESTDIR}/${dirname}
  ${surlFile}  Build surl  ${NESTED_SA}  ${TESTDIR}/${dirname}/${filename}
  ${output}  Perform mkdir using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_SUCCESS
  Copy-out file using gfal-utils  ${filename}  ${surlFile}
  ${output}  Perform ls using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  ${NESTED_SA}/${TESTDIR}/${dirname}
  Should Contain  ${output}  ${NESTED_SA}/${TESTDIR}/${dirname}/${filename}
  [Teardown]  Clear all credentials

Check approached VFS with aliased accesspoint
  [Tags]  ls  aliased  storm-client
  [Setup]  Use voms proxy  ${defaultUser}  ${NESTED_SA_VONAME}
  ${dirname}  Get a unique name
  ${filename}  Create local file
  ${surlDir}  Build surl  ${ALIASED_SA}  ${TESTDIR}/${dirname}
  ${surlFile}  Build surl  ${ALIASED_SA}  ${TESTDIR}/${dirname}/${filename}
  ${output}  Perform mkdir using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_SUCCESS
  Put without really putting using clientSRM  ${surlFile}
  ${output}  Perform ls using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_SUCCESS
  Should Contain  ${output}  ${ALIASED_SA}/${TESTDIR}/${dirname}
  Should Contain  ${output}  ${ALIASED_SA}/${TESTDIR}/${dirname}/${filename}
  [Teardown]  Clear all credentials
