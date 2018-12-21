*** Keywords ***

List files in directory using gfal-utils  [Arguments]  ${surl}  ${expectedRc}=0  ${expectedContent}=${EMPTY}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-ls -laH ${surl}
  Log  ${output}
  Should Be Equal As Integers  ${rc}  ${expectedRc}
  Should Contain  ${output}  ${expectedContent}
  [Return]  ${output}

Check surl exists using gfal-utils  [Arguments]  ${surl}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-stat ${surl}
  Log  ${output}
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}

Check surl does not exists using gfal-utils  [Arguments]  ${surl}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-stat ${surl}
  Log  ${output}
  Should Be Equal As Integers  ${rc}  2
  Should Contain  ${output}  No such file or directory
  Should Contain  ${output}  SRM_INVALID_PATH
  [Return]  ${output}

Copy-out file using gfal-utils  [Arguments]  ${localFileName}  ${surl}  ${options}=${EMPTY}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-copy -v ${options} file:///tmp/${TESTDIR}/${localFileName} ${surl}
  Log  ${output}
  Run Keyword If  ${rc}!=0  Fail  "Exit code value is ${rc} instead of 0"
  [Return]  ${output}

Copy-in file using gfal-utils  [Arguments]  ${surl}  ${localFileName}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-copy -v ${surl} file:///tmp/${TESTDIR}/${localFileName}
  Log  ${output}
  Run Keyword If  ${rc}!=0  Fail  "Exit code value is ${rc} instead of 0"
  [Return]  ${output}

Copy file using gfal-utils  [Arguments]  ${srcSurl}  ${destSurl}  ${options}=${EMPTY}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-copy -v ${options} ${srcSurl} ${destSurl}
  Log  ${output}
  Run Keyword If  ${rc}!=0  Fail  "Exit code value is ${rc} instead of 0"
  [Return]  ${output}

Get checksum of remote file using gfal-utils  [Arguments]  ${surl}  ${algorithm}=adler32
  ${rc}  ${output}  Run And Return Rc And Output  gfal-sum ${surl} ${algorithm}
  Log  ${output}
  Should Be Equal As Integers  ${rc}  0
  ${rest}  ${last}=  Split String From Right  ${output}
  [Return]  ${last}
