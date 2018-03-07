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

Create voms fake proxy   [Arguments]  ${user}  ${vo}  ${fqans}
  ${usercert}  Get user x509 p12 path  ${user}
  ${userpass}  Set Variable  pass
  ${proxy}  Get user voms proxy path  ${user}  ${vo}
  #${output}  ${stderr}  Run Keyword If  "${vomsFake}" == "true"  Execute and Check Success   echo ${userpass}|VOMS_CLIENTS_JAVA_OPTIONS="-Dvoms.fake.vo=${vo} -Dvoms.fake=${VOMS_FAKE} -Dvoms.fake.aaCert=${VOMS_FAKE_AACERT} -Dvoms.fake.aaKey=${VOMS_FAKE_AAKEY} -Dvoms.fake.fqans=${fqan}" voms-proxy-init -pwstdin --debug --voms ${vo} --cert ${usercert} --out ${proxy}
  ${options}  Set variable  -Dvoms.fake.vo=${vo} -Dvoms.fake=${vomsFake} -Dvoms.fake.aaCert=${vomsFakeCert} -Dvoms.fake.aaKey=${vomsFakeKey} -Dvoms.fake.fqans=${fqans}
  ${output}  ${stderr}  Execute and Check Success   echo ${userpass}|VOMS_CLIENTS_JAVA_OPTIONS="${options}" voms-proxy-init -pwstdin --voms ${vo} --cert ${usercert} --out ${proxy}
  Log  ${output}
  Log  ${stderr}

Create voms proxy   [Arguments]   ${user}  ${vo}
  ${usercert}  Get user x509 p12 path  ${user}
  ${userpass}  Set Variable  pass
  ${proxy}  Get user voms proxy path  ${user}  ${vo}
  #${output}  ${stderr}  Run Keyword If  "${vomsFake}" == "false"  Execute and Check Success   echo ${userpass}|voms-proxy-init -pwstdin --voms ${vo} --cert ${usercert} --out ${proxy}
  ${output}  ${stderr}  Execute and Check Success   echo ${userpass}|voms-proxy-init -pwstdin --voms ${vo} --cert ${usercert} --out ${proxy}
  Log  ${output}
  Log  ${stderr}

Create grid proxy   [Arguments]   ${user}
  ${usercert}  Get user x509 p12 path  ${user}
  ${userpass}  Set Variable  pass
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

Create webdav remote working directory  [Arguments]  ${storageArea}  ${options}
  ${url}  Build URL  ${DAVSecureEndpoint}  ${storageArea}
  ${output}  ${stderr}  Do CURL MKCOL  ${url}  ${options}
  Log  ${output}
  Should Contain  ${output}  201 Created

Clear remote working directory  [Arguments]  ${storageArea}
  ${surl}  Build surl  ${storageArea}  ${TESTDIR}
  ${output}  Perform rmdir using clientSRM  ${surl}  -r
  Log  ${output}
  Should Contain  ${output}  SRM_SUCCESS

Clear webdav remote working directory  [Arguments]  ${storageArea}  ${options}
  ${url}  Build URL  ${DAVSecureEndpoint}  ${storageArea}
  ${output}  ${stderr}  Do CURL DELETE  ${url}  ${options}
  Log  ${output}
  Should Contain  ${output}  204 No Content

List of voms fake proxy creation
  Create voms fake proxy  ${USER.1}  ${VO.1}  ${vomsFakeFqans.1}
  Create voms fake proxy  ${USER.2}  ${VO.1}  ${vomsFakeFqans.1}
  Create voms fake proxy  ${USER.3}  ${VO.1}  ${vomsFakeFqans.1}
  Create voms fake proxy  ${USER.1}  ${VO.2}  ${vomsFakeFqans.2}

List of voms proxy creation
  Create voms proxy  ${USER.1}  ${VO.1}
  Create voms proxy  ${USER.2}  ${VO.1}
  Create voms proxy  ${USER.1}  ${VO.2}
  Create voms proxy  ${USER.3}  ${VO.1}


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
  Run keyword if   "${vomsFake}" == "true"  List of voms fake proxy creation
  Run keyword if   "${vomsFake}" == "false" List of voms proxy creation
  #Create voms fake proxy  ${USER.1}  ${VO.1}  ${VOMS_FAKE_FQANS.1}
  #Create voms fake proxy  ${USER.2}  ${VO.1}  ${VOMS_FAKE_FQANS.1}
  #Create voms fake proxy  ${USER.3}  ${VO.1}  ${VOMS_FAKE_FQANS.1}
  #Create voms fake proxy  ${USER.1}  ${VO.2}  ${VOMS_FAKE_FQANS.2}
  #Create voms proxy  ${USER.1}  ${VO.1}
  #Create voms proxy  ${USER.2}  ${VO.1}
  #Create voms proxy  ${USER.1}  ${VO.2}
  #Create voms proxy  ${USER.3}  ${VO.1}
  Create grid proxy  ${USER.1}

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
  
Setup webdav remote working directories
  Use voms proxy  ${DEFAULT_USER}  ${DEFAULT_VO}
  ${options}  Get CURL VOMS proxy options  ${DEFAULT_USER}  ${DEFAULT_VO}
  Create webdav remote working directory  ${DEFAULT_SA}  ${options}
  Create webdav remote working directory  ${SA.7}  ${options}
  Create webdav remote working directory  ${SA.9}  ${options}
  Use voms proxy  ${DEFAULT_USER}  ${VO.2}
  ${options}  Get CURL VOMS proxy options  ${DEFAULT_USER}  ${VO.2}
  Create webdav remote working directory  ${SA.2}  ${options}
  Create webdav remote working directory  ${SA.5}  ${options}
  Create webdav remote working directory  ${SA.8}  ${options}
  Create webdav remote working directory  ${SA.6}  ${options}
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
  
Teardown webdav remote working directories
  Use voms proxy  ${DEFAULT_USER}  ${DEFAULT_VO}
  ${options}  Get CURL VOMS proxy options  ${DEFAULT_USER}  ${DEFAULT_VO}
  Clear webdav remote working directory  ${DEFAULT_SA}  ${options}
  Clear webdav remote working directory  ${SA.7}  ${options}
  Clear webdav remote working directory  ${SA.9}  ${options}
  Use voms proxy  ${DEFAULT_USER}  ${VO.2}
  ${options}  Get CURL VOMS proxy options  ${DEFAULT_USER}  ${VO.2}
  Clear webdav remote working directory  ${SA.2}  ${options}
  Clear webdav remote working directory  ${SA.5}  ${options}
  Clear webdav remote working directory  ${SA.8}  ${options}
  Clear webdav remote working directory  ${SA.6}  ${options}
  Clear all credentials

Setup suite
  Setup local working directory
  Setup remote working directories

Setup suite webdav
  Setup local working directory
  Setup webdav remote working directories

Teardown suite
  Teardown remote working directories
  Teardown local working directory

Teardown suite webdav
  Teardown webdav remote working directories
  Teardown local working directory
