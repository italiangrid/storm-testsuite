*** Keywords ***

Get recall requests in progress  [Arguments]  ${maxResults}
  ${output}  ${rc}  Curl  GET  http://${recallEndpoint}/recalltable/task?maxResults=${maxResults}  -i -H "Token:${xmlrpcToken}"
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}

Get and update to progress recall tasks ready for being taken over  [Arguments]  ${maxResults}
  ${output}  ${rc}  Curl  PUT  http://${recallEndpoint}/recalltable/tasks  -i -s -S -H "Content-Type:text/plain" -H "Token:${xmlrpcToken}" -d first=${maxResults}
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}

Update a recall task status using a groupTaskId  [Arguments]  ${groupTaskId}  ${status}
  ${output}  ${rc}  Curl  PUT  http://${recallEndpoint}/recalltable/task/${groupTaskId}  -i -s -S -H "Content-Type:text/plain" -H "Token:${xmlrpcToken}" -d status=${status}
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}

Check for a completed recall task  [Arguments]  ${requestToken}  ${fileName}
  ${output}  ${rc}  Curl  PUT  http://${recallEndpoint}/recalltable/task  -i -H "Content-Type:text/plain" -H "Token:${xmlrpcToken}" -d $'requestToken=${requestToken}\nsurl=srm://${srmEndpoint}/srm/managerv2?SFN=/${TAPE_SA}/${fileName}'
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}

Insert new recall request  [Arguments]  ${absoluteFilePath}  ${userId}
  ${output}  ${rc}  Curl  POST  http://${recallEndpoint}/recalltable/task  -i -H "Content-Type:application/json" -H "Token:${xmlrpcToken}" -d '{fileName:${absoluteFilePath},userId:${userId}}'
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}

Get first recall task
  ${output}  ${rc}  Curl  PUT  http://${recallEndpoint}/recalltable/tasks  -s -S -H "Content-Type:text/plain" -H "Token:${xmlrpcToken}" -d first=1
  Should Be Equal As Integers  ${rc}  0
  ${data} =  Get Line  ${output}  -1
  Log  ${data}
  [Return]  ${data}

Set success for taskid  [Arguments]  ${taskId}
  ${output}  ${rc}  Curl  PUT  http://${recallEndpoint}/recalltable/task/${taskId}  -s -S -H "Content-Type:text/plain" -H "Token:${xmlrpcToken}" -d "status=0"
  Should Be Equal As Integers  ${rc}  0
  [Return]  ${output}
