*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Space token used space is update
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/109. Given a Space Token ST and a SURL that resides on ST pointing to a not existent file, verify that inspecting the unused space of the ST before and after a non-empty file has been stored on the SURL, the ST used space value is updated accordingly to the size of the new file.
  [Tags]  storm-client  gfal-utils  gst  regression
  [Setup]  Use default voms proxy
  ${token}  Get SA Token
  Log  ${token}
  ${size_before}  Get unused size using clientSRM  ${token}
  Log  ${size_before}
  ${filename}  Create local file
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  Copy-out file using gfal-utils  ${filename}  ${surl}
  ${size_after}  Get unused size using clientSRM  ${token}
  Log  ${size_after}
  ${diff_size}  Run  echo `expr ${size_before} - ${size_after}`
  ${file_size}  Run  ls -l /tmp/${TESTDIR}/${filename} | awk {'print $5'}
  Should be equal  ${file_size}  ${diff_size}
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Check a srmGetSpaceMetadata call succedes when a valid Space Token not associated to a Storage Area is given
  [Tags]  storm-client  gsm  regression
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/277 Storm failed with "SRM_INTERNAL_ERROR" and "Storage Space not initialized yet" as explaination. It must succede since it does not needs to be initialized.
  [Setup]  Use default voms proxy
  ${token}  Reserve space using clientSRM
  ${output}  Get space metadata using clientSRM  ${token}
  Should Contain  ${output}  SRM_SUCCESS  
  ${output}  Release space using clientSRM  ${token}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials

Check a GetSpaceMetadata succedes when using a proxy without voms extensions
  [Tags]  storm-client  gsm  regression
  [Documentation]  Regression test for https://storm.cnaf.infn.it:8443/redmine/issues/189
  [Setup]  Use default voms proxy
  ${token}  Get SA Token
  Log  ${token}
  ${spacetoken}  Get space token using clientSRM  ${token}
  ${output}  Get space metadata using clientSRM  ${spacetoken}
  Should Contain  ${output}  SRM_SUCCESS
  [Teardown]  Clear all credentials
