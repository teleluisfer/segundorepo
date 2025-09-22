# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

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
get_host_port_scan_result_response = vulnerability_scanning_client.get_host_port_scan_result(
    host_port_scan_result_id="ocid1.vsshostscanrecipe.oc1.sa-saopaulo-1.aaaaaaaaryx6gdht5vkcx4cg6hur75r4zln4pndnpd3uu62qxr573pvi5g6q",
    opc_request_id="")

# Get the data from response
print(get_host_port_scan_result_response.data)
