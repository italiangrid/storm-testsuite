*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Check a get space metadata request fails when a wrong token format is provided
  [Tags]  regression  gsm
  [Setup]  Use default voms proxy
  ${output}  Get space metadata using clientSRM  "ciccio' OR SLEEP(1)-- "
  Log  ${output}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials

Check a get request summary fails when a wrong token format is provided
  [Tags]  regression  grs
  [Setup]  Use default voms proxy
  ${output}  Get request summary using clientSRM  "ciccio' OR 1=1) AND SLEEP(1)-- "
  Log  ${output}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials

Check a reserve space request fails when a wrong token format is provided
  [Tags]  regression  rsp
  [Setup]  Use default voms proxy
  ${output}  Reserve space using clientSRM with token  "ciccio' or SLEEP(1)-- "
  Log  ${output}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials

Check a release space request fails when a wrong token format is provided
  [Tags]  regression  rs
  [Setup]  Use default voms proxy
  ${output}  Release space using clientSRM  "ciccio' or SLEEP(1)-- "
  Log  ${output}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials

Check a get space tokens request fails when a wrong token format is provided
  [Tags]  regression  gst
  [Setup]  Use default voms proxy
  ${output}  Get space token output using clientSRM  "ciccio' OR SLEEP(1)-- "
  Log  ${output}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials

Check a get request tokens fails with an invalid user request description
  [Tags]  regression  grt
  [Setup]  Use default voms proxy
  ${output}  Get request tokens using clientSRM  "ciccio' OR SLEEP(1)-- "
  Log  ${output}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid user request description
  [Teardown]  Clear all credentials

Check a ptp fails when a malformed surl is supplied
  [Tags]  storm-client  ptp  regression
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  "${TESTDIR}/${filename} ciccio') OR SLEEP(1)-- "
  ${output}  Execute clientSRM Command on Surl  ptp  ${surl}  ${EMPTY}
  Log  ${output}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid surl
  [Teardown]  Clear all credentials

Check a sptp fails when a malformed token is supplied
  [Tags]  storm-client  sptp  regression
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/{filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}
  ${output}  Perform sptp using clientSRM  ${surl}  "ciccio' OR SLEEP(1)-- "
  Log  ${output}  
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials

Check a ptg fails when a malformed surl is supplied
  [Tags]  storm-client  ptg  regression
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  ${surl}  Build surl  ${DEFAULT_SA}  "${TESTDIR}/${filename} ciccio') OR SLEEP(1)-- "
  ${output}  Execute clientSRM Command on Surl  ptg  ${surl}  ${EMPTY}
  Log  ${output}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid surl
  Remove local file  ${filename}
  [Teardown]  Clear all credentials

Check a sptg fails when a malformed token is supplied
  [Tags]  storm-client  sptg  regression
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  ${output}  ${token}  Perform ptg using clientSRM  ${surl}
  ${output}  Perform sptg using clientSRM  ${surl}  "ciccio' OR SLEEP(1)-- "
  Log  ${output}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials

Check a pd fails when a malformed token is supplied
  [Tags]  storm-client  pd
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${output}  Perform pd using clientSRM  ${surl}  "ciccio' OR SLEEP(1)-- "
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials

Check a pd fails when a malformed surl is supplied
  [Tags]  storm-client  pd
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${surl}  Build surl  ${DEFAULT_SA}  "${filename} ciccio') OR SLEEP(1)-- "
  ${output}  Perform pd using clientSRM  ${surl}  ${token}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid surl
  [Teardown]  Clear all credentials

Check an abort request fails when a malformed token is supplied
  [Tags]  storm-client  abort  
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name  
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl} -p
  ${output}  Perform abort request using clientSRM  "${token}' or SLEEP(1)-- "
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials

Check an abort file fails when a malformed token is supplied
  [Tags]  storm-client  abort
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl} -p
  ${output}  Perform abort file using clientSRM  ${surl}  "${token}' or SLEEP(1)-- "
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials

