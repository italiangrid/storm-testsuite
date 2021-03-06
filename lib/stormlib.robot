*** Keywords ***

Execute and Check Success  [Arguments]  ${cmd}
  ${rc}  ${output}=  Run and Return RC And Output  ${cmd}
  Should Be Equal As Integers  ${rc}  0  ${cmd} failed with ${output}  False
  [Return]  ${output}  ${EMPTY}

Execute and Check Failure   [Arguments]   ${cmd}
  ${rc}   ${output}=   Run and Return RC And Output  ${cmd}
  Should Not Be Equal As Integers  ${rc}  0  ${cmd} failed with ${output}
  [Return]  ${output}

Get a unique name
  ${name}  ${stderr}  Execute and Check Success  basename `mktemp`
  Execute and Check Success  rm -f /tmp/${name}
  [Return]  ${name}

Create local file
  ${name}  Get a unique name
  Execute and Check Success  dd if=/dev/urandom of=/tmp/${TESTDIR}/${name} bs=1M count=1
  [Return]  ${name}

Create local file with text  [Arguments]  ${fileContent}=File di testo di prova
  ${name}  Get a unique name
  ${path}  Get local file path from name  ${name}
  Execute and Check Success  echo -n "${fileContent}" > ${path}
  [Return]  ${name}

Get local file path from name  [Arguments]  ${name}
  [Return]  /tmp/${TESTDIR}/${name}

Create local file with fake size  [Arguments]  ${megabytes}
  ${name}  Get a unique name
  Execute and Check Success  dd if=/dev/null of=/tmp/${TESTDIR}/${name} bs=1M count=1 seek=${megabytes}
  [Return]  ${name}

Create local empty file
  ${name}  Get a unique name
  Execute and Check Success  touch /tmp/${TESTDIR}/${name}
  [Return]  ${name}

Create local file with checksum that starts with zero
  ${name}  Get a unique name
  Execute and Check Success  echo "a" > /tmp/${TESTDIR}/${name}
  [Return]  ${name}

Create local directory  [Arguments]  ${dirname}
  Execute and Check Success  mkdir /tmp/${dirname}

Remove local file  [Arguments]  ${filename}
  Execute and Check Success  rm -f /tmp/${TESTDIR}/${filename}

Remove local directory  [Arguments]  ${dirname}
  Execute and Check Success  rm -rf /tmp/${dirname}

Build surl  [Arguments]  ${storageArea}  ${relativePath}
  ${output}  Set variable  srm://${srmEndpoint}/srm/managerv2?SFN=/${storageArea}/${relativePath}
  [Return]  ${output}

Build simple surl  [Arguments]  ${storageArea}  ${relativePath}
  ${output}  Set variable  srm://${srmEndpoint}/${storageArea}/${relativePath}
  [Return]  ${output}

Build gsiftp TURL  [Arguments]  ${storageArea}  ${relativePath}
  ${output}  Set variable  gsiftp://${globusEndpoint}/${storageAreaRoot}/${storageArea}/${relativePath}
  [Return]  ${output}

Get SA Token  [Arguments]  ${saname}=${DEFAULT_SA}
  ${output}  ${error}  Execute and Check Success  echo "${saname}" | sed "s/[^A-Za-z0-99]//g"
  [Return]  ${output.upper()}_TOKEN
