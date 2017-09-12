*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Check if StoRM publishes correctly values for used and free space on the BDII
  [Tags]  regression
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Check file does not exists using lcg-utils  ${surl}
  Copy-out file using lcg-utils  ${filename}  ${surl}
  ${saToken}  Get SA Token
  ${size_before}  Get unused size using clientSRM  ${saToken}
  Log  ${size_before}
  Check file exists using lcg-utils  ${surl}
  Perform rm using clientSRM  ${surl}
  Check file does not exists using lcg-utils  ${surl}
  ${size_after}  Get unused size using clientSRM  ${saToken}
  Log  ${size_after}
  ${diff_size}  Run  echo `expr ${size_after} - ${size_before}`
  ${file_size}  Run  ls -l /tmp/${TESTDIR}/${filename} | awk {'print $5'}
  Should be equal  ${file_size}  ${diff_size}
  [Teardown]  Clear all credentials
