*** Keywords ***

List files in directory using lcg_utils  [Arguments]  ${surl}
  ${output}  Run  lcg-ls -l -b -D srmv2 ${surl}
  [Return]  ${output}

Check file exists using lcg-utils  [Arguments]  ${surl}
  ${output}  Run  lcg-ls -l -b -D srmv2 ${surl}
  [Return]  ${output}

Check file does not exists using lcg-utils  [Arguments]  ${surl}
  ${output}  Run  lcg-ls -l -b -D srmv2 ${surl}
  Should Contain  ${output}  No such file or directory

Copy-out file using lcg-utils  [Arguments]  ${localFileName}  ${surl}  ${options}=${EMPTY}
  ${output}  Run  lcg-cp -b -D srmv2 file:///tmp/${TESTDIR}/${localFileName} ${surl} -v ${options}
  [Return]  ${output}

Copy-in file using lcg-utils  [Arguments]  ${surl}  ${localFileName}
  ${output}  Run  lcg-cp -b -D srmv2 ${surl} file:///tmp/${TESTDIR}/${localFileName} -v
  [Return]  ${output}

Copy file using lcg-utils  [Arguments]  ${srcSurl}  ${destSurl}  ${options}=${EMPTY}
  ${output}  Run  lcg-cp -b -D srmv2 ${srcSurl} ${destSurl} -v ${options}
  [Return]  ${output}
