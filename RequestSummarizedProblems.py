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
cloud_guard_client = oci.cloud_guard.CloudGuardClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
request_summarized_problems_response = cloud_guard_client.request_summarized_problems(
    list_dimensions=["DETECTOR_ID","RISK_LEVEL","REGION"],
    compartment_id="ocid1.tenancy.oc1..aaaaaaaan3uvkgatj4cca5rmt4hltrx3maiwq63yo7gtsivpmtbfm54albqq",
    compartment_id_in_subtree=True,
    access_level="ACCESSIBLE",
    limit=927,
#    page="EXAMPLE-page-Value",
#    opc_request_id="QAHAN9HWDGOO4OXAYCH3<unique_ID>")
    )

# Get the data from response
print(request_summarized_problems_response.data)
