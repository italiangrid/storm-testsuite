*** Keywords ***

##### TEST SETUP AND TEARDOWN

Setup default SA
  Use default voms proxy
  ${options}  Get CURL default VOMS proxy options
  ${dirname}  Get a unique name
  ${filename}  Create local file with text  test123456789
  ${localfilepath}  Get local file path from name  ${filename}
  Set Test Variable  ${TEST_CURL_OPTIONS}  ${options}
  Set Test Variable  ${TEST_REMOTE_DIRNAME}  ${dirname}
  Set Test Variable  ${TEST_FILENAME}  ${filename}
  Set Test Variable  ${TEST_LOCAL_FILEPATH}  ${localfilepath}
  Set Test Variable  ${TEST_SA}  ${DEFAULT_SA}
  Set Test Variable  ${TEST_ENDPOINT}  ${DAVSecureEndpoint}

Teardown default SA
  Clear all credentials

Setup SA and VO  [Arguments]  ${endpoint}  ${sa}  ${user}  ${voname}
  Use voms proxy  ${user}  ${voname}
  ${options}  Get CURL VOMS proxy options  ${user}  ${voname}
  ${dirname}  Get a unique name
  ${filename}  Create local file with text
  ${localfilepath}  Get local file path from name  ${filename}
  Set Test Variable  ${TEST_CURL_OPTIONS}  ${options}
  Set Test Variable  ${TEST_REMOTE_DIRNAME}  ${dirname} 
  Set Test Variable  ${TEST_FILENAME}  ${filename}
  Set Test Variable  ${TEST_LOCAL_FILEPATH}  ${localfilepath}
  Set Test Variable  ${TEST_SA}  ${sa}
  Set Test Variable  ${TEST_ENDPOINT}  ${endpoint}

Teardown SA and VO
  Clear all credentials

Setup SA  [Arguments]  ${endpoint}  ${sa}
  Clear all credentials
  ${dirname}  Get a unique name
  ${filename}  Create local file with text
  ${localfilepath}  Get local file path from name  ${filename}
  Set Test Variable  ${TEST_CURL_OPTIONS}  ${EMPTY}
  Set Test Variable  ${TEST_REMOTE_DIRNAME}  ${dirname} 
  Set Test Variable  ${TEST_FILENAME}  ${filename}
  Set Test Variable  ${TEST_LOCAL_FILEPATH}  ${localfilepath}
  Set Test Variable  ${TEST_SA}  ${sa}
  Set Test Variable  ${TEST_ENDPOINT}  ${endpoint}

Teardown SA
  Clear all credentials

### TEST INITIALIZATION

Create empty working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}
  Do CURL MKCOL and check success  ${url}  ${TEST_CURL_OPTIONS}

Create working directory
  Create empty working directory
  ${url}  Build URL  ${TEST_ENDPOINT}  ${TEST_SA}  ${TEST_REMOTE_DIRNAME}/${TEST_FILENAME}
  Do CURL PUT and check success  ${url}  ${TEST_LOCAL_FILEPATH}  ${TEST_CURL_OPTIONS}

##### TEST UTILS

Upload file with CURL  [Arguments]  ${urlDir}  ${credentials}=${EMPTY}
  ${filename}  Create local file with text
  ${path}  Get local file path from name  ${filename}
  Do CURL PUT and check success  ${urlDir}/${filename}  ${path}  ${credentials}
  Do CURL HEAD and check success  ${urlDir}/${filename}  ${credentials}
  [Return]  ${filename}

##### URL BUILDING

Build URL  [Arguments]  ${endpoint}=${DAVSecureEndpoint}  ${storagearea}=${DEFAULT_SA}  ${path}=${EMPTY}
  ${output}  Run Keyword If  '${path}'=='${EMPTY}'  Set Variable  ${endpoint}/${storagearea}/${TESTDIR}  ELSE  Set variable  ${endpoint}/${storagearea}/${TESTDIR}/${path}
  [Return]  ${output}

##### PROPFIND UTILS

Get PROPFIND ALLPROP body
  ${output}  Set variable  <?xml version='1.0' encoding='utf-8'?><propfind xmlns='DAV:'><allprop/></propfind>
  [Return]  ${output}

Get PROPFIND PROPNAME body
  ${output}  Set variable  <?xml version='1.0' encoding='utf-8'?><propfind xmlns='DAV:'><propname/></propfind>
  [Return]  ${output}

Get PROPFIND PROP body  [Arguments]  ${propname}
  ${output}  Set variable  <?xml version='1.0' encoding='utf-8'?><propfind xmlns='DAV:'><prop><${propname}/><prop/></propfind>
  [Return]  ${output}
