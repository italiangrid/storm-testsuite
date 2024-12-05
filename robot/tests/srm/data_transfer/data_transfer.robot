*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Test that the SRM service is able to transfer a file on the SRM endpoint
  [Tags]  storm-client  gfal
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using gfal-utils  ${filename}  ${surl}
  ${output}  Perform ls using clientSRM  ${surl}
  Should Contain  ${output}  SRM_SUCCESS
  Run gfal-rm on  ${surl}
  [Teardown]  Clear all credentials

Test that the SRM service is able to transfer a file from the SRM endpoint
  [Tags]  storm-client  ptg  gfal
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using gfal-utils  ${filename}  ${surl}
  Copy-in file using gfal-utils  ${surl}  ${filename}_copy
  Run gfal-rm on  ${surl}
  [Teardown]  Clear all credentials

Check checksum of copied file
  [Tags]  checksum  gfal
  [Documentation]  StoRM BE must be configured with GRIDFTP_WITH_DSI="yes" to pass this test
  [Setup]  Use default voms proxy
  ${filename}  Create local file
  ${srcsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using gfal-utils  ${filename}  ${srcsurl}
  ${destsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}_copied
  ${output}  Copy file using gfal-utils  ${srcsurl}  ${destsurl}
  ${checksum1}  Get checksum of remote file using gfal-utils  ${srcsurl}
  ${checksum2}  Get checksum of remote file using gfal-utils  ${destsurl}
  Log  ${checksum1}
  Log  ${checksum2}
  Should Be Equal As Strings  ${checksum1}  ${checksum2}
  Run gfal-rm on  ${srcsurl}
  Run gfal-rm on  ${destsurl}
  [Teardown]  Clear all credentials
