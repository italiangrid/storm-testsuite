*** Keywords ***

List files in directory using lcg_utils  [Arguments]  ${surl}
  ${output}  Run  lcg-ls -l -b -D srmv2 ${surl}
  RETURN  ${output}

Check file exists using lcg-utils  [Arguments]  ${surl}
  ${output}  Run  lcg-ls -l -b -D srmv2 ${surl}
  RETURN  ${output}

Check file does not exists using lcg-utils  [Arguments]  ${surl}
  ${output}  Run  lcg-ls -l -b -D srmv2 ${surl}
  Should Contain  ${output}  No such file or directory

Copy-out file using lcg-utils  [Arguments]  ${localFileName}  ${surl}  ${options}=${EMPTY}
  ${output}  Run  lcg-cp -b -D srmv2 file:///tmp/${TESTDIR}/${localFileName} ${surl} -v ${options}
  RETURN  ${output}

Copy-in file using lcg-utils  [Arguments]  ${surl}  ${localFileName}
  ${output}  Run  lcg-cp -b -D srmv2 ${surl} file:///tmp/${TESTDIR}/${localFileName} -v
  RETURN  ${output}

Copy file using lcg-utils  [Arguments]  ${srcSurl}  ${destSurl}  ${options}=${EMPTY}
  ${output}  Run  lcg-cp -b -D srmv2 ${srcSurl} ${destSurl} -v ${options}
  RETURN  ${output}
