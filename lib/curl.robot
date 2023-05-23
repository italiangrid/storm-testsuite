*** Keywords ***

### COMMAND ###

Curl  [Arguments]  ${method}  ${url}  ${options}=${EMPTY}
  ${rc}  ${output}  Run And Return Rc And Output  curl ${options} ${url} -X ${method} -s -L -iv
  Log  ${output}
  Log  ${rc}
  [Return]  ${output}  ${rc}

### OPTIONS ###

Get CURL x509 options  [Arguments]  ${user}=${DEFAULT_USER}
  ${proxy}  Get user grid proxy path  ${user}
  ${x509cert}  Get user x509 cert path  ${user}
  ${options}  Set variable  --cert ${proxy} --cacert ${x509cert} --capath ${trustdir}
  [Return]  ${options}

Get CURL x509 personal certificate options  [Arguments]  ${user}=${DEFAULT_USER}
  ${x509cert}  Get user x509 cert path  ${user}
  ${x509key}  Get user x509 key path  ${user}
  ${options}  Set variable  --cert ${x509cert} --key ${x509key} --capath ${trustdir}
  [Return]  ${options}

Get CURL VOMS proxy options  [Arguments]  ${user}=${DEFAULT_USER}  ${voname}=${DEFAULT_VO}
  ${proxy}  Get user voms proxy path  ${user}  ${voname}
  ${x509cert}  Get user x509 cert path  ${user}
  ${options}  Set variable  --cert ${proxy} --cacert ${x509cert} --capath ${trustdir}
  [Return]  ${options}

Get CURL default VOMS proxy options
  ${options}  Get CURL VOMS proxy options
  [Return]  ${options}

Get CURL default x509 options
  ${options}  Get CURL x509 options
  [Return]  ${options}

Get CURL header  [Arguments]  ${name}  ${value}
  ${output}  Set variable  --header "${name}: ${value}"
  [Return]  ${output}

Get CURL body  [Arguments]  ${value}
  ${output}  Set variable  --data-ascii "${value}"
  [Return]  ${output}