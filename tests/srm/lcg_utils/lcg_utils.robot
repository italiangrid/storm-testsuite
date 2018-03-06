*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

List files in an existing directory with lcg-utils
  [Tags]  lcg-utils  ls
  [Setup]  Use default voms proxy
  ${dirname}  Get a unique name
  ${filename}  Create local file
  ${surlDir}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}
  ${surlFile}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${dirname}/${filename}
  ${output}  Perform mkdir using clientSRM  ${surlDir}
  Should Contain  ${output}  SRM_SUCCESS
  Copy-out file using lcg-utils  ${filename}  ${surlFile}
  ${output}  List files in directory using lcg_utils  ${surlDir}
  Should Contain  ${output}  ${filename}
  ${output}  Perform rmdir using clientSRM  ${surlDir}  -r
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Check if a lcg-ls on an existent surl works
  [Tags]  lcg-utils  ls
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using lcg-utils  ${filename}  ${surl}
  Check file exists using lcg-utils  ${surl}
  ${output}  Perform rm using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Check if a lcg-ls on a non-existent surl fails
  [Tags]  lcg-utils  ls
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Check file does not exists using lcg-utils  ${surl}
  [Teardown]  Clear all credentials

Check lcg-cp computed checksum in case it starts with zero
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/108. Given a file with ADLER32 checksum that starts with '0' and a SURL pointing to a non existent file in an existent folder, verify that after transfering the file on the SURL the checksum value computed for the file matches as string with the one of the local file.
  [Tags]  lcg-utils  regression  cp
  [Setup]  Use default voms proxy
  ${srcFileName}  Create local file with checksum that starts with zero
  ${destFileName}  Get a unique name
  ${srcSurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${srcFileName}
  ${destSurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${destFileName}
  Copy-out file using lcg-utils  ${srcFileName}  ${srcSurl}
  ${output}  Detailed ls using clientSRM  ${srcSurl}
  ${result}  ${b_checksum}=  Should Match Regexp  ${output}  checkSumValue=(\".+\")
  Log  ${b_checksum}
  Copy file using lcg-utils  ${srcSurl}  ${destSurl}
  ${output}  Detailed ls using clientSRM  ${destSurl}
  ${result}  ${a_checksum}=  Should Match Regexp  ${output}  checkSumValue=(\".+\")
  Log  ${a_checksum}
  Should be equal  ${b_checksum}  ${a_checksum}
  [Teardown]  Clear all credentials

Test lcg-cp out
  [Tags]  lcg-utils  cp
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using lcg-utils  ${filename}  ${surl}
  [Teardown]  Clear all credentials

Copy out a file using lcg-utils
  [Tags]  lcg-utils
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Check file does not exists using lcg-utils  ${surl}
  Copy-out file using lcg-utils  ${filename}  ${surl}
  Copy-in file using lcg-utils  ${surl}  ${filename}_copied
  Execute and check success  diff /tmp/${TESTDIR}/${filename} /tmp/${TESTDIR}/${filename}_copied
  [Teardown]  Clear all credentials