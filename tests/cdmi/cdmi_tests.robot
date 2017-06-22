*** Settings ***

Resource   lib/import.robot

*** Variables ***

${AUTH} =  ${EMPTY}

*** Test Cases ***

Get CDMI Capabilities as restadmin user
  [Tags]  cdmi
  [Setup]  Use restadmin user
  ${data}  Get CDMI Capabilities  ${AUTH}
  Should Contain  ${data["children"]}  container
  Should Contain  ${data["children"]}  dataobject
  Should Be Equal  ${data["objectName"]}  cdmi_capabilities
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Get CDMI Container Capabilities as restadmin user
  [Tags]  cdmi
  [Setup]  Use restadmin user
  ${data}  Get CDMI Capability  container/  ${AUTH}
  Should Contain  ${data["children"]}  DiskOnly
  Should Be Equal  ${data["objectName"]}  container
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Get CDMI Dataobject Capabilities as restadmin user
  [Tags]  cdmi
  [Setup]  Use restadmin user
  ${data}  Get CDMI Capability  dataobject/  ${AUTH}
  Should Contain  ${data["children"]}  DiskOnly
  Should Contain  ${data["children"]}  DiskAndTape
  Should Contain  ${data["children"]}  TapeOnly
  Should Be Equal  ${data["objectName"]}  dataobject
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Get CDMI Container DiskOnly Capability as restadmin user
  [Tags]  cdmi
  [Setup]  Use restadmin user
  ${data}  Get CDMI Capability  container/DiskOnly/  ${AUTH}
  Check Container DiskOnly Capability  ${data}

Get CDMI Container DiskOnly Capability as a user with read scope
  [Tags]  cdmi
  [Setup]  Use access token of authorized iam user
  ${data}  Get CDMI Capability  container/DiskOnly/  ${AUTH}
  Check Container DiskOnly Capability  ${data}

Get CDMI Dataobject DiskOnly Capability as restadmin user
  [Tags]  cdmi
  [Setup]  Use restadmin user
  ${data}  Get CDMI Capability  dataobject/DiskOnly/  ${AUTH}
  Check Dataobject DiskOnly Capability  ${data}

Get CDMI Dataobject DiskOnly Capability as a user with read scope
  [Tags]  cdmi
  [Setup]  Use access token of authorized iam user
  ${data}  Get CDMI Capability  dataobject/DiskOnly/  ${AUTH}
  Check Dataobject DiskOnly Capability  ${data}

Get CDMI Dataobject DiskAndTape Capability as restadmin user
  [Tags]  cdmi
  [Setup]  Use restadmin user
  ${data}  Get CDMI Capability  dataobject/DiskAndTape/  ${AUTH}
  Check Dataobject DiskAndTape Capability  ${data}

Get CDMI Dataobject DiskAndTape Capability as a user with read scope
  [Tags]  cdmi
  [Setup]  Use access token of authorized iam user
  ${data}  Get CDMI Capability  dataobject/DiskAndTape/  ${AUTH}
  Check Dataobject DiskAndTape Capability  ${data}

Get CDMI Dataobject TapeOnly Capability as restadmin user
  [Tags]  cdmi
  [Setup]  Use restadmin user
  ${data}  Get CDMI Capability  dataobject/TapeOnly/  ${AUTH}
  Check Dataobject TapeOnly Capability  ${data}

Get CDMI Dataobject TapeOnly Capability as a user with read scope
  [Tags]  cdmi
  [Setup]  Use access token of authorized iam user
  ${data}  Get CDMI Capability  dataobject/TapeOnly/  ${AUTH}
  Check Dataobject TapeOnly Capability  ${data}

Get CDMI Dataobject DiskOnly Status as a user with read scope
  [Tags]  cdmi
  [Setup]  Use access token of authorized iam user
  ${data}  Get CDMI Status  tape/test_metadata/diskonly.txt  ${AUTH}
  Check Dataobject DiskOnly Metadata  ${data}  /tape/test_metadata  diskonly.txt

