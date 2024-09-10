*** Keywords ***

Execute clientSRM Command  [Arguments]  ${cmd}  ${options}=${EMPTY}
  ${output}  ${stderr}  Execute and Check Success  clientSRM ${cmd} ${options} -e ${srmEndpoint}
  Log  ${output}
  RETURN  ${output}

Execute clientSRM Command on Surl  [Arguments]  ${cmd}  ${surl}  ${options}=${EMPTY}
  ${output}  ${stderr}  Execute and Check Success  clientSRM ${cmd} ${options} -e ${srmEndpoint} -s ${surl}
  Log  ${output}
  RETURN  ${output}

Execute clientSRM Command on Surl with Token  [Arguments]  ${cmd}  ${surl}  ${token}  ${options}=${EMPTY}
  ${output}  ${stderr}  Execute and Check Success  clientSRM ${cmd} ${options} -e ${srmEndpoint} -s ${surl} -t ${token}
  Log  ${output}
  RETURN  ${output}

Execute clientSRM Command with Token  [Arguments]  ${cmd}  ${token}  ${options}=${EMPTY}
  ${output}  ${stderr}  Execute and Check Success  clientSRM ${cmd} ${options} -e ${srmEndpoint} -t ${token}
  Log  ${output}
  RETURN  ${output}

Perform mkdir using clientSRM  [Arguments]  ${surl}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl  mkdir  ${surl}  ${options}
  RETURN  ${output}

Perform rm using clientSRM  [Arguments]  ${surl}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl  rm  ${surl}  ${options}
  RETURN  ${output}

Perform rmdir using clientSRM  [Arguments]  ${surl}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl  rmdir  ${surl}  ${options}
  RETURN  ${output}

Perform ping using clientSRM
  ${output}  Execute clientSRM Command  ping  -e ${srmEndpoint}
  RETURN  ${output}

