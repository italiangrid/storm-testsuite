*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Ping using the dCache client
  [Tags]  ping  dcache-client
  [Setup]  Use default voms proxy
  ${output}  Ping using dCache client
  Should Contain  ${output}  StoRM
  [Teardown]  Clear all credentials

Create directory using the dCache client
  [Tags]  dcache-client  rmdir
  [Setup]  Use default voms proxy
  ${dirName}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirName}
  Create directory using dCache client  ${surl}
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Create a directory that already exists using the dCache client
  [Tags]  dcache-client  mkdir
  [Setup]  Use default voms proxy
  ${dirName}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirName}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  ${output}  Try to create directory using dCache client  ${surl}
  Should Contain  ${output}  SRM_DUPLICATION_ERROR
  Should Contain  ${output}  Directory specified exists!
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Remove a non existent directory using the dCache client
  [Tags]  dcache-client  rmdir
  [Setup]  Use default voms proxy
  ${dirName}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirName}
  ${output}  Try to remove directory using dCache client  ${surl}
  Should Contain  ${output}  SRM_INVALID_PATH
  Should Contain  ${output}  Directory does not exists
  [Teardown]  Clear all credentials

Remove a non existent file using the dCache client
  [Tags]  dcache-client  rm
  [Setup]  Use default voms proxy
  ${fileName}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${fileName}
  ${output}  Try to remove file using dCache client  ${surl}
  Should Contain  ${output}  SRM_INVALID_PATH
  Should Contain  ${output}  File does not exist
  [Teardown]  Clear all credentials

Remove an existent file using dCache client
  [Tags]  dcache-client  rm
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Check file does not exists using lcg-utils  ${surl}
  Copy-out file using lcg-utils  ${filename}  ${surl}
  Check file exists using lcg-utils  ${surl}
  Remove file using dCache client  ${surl}
  Remove local file  ${fileName}
  [Teardown]  Clear all credentials

Check a file is correctly transferred out, re-transferred in and deleted with dcache client
  [Tags]  lcg-utils  dcache-client
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using lcg-utils  ${filename}  ${surl}
  Copy-in file using lcg-utils  ${surl}  ${filename}
  Remove file using dCache client  ${surl}
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Check file copy in/out using lcg-utils, use dcache-client to create/remove dir and file
  [Tags]  lcg-utils  dcache-client
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${dirName}  Get a unique name
  ${surlDir}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirName}
  ${surlFile}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirName}/${filename}
  ${output}  List files in directory using lcg_utils  ${surlDir}
  Should Contain  ${output}  No such file or directory
  Create directory using dCache client  ${surlDir}
  ${output}  Try to create directory using dCache client  ${surlDir}
  Should Contain  ${output}  SRM_DUPLICATION_ERROR
  ${output}  List files in directory using lcg_utils  ${surlDir}
  Should Not Contain  ${output}  SRM_INVALID_PATH
  Copy-out file using lcg-utils  ${filename}  ${surlFile}
  ${output}  List files in directory using lcg_utils  ${surlDir}
  Should Not Contain  ${output}  SRM_INVALID_PATH
  Copy-in file using lcg-utils  ${surlFile}  ${filename}
  Remove file using dCache client  ${surlFile}
  ${output}  Try to remove file using dCache client  ${surlFile}
  Should Contain  ${output}  SRM_FAILURE
  Remove directory using dCache client  ${surlDir}
  ${output}  Try to remove directory using dCache client  ${surlDir}
  Should Contain  ${output}  SRM_INVALID_PATH
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Check a file is correctly transferred out, the calculate checksum is correct and delete with dcache client
  [Tags]  lcg-utils  dcache-client
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  List files in directory using lcg_utils  ${surl}
  Should Contain  ${output}  SRM_INVALID_PATH
  Copy-out file using lcg-utils  ${filename}  ${surl}
  ${output}  List files in directory using lcg_utils  ${surl}
  Should Contain  ${output}  ADLER32
  Remove file using dCache client  ${surl}
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Check the correct backend behaviour when a user specifies a DB PWD in the def file
  [Tags]  lcg-utils  dcache-client
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/227
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  List files in directory using lcg_utils  ${surl}
  Should Contain  ${output}  SRM_INVALID_PATH
  Copy-out file using lcg-utils  ${filename}  ${surl}
  Remove file using dCache client  ${surl}
  Remove local file  ${filename}
  [Teardown]  Clear all credentials