*** Keywords ***

Get user voms proxy path  [Arguments]  ${user}  ${voname}
  ${path}  Set Variable  /tmp/${TESTDIR}/proxies/${voname}/${user}
  RETURN  ${path}

Get user grid proxy path  [Arguments]  ${user}
  ${path}  Set Variable  /tmp/${TESTDIR}/proxies/grid/${user}
  RETURN  ${path}

Get user x509 p12 path  [Arguments]  ${user}
  ${path}  Set Variable  /tmp/${TESTDIR}/certificates/${user}.p12
  RETURN  ${path}

Get user x509 cert path  [Arguments]  ${user}
  ${path}  Set Variable  /tmp/${TESTDIR}/certificates/${user}.cert.pem
  RETURN  ${path}

Get user x509 key path  [Arguments]  ${user}
  ${path}  Set Variable  /tmp/${TESTDIR}/certificates/${user}.key.pem
  RETURN  ${path}
