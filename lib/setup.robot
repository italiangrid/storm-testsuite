*** Keywords ***

Get timestamp
  ${output}  Run  date +"%k%M%S%d%m%Y"
  [Return]  ${output}

Get uid
  ${output}  Run  id -u
  [Return]  ${output}

Set Variable If It Does Not Exist  [Arguments]  ${name}  ${value}
  ${status}  ${message} =  Run Keyword And Ignore Error  Variable Should Exist  ${name}
  Run Keyword If  "${status}" == "FAIL"  Set Global Variable  ${name}  ${value}

Set credentials for  [Arguments]  ${user}  ${voname}
  ${proxypath}  Get user voms proxy path  ${user}  ${voname}
  File Should Exist   ${proxypath}
  Set Environment Variable  X509_USER_PROXY  ${proxypath}
  
Create directory  [Arguments]  ${path}
  ${output}  ${stderr}  Execute and Check Success   mkdir ${path}
  Log  ${output}
  Log  ${stderr}

Remove directory  [Arguments]  ${path}
  ${output}  ${stderr}  Execute and Check Success   rm -rf ${path}
  Log  ${output}
  Log  ${stderr}

Add user  [Arguments]  ${user}
  ${certPath}  Get user x509 p12 path  ${user}
  Execute and Check Success   cp ${certsDir}/${user}.p12 ${certPath}
  Execute and Check Success   chmod 600 ${certPath}
  ${certPath}  Get user x509 cert path  ${user}
  Execute and Check Success   cp ${certsDir}/${user}.cert.pem ${certPath}
  Execute and Check Success   chmod 600 ${certPath}
  ${keyPath}  Get user x509 key path  ${user}
  Execute and Check Success   cp ${certsDir}/${user}.key.pem ${keyPath}
  Execute and Check Success   chmod 400 ${keyPath}

Create voms proxy   [Arguments]   ${user}  ${pass}  ${vo}
  ${usercert}  Get user x509 p12 path  ${user}
  ${userpass}  Set Variable  ${pass}
  ${proxy}  Get user voms proxy path  ${user}  ${vo}
  ${output}  ${stderr}  Execute and Check Success   echo ${userpass}|voms-proxy-init -pwstdin --voms ${vo} --cert ${usercert} --out ${proxy}
  Log  ${output}
  Log  ${stderr}

Create grid proxy   [Arguments]   ${user}  ${pass}
  ${usercert}  Get user x509 p12 path  ${user}
  ${userpass}  Set Variable  ${pass}
  ${proxy}  Get user grid proxy path  ${user}
  ${output}  ${stderr}  Execute and Check Success   echo ${userpass}|voms-proxy-init -pwstdin --cert ${usercert} --out ${proxy}
  Log  ${output}
  Log  ${stderr}
  
Use default voms proxy
  ${proxy}  Get user voms proxy path  ${DEFAULT_USER}  ${DEFAULT_VO}
  Set Environment Variable  X509_USER_PROXY  ${proxy}

Use voms proxy  [Arguments]  ${user}  ${voname}
  ${proxy}  Get user voms proxy path  ${user}  ${voname}
  Set Environment Variable  X509_USER_PROXY  ${proxy}

Use default grid proxy
  ${proxy}  Get user grid proxy path  ${DEFAULT_USER}
  Set Environment Variable  X509_USER_PROXY  ${proxy}

Use grid proxy  [Arguments]  ${user}
  ${proxy}  Get user grid proxy path  ${user}
  Set Environment Variable  X509_USER_PROXY  ${proxy}

Clear all credentials
  Set Environment Variable  X509_USER_PROXY  ${DEFAULT_X509_USER_PROXY}

Create remote working directory  [Arguments]  ${storageArea}
  ${surl}  Build surl  ${storageArea}  ${TESTDIR}
  ${output}  Perform mkdir using clientSRM  ${surl}
  Log  ${output}
  Should Contain  ${output}  SRM_SUCCESS

Clear remote working directory  [Arguments]  ${storageArea}
  ${surl}  Build surl  ${storageArea}  ${TESTDIR}
  ${output}  Perform rmdir using clientSRM  ${surl}  -r
  Log  ${output}
  Should Contain  ${output}  SRM_SUCCESS

List of voms proxy creation
  Create voms proxy  ${USER.1}  ${PASS.1}  ${VO.1}
  Create voms proxy  ${USER.2}  ${PASS.2}  ${VO.1}
  Create voms proxy  ${USER.1}  ${PASS.1}  ${VO.2}
  Create voms proxy  ${USER.3}  ${PASS.3}  ${VO.1}

Setup local working directory
  ${timestamp}  Get timestamp
  ${uid}  Get uid
  Set Variable If It Does Not Exist  \${TESTDIR}  storm-testsuite_${timestamp.strip()}
  Set Variable If It Does Not Exist  \${DEFAULT_X509_USER_PROXY}  /tmp/x509up_u${uid}
  Create directory  /tmp/${TESTDIR}
  Create directory  /tmp/${TESTDIR}/proxies
  Create directory  /tmp/${TESTDIR}/certificates
  Create directory  /tmp/${TESTDIR}/proxies/${VO.1}
  Create directory  /tmp/${TESTDIR}/proxies/${VO.2}
  Create directory  /tmp/${TESTDIR}/proxies/grid
  Add user  ${USER.1}
  Add user  ${USER.2}
  Add user  ${USER.3}
  List of voms proxy creation
  Create grid proxy  ${USER.1}  ${PASS.1}

Setup remote working directories
  Use voms proxy  ${DEFAULT_USER}  ${VO.1}
  Create remote working directory  ${SA.1}
  Create remote working directory  ${SA.7}
  Create remote working directory  ${SA.9} 
  Use voms proxy  ${DEFAULT_USER}  ${VO.2}
  Create remote working directory  ${SA.2}
  Create remote working directory  ${SA.5}
  Create remote working directory  ${SA.6}
  Create remote working directory  ${SA.8}
  Clear all credentials

Teardown local working directory
  Remove directory  /tmp/${TESTDIR}

Teardown remote working directories
  Use voms proxy  ${DEFAULT_USER}  ${VO.1}
  Clear remote working directory  ${SA.1}
  Clear remote working directory  ${SA.7}
  Clear remote working directory  ${SA.9} 
  Use voms proxy  ${DEFAULT_USER}  ${VO.2}
  Clear remote working directory  ${SA.2}
  Clear remote working directory  ${SA.5}
  Clear remote working directory  ${SA.6}
  Clear remote working directory  ${SA.8}
  Clear all credentials

Setup suite
  Setup local working directory
  Setup remote working directories

Setup suite webdav
  Setup local working directory
  Setup remote working directories

Teardown suite
  Teardown remote working directories
  Teardown local working directory

Teardown suite webdav
  Teardown remote working directories
  Teardown local working directory
