*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Get metadata of online file
  [Tags]  metadata
  ${data}  Get metadata of  ${TAPE_SA}  test_metadata/diskonly.txt
  Should Be Equal  ${data["type"]}  FILE
  Should Be Equal  ${data["status"]}  ONLINE
  Should Be Equal  ${data["attributes"]["migrated"]}  ${FALSE}

Get metadata of online and migrated file
  [Tags]  metadata
  ${data}  Get metadata of  ${TAPE_SA}  test_metadata/diskandtape.txt
  Should Be Equal  ${data["type"]}  FILE
  Should Be Equal  ${data["status"]}  ONLINE
  Should Be Equal  ${data["attributes"]["migrated"]}  ${TRUE}

Get metadata of stubbed and migrated file
  [Tags]  metadata
  ${data}  Get metadata of  ${TAPE_SA}  test_metadata/tapeonly.txt
  Should Be Equal  ${data["type"]}  FILE
  Should Be Equal  ${data["status"]}  NEARLINE
  Should Be Equal  ${data["attributes"]["migrated"]}  ${TRUE}

Get metadata of stubbed and migrated with a recall in progress file
  [Tags]  metadata
  ${data}  Get metadata of  ${TAPE_SA}  test_metadata/recallinprogress.txt
  Should Be Equal  ${data["type"]}  FILE
  Should Be Equal  ${data["status"]}  NEARLINE
  Should Be Equal  ${data["attributes"]["migrated"]}  ${TRUE}
  Should Be Equal  ${data["attributes"]["tsmRecT"]}  5b44eee4-de80-4d9c-b4ac-d4a205b4a9d4
  Should Be Equal  ${data["attributes"]["tsmRecR"]}  ${0}
  Should Be Equal  ${data["attributes"]["tsmRecD"]}  ${1495721014482}

Get metadata of directory
  [Tags]  metadata
  ${data}  Get metadata of  ${TAPE_SA}  test_metadata
  Should Be Equal  ${data["type"]}  FOLDER
  Should Be Equal  ${data["status"]}  ONLINE
  Should Contain  ${data["children"]}  diskandtape.txt
  Should Contain  ${data["children"]}  diskonly.txt
  Should Contain  ${data["children"]}  recallinprogress.txt
  Should Contain  ${data["children"]}  tapeonly.txt

Get metadata of not found resource
  [Tags]  metadata
  ${output}  Request Metadata For  ${TAPE_SA}  test_metadata/notfound.txt
  Should Contain  ${output}  404 Not Found

Get metadata with a bad request
  [Tags]  metadata
  ${output}  Unauthorized Request Metadata For  ${TAPE_SA}  ${EMPTY}
  Should Contain  ${output}  401 Unauthorized
