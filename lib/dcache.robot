*** Keywords ***

Execute dCache srm command  [Arguments]  ${cmd}  ${url}
  ${output}  ${stderr}  Execute and Check Success  srm${cmd} -2 ${url}
  RETURN  ${output}

Execute dCache srm command and check failure  [Arguments]  ${cmd}  ${url}
  ${output}  Execute and Check Failure  srm${cmd} -2 ${url}
  RETURN  ${output}

Ping using dCache client
  ${output}  Execute dCache srm command  ping  srm://${srmEndpoint}
  RETURN  ${output}

Create directory using dCache client  [Arguments]  ${surl}
  ${output}  Execute dCache srm command  mkdir  ${surl}
  Should Be Empty  ${output}

Try to create directory using dCache client  [Arguments]  ${surl}
  ${output}  Execute dCache srm command and check failure  mkdir  ${surl}
  RETURN  ${output}

Remove directory using dCache client  [Arguments]  ${surl}
  ${output}  Execute dCache srm command  rmdir  ${surl}
  Should Be Empty  ${output}

Try to remove directory using dCache client  [Arguments]  ${surl}
  ${output}  Execute dCache srm command and check failure  rmdir  ${surl}
  RETURN  ${output}

Remove file using dCache client  [Arguments]  ${surl}
  ${output}  Execute dCache srm command  rm  ${surl}
  Should Not Contain  ${output}  SRM_FAILURE

Try to remove file using dCache client  [Arguments]  ${surl}
  ${output}  Execute dCache srm command and check failure  rm  ${surl}
  RETURN  ${output}
