*** Variables ***

##### ENDPOINTS #####

${backEndHost}  omii005-vm03.cnaf.infn.it

${frontEndHost}  ${backEndHost}
${frontEndPort}  8444

${gridFTPHost}  ${frontEndHost}

${srmEndpoint}  ${frontEndHost}:${frontEndPort}
${globusEndpoint}  ${frontEndHost}:2811
${recallEndpoint}  ${backEndHost}:9998

${DAVHost}  ${backEndHost}
${DAVPort}  8085
${DAVSecurePort}  8443

${DAVContextPath}  /webdav

${DAVEndpoint}  http://${DAVHost}:${DAVPort}${DAVContextPath}
${DAVSecureEndpoint}  https://${DAVHost}:${DAVSecurePort}${DAVContextPath}

${ldapEndpoint}  ${backEndHost}:2170
${cdmiEndpoint}  cdmi-storm.cnaf.infn.it:8888
${cdmiAdminUser}  restadmin
${cdmiAdminPassword}  restadmin
${iamUserName}  storm_robot_user
${iamUserPassword}  secret
${cdmiClientId}  838129a5-84ca-4dc4-bfd8-421ee317aabd
${cdmiClientSecret}  secret

${iamEndpoint}  https://iam-test.indigo-datacloud.eu

##### CREDENTIALS #####

${USER.1}  test0
${USER.2}  test1
${USER.3}  apostrofe

${DEFAULT_USER}  ${USER.1}

${certsDir}   /usr/share/igi-test-ca
${privateKeyPassword}   pass
${trustdir}  /etc/grid-security/certificates

${xmlrpcToken}   NS4kYAZuR65XJCq

##### GLUE #####

${baseDNGlue}  mds-vo-name=resource,o=grid
${baseDNGlue2}  GLUE2GroupID=resource,o=glue

##### VOs ######

${VO.1}  test.vo
${VO.2}  test.vo.2

${DEFAULT_VO}  ${VO.1}

##### STORAGE AREAS #####

${storageAreaRoot}  /storage

${SA.1}  test.vo
${SA.2}  test.vo.2
${SA.4}  test.vo.2/nested
${SA.5}  alias
${SA.6}  tape
${SA.7}  igi
${SA.8}  test.vo.bis
${SA.9}  noauth

${DEFAULT_SA}  ${SA.1}
${DEFAULT_SA_VONAME}  ${VO.1}

${TAPE_SA}  ${SA.6}
${TAPE_SA_VONAME}  ${VO.2}

${NESTED_SA}  ${SA.4}
${NESTED_SA_VONAME}  ${VO.2}

${ALIASED_SA}  ${SA.5}
${ALIASED_SA_VONAME}  ${VO.2}

##### LINKS

${SYMLINK.1}  testvo_to_testvo2