Get CDMI Dataobject DiskAndTape Status as a user with read scope
  [Tags]  cdmi
  [Setup]  Use access token of authorized iam user
  ${data}  Get CDMI Status  tape/test_metadata/diskandtape.txt  ${AUTH}
  Check Dataobject DiskAndTape Metadata  ${data}  /tape/test_metadata  diskandtape.txt

Get CDMI Dataobject TapeOnly Status as a user with read scope
  [Tags]  cdmi
  [Setup]  Use access token of authorized iam user
  ${data}  Get CDMI Status  tape/test_metadata/tapeonly.txt  ${AUTH}
  Check Dataobject TapeOnly Metadata  ${data}  /tape/test_metadata  tapeonly.txt


*** Keywords ***

Use restadmin user
  Set Test Variable  ${AUTH}  -u ${cdmiAdminUser}:${cdmiAdminPassword}

Use access token of authorized iam user
  ${accessToken}  Get Access Token With Read Scope  ${iamUserName}  ${iamUserPassword}
  Set Test Variable  ${AUTH}  -H "Authorization: Bearer ${accessToken}"

Should have capability  [Arguments]  ${capabilities}  ${name}
  Should Be Equal  ${capabilities["${name}"]}  ${TRUE}

Should have metadata value  [Arguments]  ${metadata}  ${key}  ${value}
  Should Be Equal  ${metadata["${key}"]}  ${value}

Should contain metadata value  [Arguments]  ${metadata}  ${key}  ${value}
  Should Contain  ${metadata["${key}"]}  ${value}

Check container capabilities  [Arguments]  ${capabilities}
  Should have capability  ${capabilities}  cdmi_default_dataobject_capability_class
  Should have capability  ${capabilities}  cdmi_data_redundancy
  Should have capability  ${capabilities}  cdmi_location
  Should have capability  ${capabilities}  cdmi_geographic_placement
  Should have capability  ${capabilities}  cdmi_latency
  Should have capability  ${capabilities}  cdmi_capabilities_exact_inherit
  Should have capability  ${capabilities}  cdmi_capabilities_templates
  Should have capability  ${capabilities}  cdmi_export_container_http
  Should have capability  ${capabilities}  cdmi_throughput

Check dataobject capabilities  [Arguments]  ${capabilities}
  Should have capability  ${capabilities}  cdmi_data_redundancy
  Should have capability  ${capabilities}  cdmi_geographic_placement
  Should have capability  ${capabilities}  cdmi_latency
  Should have capability  ${capabilities}  cdmi_capabilities_exact_inherit
  Should have capability  ${capabilities}  cdmi_capabilities_templates
  Should have capability  ${capabilities}  cdmi_throughput

Check DiskOnly metadata values  [Arguments]  ${metadata}
  Should have metadata value  ${metadata}  cdmi_data_redundancy  1
  Should have metadata value  ${metadata}  cdmi_throughput  4194304
  Should have metadata value  ${metadata}  cdmi_latency  0
  Should contain metadata value  ${metadata}  cdmi_geographic_placement  IT

Check DiskOnly provided metadata values  [Arguments]  ${metadata}
  Should have metadata value  ${metadata}  cdmi_data_redundancy_provided  1
  Should have metadata value  ${metadata}  cdmi_throughput_provided  4194304
  Should have metadata value  ${metadata}  cdmi_latency_provided  0
  Should contain metadata value  ${metadata}  cdmi_geographic_placement_provided  IT

Check DiskAndTape metadata values  [Arguments]  ${metadata}
  Should have metadata value  ${metadata}  cdmi_data_redundancy  2
  Should have metadata value  ${metadata}  cdmi_throughput  4194304
  Should have metadata value  ${metadata}  cdmi_latency  0
  Should contain metadata value  ${metadata}  cdmi_geographic_placement  IT

Check DiskAndTape provided metadata values  [Arguments]  ${metadata}
  Should have metadata value  ${metadata}  cdmi_data_redundancy_provided  2
  Should have metadata value  ${metadata}  cdmi_throughput_provided  4194304
  Should have metadata value  ${metadata}  cdmi_latency_provided  0
  Should contain metadata value  ${metadata}  cdmi_geographic_placement_provided  IT

