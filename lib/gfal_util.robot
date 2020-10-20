*** Keywords ***

Run gfal-ls on
  [Arguments]  ${url}  ${options}=-laH  ${expectedRc}=0
  ${rc}  ${output}  Run And Return Rc And Output  gfal-ls ${options} ${url}
  Log  ${output}
  Run Keyword If  ${rc}!=${expectedRc}  Fail  "Exit code value is ${rc} instead of ${expectedRc}"
  [Return]  ${output}

Run gfal-rm on  [Arguments]  ${url}  ${options}=${EMPTY}  ${expectedRc}=0
  ${rc}  ${output}  Run And Return Rc And Output  gfal-rm ${options} ${url}
  Log  ${output}
  Run Keyword If  ${rc}!=${expectedRc}  Fail  "Exit code value is ${rc} instead of ${expectedRc}"
  [Return]  ${output}

Run gfal-stat on  [Arguments]  ${url}  ${options}=${EMPTY}  ${expectedRc}=0
  ${rc}  ${output}  Run And Return Rc And Output  gfal-stat ${options} ${url}
  Log  ${output}
  Run Keyword If  ${rc}!=${expectedRc}  Fail  "Exit code value is ${rc} instead of ${expectedRc}"
  [Return]  ${output}

Run gfal-copy on  [Arguments]  ${src}  ${dest}  ${options}=${EMPTY}  ${expectedRc}=0
  ${rc}  ${output}  Run And Return Rc And Output  gfal-copy ${options} ${src} ${dest}
  Log  ${output}
  Run Keyword If  ${rc}!=${expectedRc}  Fail  "Exit code value is ${rc} instead of ${expectedRc}"
  [Return]  ${output}

Run gfal-copy out on  [Arguments]  ${localFileName}  ${url}  ${options}=${EMPTY}  ${expectedRc}=0
  ${output}  Run gfal-copy on  file:///tmp/${TESTDIR}/${localFileName}  ${url}  ${options}  ${expectedRc}
  [Return]  ${output}

Run gfal-copy in on  [Arguments]  ${url}  ${localFileName}  ${options}=${EMPTY}  ${expectedRc}=0
  ${output}  Run gfal-copy on  ${url}  file:///tmp/${TESTDIR}/${localFileName}  ${options}  ${expectedRc}
  [Return]  ${output}

Copy-out file using gfal-utils  [Arguments]  ${localFileName}  ${url}  ${options}=${EMPTY}
  ${output}  Run gfal-copy on  src=file:///tmp/${TESTDIR}/${localFileName}  dest=${url}  options=${options}
  [Return]  ${output}

Copy-in file using gfal-utils  [Arguments]  ${url}  ${localFileName}
  ${output}  Run gfal-copy on  src=${url}  dest=file:///tmp/${TESTDIR}/${localFileName}  options=${options}
  [Return]  ${output}

Copy file using gfal-utils  [Arguments]  ${src}  ${dest}  ${options}=${EMPTY}
  ${output}  Run gfal-copy on  src=${src}  dest=${dest}  options=${options}
  [Return]  ${output}

Get checksum of remote file using gfal-utils  [Arguments]  ${url}  ${algorithm}=adler32
  ${rc}  ${output}  Run And Return Rc And Output  gfal-sum ${url} ${algorithm}
  Log  ${output}
  Should Be Equal As Integers  ${rc}  0
  ${rest}  ${last}=  Split String From Right  ${output}
  [Return]  ${last}

Remove url using gfal-utils  [Arguments]  ${url}  ${options}=${EMPTY}
  ${rc}  ${output}  Run And Return Rc And Output  gfal-rm ${options} -v ${url}
  Log  ${output}
  Run Keyword If  ${rc}!=0  Fail  "Exit code value is ${rc} instead of 0"
  [Return]  ${output}