Check an ls request fails when a malformed surl is supplied
  [Tags]  storm-client  ls
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  "${TESTDIR}/${filename} ciccio') OR SLEEP(1)-- "
  ${output}  Perform ls using clientSRM  ${surl}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid surl
  [Teardown]  Clear all credentials

Check a mkdir request fails when a malformed surl is supplied
  [Tags]  storm-client  mkdir
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  "${TESTDIR}/${filename} ciccio') OR SLEEP(1)-- "
  ${output}  Perform mkdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid surl
  [Teardown]  Clear all credentials

Check a rmdir request fails when a malformed surl is supplied
  [Tags]  storm-client  rmdir
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  Perform mkdir using clientSRM  ${surl}
  ${surl}  Build surl  ${DEFAULT_SA}  "${TESTDIR}/${filename} ciccio') OR SLEEP(1)-- "
  ${output}  Perform rmdir using clientSRM  ${surl}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid surl
  [Teardown]  Clear all credentials

Check a rf request fails when a malformed token is supplied
  [Tags]  storm-client  mkdir
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl} -p
  ${output}  Perform pd using clientSRM  ${surl}  ${token}  -p
  ${output}  ${token}  Perform ptg using clientSRM  ${surl} -p
  ${output}  Perform rf using clientSRM  ${surl}  "${token}' and sleep(1)-- "
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials 

Check a rm request fails when a malformed surl is supplied
  [Tags]  storm-client  rm
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${surl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl} -p
  ${output}  Perform pd using clientSRM  ${surl}  ${token}  -p
  ${surl}  Build surl  ${DEFAULT_SA}  "${TESTDIR}/${filename} ciccio' or sleep(1)-- "  
  ${output}  Perform rm using clientSRM  ${surl}
  Log  ${output}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid surl
  [Teardown]  Clear all credentials

Check a mv request fails when a malformed surl is supplied  
  [Tags]  storm-client  mv
  [Setup]  Use default voms proxy
  ${filename}  Get a unique name
  ${srcsurl}  Build surl  ${DEFAULT_SA}  ${TESTDIR}/${filename}
  ${output}  ${token}  Perform ptp using clientSRM  ${srcsurl} -p
  ${output}  Perform pd using clientSRM  ${srcsurl}  ${token}  -p
  ${destsurl}  Build surl  ${DEFAULT_SA}  "${TESTDIR}/${filename}' or sleep(1)-- "
  ${output}  Perform mv using clientSRM  ${srcsurl}  ${destsurl}  -p
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid surl
  [Teardown]  Clear all credentials

Check a malformed token format does not work when pushed to the FE
  [Tags]  storm-client  regression
  [Setup]  Use default voms proxy
  ${output}  Get request summary using clientSRM  "ciccio' OR 1=1) AND SLEEP(1) "
  Log  ${output}
  Should Contain  ${output}  SRM_INVALID_REQUEST
  Should Contain  ${output}  invalid token
  [Teardown]  Clear all credentials

Check failure when getting the number of recall requests in progress using wrong input
  [Tags]  regression  recall
  [Setup]  Clear all credentials
  ${output}  Get recall requests in progress  "1%20or%201=1-- "
  Log  ${output}
  Should Not Contain  ${output}  200 OK
  Should Contain  ${output}  404 Not Found

Check failure when getting and update recall requests ready for being taken over using wrong input
  [Tags]  regression  recall
  [Setup]  Clear all credentials
  ${output}  Get and update to progress recall tasks ready for being taken over  "1%20or%201=1-- "
  Log  ${output}
  Should Not Contain  ${output}  200 OK
  Should Contain  ${output}  500 Request failed

Check failure when updating a recall task using the group task with wrong input
  [Tags]  regression  recall
  [Setup]  Clear all credentials
  ${output}  Update a recall task status using a groupTaskId  "ciccio or 1=1-- "  "1%20or%201=1-- "
  Should Not Contain  ${output}  200 OK
  Should Contain  ${output}  400 Bad Request