Check TapeOnly metadata values  [Arguments]  ${metadata}
  Should have metadata value  ${metadata}  cdmi_data_redundancy  1
  Should have metadata value  ${metadata}  cdmi_throughput  4194304
  Should have metadata value  ${metadata}  cdmi_latency  10000
  Should contain metadata value  ${metadata}  cdmi_geographic_placement  IT
  Should have metadata value  ${metadata}  cdmi_data_storage_lifetime  P20Y
  Should have metadata value  ${metadata}  cdmi_durability  99.999
  Should contain metadata value  ${metadata}  cdmi_capabilities_allowed  /cdmi_capabilities/dataobject/DiskAndTape

Check TapeOnly provided metadata values  [Arguments]  ${metadata}
  Should have metadata value  ${metadata}  cdmi_data_redundancy_provided  1
  Should have metadata value  ${metadata}  cdmi_throughput_provided  4194304
  Should have metadata value  ${metadata}  cdmi_latency_provided  10000
  Should contain metadata value  ${metadata}  cdmi_geographic_placement_provided  IT
  Should have metadata value  ${metadata}  cdmi_data_storage_lifetime_provided  P20Y
  Should have metadata value  ${metadata}  cdmi_durability_provided  99.999
  Should contain metadata value  ${metadata}  cdmi_capabilities_allowed_provided  /cdmi_capabilities/dataobject/DiskAndTape

Check Container DiskOnly Capability  [Arguments]  ${data}
  Should Be Equal  ${data["objectName"]}  DiskOnly
  Check DiskOnly metadata values  ${data["metadata"]}
  Check container capabilities  ${data["capabilities"]}
  Should Be Equal  ${data["parentURI"]}  /cdmi_capabilities/container
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Check Dataobject DiskOnly Capability  [Arguments]  ${data}
  Should Be Equal  ${data["objectName"]}  DiskOnly
  Check DiskOnly metadata values  ${data["metadata"]}
  Check dataobject capabilities  ${data["capabilities"]}
  Should Be Equal  ${data["parentURI"]}  /cdmi_capabilities/dataobject
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Check Dataobject DiskOnly Metadata  [Arguments]  ${data}  ${parent}  ${filename}
  Should Be Equal  ${data["objectName"]}  ${filename}
  Check DiskOnly provided metadata values  ${data["metadata"]}
  Should Be Equal  ${data["capabilitiesURI"]}  /cdmi_capabilities/dataobject/DiskOnly
  Should Be Equal  ${data["parentURI"]}  ${parent}
  Should Be Equal  ${data["objectType"]}  application/cdmi-object

Check Dataobject DiskAndTape Capability  [Arguments]  ${data}
  Should Be Equal  ${data["objectName"]}  DiskAndTape
  Check DiskAndTape metadata values  ${data["metadata"]}
  Check dataobject capabilities  ${data["capabilities"]}
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Check Dataobject DiskAndTape Metadata  [Arguments]  ${data}  ${parent}  ${filename}
  Should Be Equal  ${data["objectName"]}  ${filename}
  Check DiskAndTape provided metadata values  ${data["metadata"]}
  Should Be Equal  ${data["capabilitiesURI"]}  /cdmi_capabilities/dataobject/DiskAndTape
  Should Be Equal  ${data["parentURI"]}  ${parent}
  Should Be Equal  ${data["objectType"]}  application/cdmi-object

Check Dataobject TapeOnly Capability  [Arguments]  ${data}
  Should Be Equal  ${data["objectName"]}  TapeOnly
  Check TapeOnly metadata values  ${data["metadata"]}
  Check dataobject capabilities  ${data["capabilities"]}
  Should Be Equal  ${data["objectType"]}  application/cdmi-capability

Check Dataobject TapeOnly Metadata  [Arguments]  ${data}  ${parent}  ${filename}
  Should Be Equal  ${data["objectName"]}  ${filename}
  Check TapeOnly provided metadata values  ${data["metadata"]}
  Should Be Equal  ${data["capabilitiesURI"]}  /cdmi_capabilities/dataobject/TapeOnly
  Should Be Equal  ${data["parentURI"]}  ${parent}
  Should Be Equal  ${data["objectType"]}  application/cdmi-object