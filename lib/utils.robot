*** Keywords ***

Cat local file  [Arguments]  ${localFileName}
  ${output}  ${error}  Execute and Check Success  cat  /tmp/${TESTDIR}/${localFileName}
  [Return]  ${output}