Perform ptp using clientSRM  [Arguments]  ${surl}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl  ptp  ${surl}  ${options}
  ${result}  ${token}=  Should Match Regexp  ${output}  requestToken=(\".+\")
  RETURN  ${output}  ${token}

Perform ptp with transfer protocol using clientSRM  [Arguments]  ${surl}  ${protocol}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl  ptp  ${surl}  -T -P ${protocol} ${options}
  ${result}  ${token}=  Should Match Regexp  ${output}  requestToken=(\".+\")
  ${result}  ${turl}=  Should Match Regexp  ${output}  TURL=(\".+\")
  RETURN  ${output}  ${token}  ${turl}

Perform sptp using clientSRM  [Arguments]  ${surl}  ${token}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl with token  sptp  ${surl}  ${token}  ${options}
  RETURN  ${output}

Perform pd using clientSRM  [Arguments]  ${surl}  ${token}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl with token  pd  ${surl}  ${token}  ${options}
  RETURN  ${output}

Perform ptg using clientSRM  [Arguments]  ${surl}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl  ptg  ${surl}  ${options}
  ${result}  ${token}=  Should Match Regexp  ${output}  requestToken=(\".+\")
  RETURN  ${output}  ${token}

Perform ptg with transfer protocol using clientSRM  [Arguments]  ${surl}  ${protocol}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl  ptg  ${surl}  -T -P ${protocol} ${options}
  ${result}  ${token}=  Should Match Regexp  ${output}  requestToken=(\".+\")
  ${result}  ${turl}=  Should Match Regexp  ${output}  transferURL=(\".+\")
  RETURN  ${output}  ${token}  ${turl}

Perform bol using clientSRM  [Arguments]  ${surl}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl  bol  ${surl}  ${options}
  ${result}  ${token}=  Should Match Regexp  ${output}  requestToken=(\".+\")
  RETURN  ${output}  ${token}

Perform sbol using clientSRM  [Arguments]  ${surl}  ${token}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl with token  sbol  ${surl}  ${token}  ${options}
  RETURN  ${output}

Perform sptg using clientSRM  [Arguments]  ${surl}  ${token}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl with token  sptg  ${surl}  ${token}  ${options}
  RETURN  ${output}

Perform rf using clientSRM  [Arguments]  ${surl}  ${token}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl with token  rf  ${surl}  ${token}  ${options}
  RETURN  ${output}

Perform rf using clientSRM without token  [Arguments]  ${surl}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl  rf  ${surl}  ${options}
  RETURN  ${output}

Perform rf using clientSRM without surl  [Arguments]  ${token}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command with Token  rf  ${token}  ${options}
  RETURN  ${output}

Perform abort request using clientSRM  [Arguments]  ${token}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command  AbortRequest  -t ${token} ${options}
  RETURN  ${output}

Perform abort file using clientSRM  [Arguments]  ${surl}  ${token}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl with token  AbortFiles  ${surl}  ${token}  ${options}
  RETURN  ${output}

Perform mv using clientSRM  [Arguments]  ${srcsurl}  ${destsurl}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command  mv -s ${srcsurl} -t ${destsurl}  ${options}
  RETURN  ${output}

Perform ls using clientSRM  [Arguments]  ${surl}  ${options}=${EMPTY}
  ${output}  Execute clientSRM Command on Surl  ls  ${surl}  ${options}
  RETURN  ${output}

Detailed ls using clientSRM  [Arguments]  ${surl}
  ${output}  Perform ls using clientSRM  ${surl}  -l -c 1
  RETURN  ${output}

Get unused size using clientSRM  [Arguments]  ${storageAreaToken}
  ${output}  Execute clientSRM Command  gst  -e httpg://${srmEndpoint}/ -d ${storageAreaToken}
  ${result}  ${token}=  Should Match Regexp  ${output}  (\".+-.+-.+-.+-.+\")
  ${output}  Get space metadata using clientSRM  ${token}
  ${result}  ${unusedSize}=  Should Match Regexp  ${output}  unusedSize=(.+)
  RETURN  ${unusedSize}

Get space metadata using clientSRM  [Arguments]  ${storageAreaToken}
  ${output}  Execute clientSRM Command  gsm  -e httpg://${srmEndpoint}/ -s ${storageAreaToken}
  RETURN  ${output}

Get request summary using clientSRM  [Arguments]  ${token}
  ${output}  Execute clientSRM Command  grs  -e httpg://${srmEndpoint}/ -t ${token}
  RETURN  ${output}

Get request tokens using clientSRM  [Arguments]  ${token}
  ${output}  Execute clientSRM Command  grt  -e httpg://${srmEndpoint}/ -d ${token}
  RETURN  ${output}

Reserve space using clientSRM
  ${output}  Execute clientSRM Command  rs  -e httpg://${srmEndpoint}/ -a 10 -b 5 -r 0,0
  ${result}  ${token}=  Should Match Regexp  ${output}  (\".+-.+-.+-.+-.+\")
  RETURN  ${token}

Reserve space using clientSRM with token  [Arguments]  ${token}
  ${output}  Execute clientSRM Command  rs  -e httpg://${srmEndpoint}/ -a 10 -b 5 -r 0,0 -d ${token}
  RETURN  ${output}

Release space using clientSRM  [Arguments]  ${token}
  ${output}  Execute clientSRM Command  rsp  -e httpg://${srmEndpoint}/ -t ${token} -f 1
  RETURN  ${output}

Create directory using clientSRM  [Arguments]  ${storageArea}  ${path}
  ${surl}  Build Surl  ${storageArea}  ${path}
  ${output}  Perform mkdir using clientSRM  ${surl}
  RETURN  ${output}

Remove empty directory using clientSRM  [Arguments]  ${storageArea}  ${path}
  ${surl}  Build Surl  ${storageArea}  ${path}
  ${output}  Perform rmdir using clientSRM  ${surl}
  RETURN  ${output}

Remove not empty directory using clientSRM  [Arguments]  ${storageArea}  ${path}
  ${surl}  Build Surl  ${storageArea}  ${path}
  ${output}  Perform rmdir using clientSRM  ${surl}  -r
  RETURN  ${output}

Remove file using clientSRM  [Arguments]  ${storageArea}  ${path}
  ${surl}  Build Surl  ${storageArea}  ${path}
  ${output}  Perform rm using clientSRM  ${surl}
  RETURN  ${output}

Put without really putting using clientSRM  [Arguments]  ${surl}
  ${output}  ${token}  Perform ptp using clientSRM  ${surl}  -p
  Should Contain  ${output}  SRM_SPACE_AVAILABLE
  ${output}  Perform pd using clientSRM  ${surl}  ${token}  -p
  Should Contain  ${output}  SRM_SUCCESS
  RETURN  ${output}

List files in directory using clientSRM  [Arguments]  ${storageArea}  ${path}
  ${surl}  Build Surl  ${storageArea}  ${path}
  ${output}  Perform ls using clientSRM  ${surl}
  RETURN  ${output}

Get space token using clientSRM  [Arguments]  ${token}
  ${output}  Execute clientSRM Command  gst -v ES -e httpg://${srmEndpoint} -d ${token}
  ${result}  ${token}=  Should Match Regexp  ${output}  (\".+-.+-.+-.+-.+\")
  RETURN  ${token}

Get space token output using clientSRM  [Arguments]  ${token}
  ${output}  Execute clientSRM Command  gst -v ES -e httpg://${srmEndpoint} -d ${token}
  RETURN  ${output}