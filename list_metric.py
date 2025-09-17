#!/usr/bin/python3

# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing EXAMPLE or unique_id, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
monitoring_client = oci.monitoring.MonitoringClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
list_metrics_response = monitoring_client.list_metrics(
    compartment_id="ocid1.tenancy.oc1..aaaaaaaan3uvkgatj4cca5rmt4hltrx3maiwq63yo7gtsivpmtbfm54albqq",
    list_metrics_details=oci.monitoring.models.ListMetricsDetails(
        name="<YOUR METRIC NAME>",
        namespace="<YOUR CUSTOM NAMESPACE>"))


# Get the data from response
print(list_metrics_response.data)
