# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
from datetime import datetime
from collections import namedtuple

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
vulnerability_scanning_client = oci.vulnerability_scanning.VulnerabilityScanningClient(config)

# Send the request to service, some parameters are not required, see API
# doc for more info
list_host_port_scan_results_response = vulnerability_scanning_client.list_host_port_scan_results(
    compartment_id="ocid1.tenancy.oc1..aaaaaaaan3uvkgatj4cca5rmt4hltrx3maiwq63yo7gtsivpmtbfm54albqq",
#    instance_id="ocid1.test.oc1..<unique_ID>EXAMPLE-instanceId-Value",
#    highest_problem_severity="HIGH",
#    time_started_greater_than_or_equal_to=datetime.strptime("2012-12-31T16:09:12.418Z","%Y-%m-%dT%H:%M:%S.%fZ"),
#    time_started_less_than_or_equal_to=datetime.strptime("2001-09-13T00:10:39.197Z","%Y-%m-%dT%H:%M:%S.%fZ"),
    sort_order="DESC",
    sort_by="openPortCount",
#    limit=546,
#    page="EXAMPLE-page-Value",
#    opc_request_id="0IWKTODEZDHNXSVQSJX6<unique_ID>",
#    display_name="EXAMPLE-displayName-Value",
    is_latest_only=True)

# Get the data from response
print(list_host_port_scan_results_response.data)

##print(list_host_port_scan_results_response.data.items)
#listEscaneo.append(list_host_port_scan_results_response.data)
#for x in list_host_port_scan_results_response.data.items:
#    print(x.id,":    ",x.open_port_count)
#tcl = type(namedtuple("llavesita",list_host_port_scan_results_response.data))
#print("tipo de objeto de list_host_port_scan_results_response:",tcl)







#for x in list_host_port_scan_results_response.data.items:
#    print(x.id,":    ",x.open_port_count)

