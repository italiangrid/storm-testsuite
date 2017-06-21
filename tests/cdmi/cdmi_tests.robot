*** Settings ***

Resource   lib/import.robot

*** Test Cases ***

Get CDMI Capabilities as restadmin user
  [Tags]  cdmi
  ${data}  Get CDMI Capabilities  -u ${cdmiAdminUser}:${cdmiAdminPassword}
  Should Contain  ${data["children"]}  container
  Should Contain  ${data["children"]}  dataobject
  Should Be Equal  ${data["objectName"]}  cdmi_capabilities
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Get CDMI Container Capabilities as restadmin user
  [Tags]  cdmi
  ${data}  Get CDMI Capability  container/  -u ${cdmiAdminUser}:${cdmiAdminPassword}
  Should Contain  ${data["children"]}  DiskOnly
  Should Be Equal  ${data["objectName"]}  container
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Get CDMI Dataobject Capabilities as restadmin user
  [Tags]  cdmi
  ${data}  Get CDMI Capability  dataobject/  -u ${cdmiAdminUser}:${cdmiAdminPassword}
  Should Contain  ${data["children"]}  DiskOnly
  Should Contain  ${data["children"]}  DiskAndTape
  Should Contain  ${data["children"]}  TapeOnly
  Should Be Equal  ${data["objectName"]}  dataobject
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Get CDMI Container DiskOnly Capability as restadmin user
  [Tags]  cdmi
  ${data}  Get CDMI Capability  container/DiskOnly/  -u ${cdmiAdminUser}:${cdmiAdminPassword}
  Check Container DiskOnly Capability  ${data}

Get CDMI Container DiskOnly Capability as a user with read scope
  [Tags]  cdmi
  ${accessToken}  Get Access Token With Read Scope  ${iamUserName}  ${iamUserPassword}
  ${data}  Get CDMI Capability  container/DiskOnly/  -H "Authorization: Bearer ${accessToken}"
  Check Container DiskOnly Capability  ${data}

Get CDMI Dataobject DiskOnly Capability as restadmin user
  [Tags]  cdmi
  ${data}  Get CDMI Capability  dataobject/DiskOnly/  -u ${cdmiAdminUser}:${cdmiAdminPassword}
  Check Dataobject DiskOnly Capability  ${data}

Get CDMI Dataobject DiskOnly Capability as a user with read scope
  [Tags]  cdmi
  ${accessToken}  Get Access Token With Read Scope  ${iamUserName}  ${iamUserPassword}
  ${data}  Get CDMI Capability  dataobject/DiskOnly/  -H "Authorization: Bearer ${accessToken}"
  Check Dataobject DiskOnly Capability  ${data}

Get CDMI Dataobject DiskAndTape Capability as restadmin user
  [Tags]  cdmi
  ${data}  Get CDMI Capability  dataobject/DiskAndTape/  -u ${cdmiAdminUser}:${cdmiAdminPassword}
  Check Dataobject DiskAndTape Capability  ${data}

Get CDMI Dataobject DiskAndTape Capability as a user with read scope
  [Tags]  cdmi
  ${accessToken}  Get Access Token With Read Scope  ${iamUserName}  ${iamUserPassword}
  ${data}  Get CDMI Capability  dataobject/DiskAndTape/  -H "Authorization: Bearer ${accessToken}"
  Check Dataobject DiskAndTape Capability  ${data}

Get CDMI Dataobject TapeOnly Capability as restadmin user
  [Tags]  cdmi
  ${data}  Get CDMI Capability  dataobject/TapeOnly/  -u ${cdmiAdminUser}:${cdmiAdminPassword}
  Check Dataobject TapeOnly Capability  ${data}

Get CDMI Dataobject TapeOnly Capability as a user with read scope
  [Tags]  cdmi
  ${accessToken}  Get Access Token With Read Scope  ${iamUserName}  ${iamUserPassword}
  ${data}  Get CDMI Capability  dataobject/TapeOnly/  -H "Authorization: Bearer ${accessToken}"
  Check Dataobject TapeOnly Capability  ${data}

*** Keywords ***

Check Container DiskOnly Capability  [Arguments]  ${data}
  Should Be Equal  ${data["objectName"]}  DiskOnly
  Should Be Equal  ${data["metadata"]["cdmi_data_redundancy"]}  1
  Should Be Equal  ${data["metadata"]["cdmi_latency"]}  0
  Should Be Equal  ${data["metadata"]["cdmi_throughput"]}  4194304
  Should Contain  ${data["metadata"]["cdmi_geographic_placement"]}  IT
  Should Be Equal  ${data["capabilities"]["cdmi_default_dataobject_capability_class"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_data_redundancy"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_location"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_geographic_placement"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_latency"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_capabilities_exact_inherit"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_capabilities_templates"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_export_container_http"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_throughput"]}  ${TRUE}
  Should Be Equal  ${data["parentURI"]}  /cdmi_capabilities/container
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Check Dataobject DiskOnly Capability  [Arguments]  ${data}
  Should Be Equal  ${data["objectName"]}  DiskOnly
  Should Be Equal  ${data["metadata"]["cdmi_data_redundancy"]}  1
  Should Be Equal  ${data["metadata"]["cdmi_latency"]}  0
  Should Be Equal  ${data["metadata"]["cdmi_throughput"]}  4194304
  Should Contain  ${data["metadata"]["cdmi_geographic_placement"]}  IT
  Should Be Equal  ${data["capabilities"]["cdmi_data_redundancy"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_geographic_placement"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_latency"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_capabilities_exact_inherit"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_capabilities_templates"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_throughput"]}  ${TRUE}
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Check Dataobject DiskAndTape Capability  [Arguments]  ${data}
  Should Be Equal  ${data["objectName"]}  DiskAndTape
  Should Be Equal  ${data["metadata"]["cdmi_data_redundancy"]}  2
  Should Be Equal  ${data["metadata"]["cdmi_latency"]}  0
  Should Be Equal  ${data["metadata"]["cdmi_throughput"]}  4194304
  Should Contain  ${data["metadata"]["cdmi_geographic_placement"]}  IT
  Should Be Equal  ${data["capabilities"]["cdmi_data_redundancy"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_geographic_placement"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_latency"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_capabilities_exact_inherit"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_capabilities_templates"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_throughput"]}  ${TRUE}
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Check Dataobject TapeOnly Capability  [Arguments]  ${data}
  Should Be Equal  ${data["objectName"]}  TapeOnly
  Should Be Equal  ${data["metadata"]["cdmi_data_redundancy"]}  1
  Should Be Equal  ${data["metadata"]["cdmi_latency"]}  10000
  Should Be Equal  ${data["metadata"]["cdmi_throughput"]}  4194304
  Should Be Equal  ${data["metadata"]["cdmi_data_storage_lifetime"]}  P20Y
  Should Be Equal  ${data["metadata"]["cdmi_durability"]}  99.999
  Should Contain  ${data["metadata"]["cdmi_capabilities_allowed"]}  /cdmi_capabilities/dataobject/DiskAndTape
  Should Contain  ${data["metadata"]["cdmi_geographic_placement"]}  IT
  Should Be Equal  ${data["capabilities"]["cdmi_data_redundancy"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_geographic_placement"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_data_redundancy"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_latency"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_capabilities_exact_inherit"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_capabilities_templates"]}  ${TRUE}
  Should Be Equal  ${data["capabilities"]["cdmi_throughput"]}  ${TRUE}
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability