# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
from datetime import datetime

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
cloud_guard_client = oci.cloud_guard.CloudGuardClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
list_problems_response = cloud_guard_client.list_problems(
    compartment_id="ocid1.tenancy.oc1..aaaaaaaan3uvkgatj4cca5rmt4hltrx3maiwq63yo7gtsivpmtbfm54albqq",
#    time_last_detected_greater_than_or_equal_to=datetime.strptime( "2039-04-21T14:26:34.461Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
#    time_last_detected_less_than_or_equal_to=datetime.strptime( "2021-12-07T11:08:06.927Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
#    time_first_detected_greater_than_or_equal_to=datetime.strptime( "2033-01-01T10:36:12.421Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
#    time_first_detected_less_than_or_equal_to=datetime.strptime( "2025-09-09T06:14:41.409Z","%Y-%m-%dT%H:%M:%S.%fZ"),
#    lifecycle_detail="RESOLVED",
#    lifecycle_state="ACTIVE",
    region="sa-saopaulo-1",
#    risk_level="CRITICAL",
#    resource_type="EXAMPLE-resourceType-Value",
#    city="EXAMPLE-city-Value",
#    state="EXAMPLE-state-Value",
#    country="EXAMPLE-country-Value",
#    label="EXAMPLE-label-Value",
#    detector_rule_id_list=["EXAMPLE--Value"],
#    detector_type="IAAS_INSTANCE_SECURITY_DETECTOR",
# 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR', 'IAAS_INSTANCE_SECURITY_DETECTOR', 'IAAS_CONTAINER_SECURITY_DETECTOR'
#    detector_type="IAAS_ACTIVITY_DETECTOR",
    detector_type="IAAS_CONFIGURATION_DETECTOR",
#    detector_type="IAAS_CONFIGURATION_DETECTOR",
#    target_id="ocid1.test.oc1..<unique_ID>EXAMPLE-targetId-Value",
#    target_id="ocid1.compartment.oc1..aaaaaaaa3drricpqotqm7htfnwlf4bm7k2smksj7jrkxxtrsjjruh2cbakga",
#    problem_category="SECURITY_ZONE",
#    compartment_id_in_subtree=False,
    compartment_id_in_subtree=True,
#    access_level="RESTRICTED",
    access_level="ACCESSIBLE",
 #   resource_id="ocid1.test.oc1..<unique_ID>EXAMPLE-resourceId-Value",
   limit=426,
 #   page="EXAMPLE-page-Value",
    sort_order="DESC",
    sort_by="riskLevel",
 #   opc_request_id="82QLUSYWTKTKCSZRYIB4<unique_ID>")
    )

# Get the data from response
#print(list_problems_response.data)
y=0;
for x in list_problems_response.data.items:
    y=y+1;
    #print(x.id,":    ",x.detector_id)
    print(x.id)

#print("total:",y);

