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
vulnerability_scanning_client = oci.vulnerability_scanning.VulnerabilityScanningClient(
    config)


# Send the request to service, some parameters are not required, see API
# doc for more info
list_host_agent_scan_results_response = vulnerability_scanning_client.list_host_agent_scan_results(
    compartment_id="ocid1.compartment.oc1..aaaaaaaa4fyiek2wytf6acqublcnqbum3j6pekx2u4nivcsgpof2hkmkvapq",
#    instance_id="ocid1.test.oc1..<unique_ID>EXAMPLE-instanceId-Value",
#    highest_problem_severity="HIGH",
#    operating_system="EXAMPLE-operatingSystem-Value",
#    time_started_greater_than_or_equal_to=datetime.strptime(        "2048-05-10T02:29:56.329Z",        "%Y-%m-%dT%H:%M:%S.%fZ"),
#    time_started_less_than_or_equal_to=datetime.strptime(       "2030-08-10T18:50:19.216Z",        "%Y-%m-%dT%H:%M:%S.%fZ"),
    sort_order="DESC",
    sort_by="problemCount",
    limit=289,
#    page="EXAMPLE-page-Value",
#    opc_request_id="ZUNUKV3MK2CT4MZQQRTZ<unique_ID>",
#    display_name="EXAMPLE-displayName-Value",
#    is_latest_only=False)
)

# Get the data from response
print(list_host_agent_scan_results_response.data)
