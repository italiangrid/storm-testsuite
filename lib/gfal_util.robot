*** Keywords ***

Run gfal-mkdir on
  [Arguments]  ${url}  ${options}=-v  ${expectedRc}=0
  ${rc}  ${output}  Run And Return Rc And Output  gfal-mkdir ${options} ${url}
  Log  ${output}
  Run Keyword If  ${rc}!=${expectedRc}  Fail  "Exit code value is ${rc} instead of ${expectedRc}"
  RETURN  ${output}

Run gfal-ls on
  [Arguments]  ${url}  ${options}=-laH  ${expectedRc}=0
  ${rc}  ${output}  Run And Return Rc And Output  gfal-ls ${options} ${url}
  Log  ${output}
  Run Keyword If  ${rc}!=${expectedRc}  Fail  "Exit code value is ${rc} instead of ${expectedRc}"
  RETURN  ${output}

Run gfal-rm on  [Arguments]  ${url}  ${options}=-v  ${expectedRc}=0
  ${rc}  ${output}  Run And Return Rc And Output  gfal-rm ${options} ${url}
  Log  ${output}
  Run Keyword If  ${rc}!=${expectedRc}  Fail  "Exit code value is ${rc} instead of ${expectedRc}"
  RETURN  ${output}

Run gfal-rmdir on  [Arguments]  ${url}  ${options}=-v  ${expectedRc}=0
  RETURN  Run gfal-rm on  ${url}  ${options} --recursive ${expectedRc}

Run gfal-stat on  [Arguments]  ${url}  ${options}=-v  ${expectedRc}=0
  ${rc}  ${output}  Run And Return Rc And Output  gfal-stat ${options} ${url}
  Log  ${output}
  Run Keyword If  ${rc}!=${expectedRc}  Fail  "Exit code value is ${rc} instead of ${expectedRc}"
  RETURN  ${output}

Run gfal-copy on  [Arguments]  ${src}  ${dest}  ${options}=-v  ${expectedRc}=0
  ${rc}  ${output}  Run And Return Rc And Output  gfal-copy ${options} ${src} ${dest}
  Log  ${output}
  Run Keyword If  ${rc}!=${expectedRc}  Fail  "Exit code value is ${rc} instead of ${expectedRc}"
  RETURN  ${output}

Run gfal-copy out on  [Arguments]  ${localFileName}  ${url}  ${options}=-v  ${expectedRc}=0
  ${output}  Run gfal-copy on  file:///tmp/${TESTDIR}/${localFileName}  ${url}  ${options}  ${expectedRc}
  RETURN  ${output}

Run gfal-copy in on  [Arguments]  ${url}  ${localFileName}  ${options}=-v  ${expectedRc}=0
  ${output}  Run gfal-copy on  ${url}  file:///tmp/${TESTDIR}/${localFileName}  ${options}  ${expectedRc}
  RETURN  ${output}

Copy-out file using gfal-utils  [Arguments]  ${localFileName}  ${url}  ${options}=-v
  ${output}  Run gfal-copy on  src=file:///tmp/${TESTDIR}/${localFileName}  dest=${url}  options=${options}
  RETURN  ${output}

Copy-in file using gfal-utils  [Arguments]  ${url}  ${localFileName}  ${options}=-v
  ${output}  Run gfal-copy on  src=${url}  dest=file:///tmp/${TESTDIR}/${localFileName}  options=${options}
  RETURN  ${output}

Copy file using gfal-utils  [Arguments]  ${src}  ${dest}  ${options}=-v
  ${output}  Run gfal-copy on  src=${src}  dest=${dest}  options=${options}
  RETURN  ${output}

Get checksum of remote file using gfal-utils  [Arguments]  ${url}  ${algorithm}=adler32
  ${rc}  ${output}  Run And Return Rc And Output  gfal-sum ${url} ${algorithm}
  Log  ${output}
  Should Be Equal As Integers  ${rc}  0
  ${rest}  ${last}=  Split String From Right  ${output}
  RETURN  ${last}
