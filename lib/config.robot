*** Keywords ***

Get user voms proxy path  [Arguments]  ${user}  ${voname}
  ${path}  Set Variable  /tmp/${TESTDIR}/proxies/${voname}/${user}
  [Return]  ${path}

Get user voms fake proxy path  [Arguments]  ${user}  ${voname}
  ${path}  Set Variable  /tmp/${TESTDIR}/fakeproxies/${voname}/${user}
  [Return]  ${path}

Get user grid proxy path  [Arguments]  ${user}
  ${path}  Set Variable  /tmp/${TESTDIR}/proxies/grid/${user}
  [Return]  ${path}

Get user x509 p12 path  [Arguments]  ${user}
  ${path}  Set Variable  /tmp/${TESTDIR}/certificates/${user}.p12
  [Return]  ${path}

Get user x509 cert path  [Arguments]  ${user}
  ${path}  Set Variable  /tmp/${TESTDIR}/certificates/${user}.cert.pem
  [Return]  ${path}

Get user x509 key path  [Arguments]  ${user}
  ${path}  Set Variable  /tmp/${TESTDIR}/certificates/${user}.key.pem
  [Return]  ${path}
