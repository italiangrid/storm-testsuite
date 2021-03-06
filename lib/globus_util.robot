*** Keywords ***

Copy-out file using globus-utils  [Arguments]  ${localPath}  ${turl}
  Execute and Check Success  globus-url-copy file:///tmp/${TESTDIR}/${localPath} ${turl}

Try to copy-out file using globus-utils  [Arguments]  ${localPath}  ${turl}
  ${output}  Execute and Check Failure  globus-url-copy file:///tmp/${TESTDIR}/${localPath} ${turl}
   [Return]  ${output}

Copy-in file using globus-utils  [Arguments]  ${turl}  ${localPath}
  Execute and Check Success  globus-url-copy ${turl} file:///tmp/${TESTDIR}/${localPath}

Copy-in file using gsiftp protocol  [Arguments]  ${turl}  ${localPath}
  Execute and Check Success  globus-url-copy ${turl} file:///tmp/${TESTDIR}/${localPath}
