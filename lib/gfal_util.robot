*** Keywords ***

List files in directory using gfal-utils  [Arguments]  ${url}  ${expectedRc}=0  ${expectedContent}=${EMPTY}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-ls -laH ${url}
  Log  ${output}
  Should Be Equal As Integers  ${rc}  ${expectedRc}
  Should Contain  ${output}  ${expectedContent}
  [Return]  ${output}

Check exists using gfal-utils  [Arguments]  ${url}
  ${rc}  ${output}  Run gfal-stat on  ${url}
  Log  ${output}
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}

Check not exists using gfal-utils  [Arguments]  ${url}  ${expectedRc}=2  ${expectedContent}=No such file or directory
  ${rc}  ${output}  Run gfal-stat on  ${url}
  Log  ${output}
  Should Be Equal As Integers  ${rc}  ${expectedRc}
  Should Contain  ${output}  ${expectedContent}
  [Return]  ${output}

Run gfal-stat on  [Arguments]  ${url}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-stat ${url}
  Log  ${output}

  [Return]  ${rc}  ${output}

Copy-out file using gfal-utils  [Arguments]  ${localFileName}  ${url}  ${options}=${EMPTY}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-copy -v ${options} file:///tmp/${TESTDIR}/${localFileName} ${url}
  Log  ${output}
  Run Keyword If  ${rc}!=0  Fail  "Exit code value is ${rc} instead of 0"
  [Return]  ${output}

Copy-in file using gfal-utils  [Arguments]  ${url}  ${localFileName}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-copy -v ${url} file:///tmp/${TESTDIR}/${localFileName}
  Log  ${output}
  Run Keyword If  ${rc}!=0  Fail  "Exit code value is ${rc} instead of 0"
  [Return]  ${output}

Copy file using gfal-utils  [Arguments]  ${src}  ${dest}  ${options}=${EMPTY}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-copy -v ${options} ${src} ${dest}
  Log  ${output}
  Run Keyword If  ${rc}!=0  Fail  "Exit code value is ${rc} instead of 0"
  [Return]  ${output}

Get checksum of remote file using gfal-utils  [Arguments]  ${url}  ${algorithm}=adler32
  ${rc}  ${output}  Run And Return Rc And Output  gfal-sum ${url} ${algorithm}
  Log  ${output}
  Should Be Equal As Integers  ${rc}  0
  ${rest}  ${last}=  Split String From Right  ${output}
  [Return]  ${last}

Remove url using gfal-utils  [Arguments]  ${url}  ${options}=${EMPTY}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-rm ${options} -v ${surl}
  Log  ${output}
  Run Keyword If  ${rc}!=0  Fail  "Exit code value is ${rc} instead of 0"
  [Return]  ${output}
