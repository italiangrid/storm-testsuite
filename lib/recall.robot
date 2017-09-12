*** Keywords ***

Get recall requests in progress  [Arguments]  ${maxResults}
  ${output}  ${stderr}  Curl  GET  http://${recallEndpoint}/recalltable/task?maxResults=${maxResults}  -i -H "Token:${xmlrpcToken}"
  Log  ${output}
  [Return]  ${output}

Get and update to progress recall tasks ready for being taken over  [Arguments]  ${maxResults}
  ${output}  ${stderr}  Curl  PUT  http://${recallEndpoint}/recalltable/tasks  -i -s -S -H "Content-Type:text/plain" -H "Token:${xmlrpcToken}" -d first=${maxResults}
  Log  ${output}
  [Return]  ${output}

Update a recall task status using a groupTaskId  [Arguments]  ${groupTaskId}  ${status}
  ${output}  ${stderr}  Curl  PUT  http://${recallEndpoint}/recalltable/task/${groupTaskId}  -i -s -S -H "Content-Type:text/plain" -H "Token:${xmlrpcToken}" -d status=${status}
  Log  ${output}
  [Return]  ${output}

Check for a completed recall task  [Arguments]  ${requestToken}  ${fileName}
  ${output}  ${stderr}  Curl  PUT  http://${recallEndpoint}/recalltable/task  -i -H "Content-Type:text/plain" -H "Token:${xmlrpcToken}" -d $'requestToken=${requestToken}\nsurl=srm://${srmEndpoint}/srm/managerv2?SFN=/${TAPE_SA}/${fileName}'
  Log  ${output}
  [Return]  ${output}

Insert new recall request  [Arguments]  ${absoluteFilePath}  ${userId}
  ${output}  ${stderr}  Curl  POST  http://${recallEndpoint}/recalltable/task  -i -H "Content-Type:application/json" -H "Token:${xmlrpcToken}" -d '{fileName:${absoluteFilePath},userId:${userId}}'
  Log  ${output}
  [Return]  ${output}

Get first recall task
  ${output}  ${stderr}  Curl  PUT  http://${recallEndpoint}/recalltable/tasks  -s -S -H "Content-Type:text/plain" -H "Token:${xmlrpcToken}" -d first=1
  Log  ${output}
  ${data} =  Get Line  ${output}  -1
  Log  ${data}
  [Return]  ${data}

Set success for taskid  [Arguments]  ${taskId}
  ${output}  ${stderr}  Curl  PUT  http://${recallEndpoint}/recalltable/task/${taskId}  -s -S -H "Content-Type:text/plain" -H "Token:${xmlrpcToken}" -d "status=0"
  Log  ${output}
  [Return]  ${output}