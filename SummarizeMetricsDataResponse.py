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
monitoring_client = oci.monitoring.MonitoringClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
summarize_metrics_data_response = monitoring_client.summarize_metrics_data(
    compartment_id="ocid1.tenancy.oc1..aaaaaaaan3uvkgatj4cca5rmt4hltrx3maiwq63yo7gtsivpmtbfm54albqq",
    summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
        #namespace="EXAMPLE-namespace-Value",
        #query="EXAMPLE-query-Value",
        #resource_group="EXAMPLE-resourceGroup-Value",
        start_time=datetime.strptime(
            "2024-08-08T12:50:27.545Z",
            "%Y-%m-%dT%H:%M:%S.%fZ"),
        end_time=datetime.strptime(
            "2032-05-24T09:36:44.528Z",
            "%Y-%m-%dT%H:%M:%S.%fZ"),
        #resolution="EXAMPLE-resolution-Value"),
        #opc_request_id="O6CMJ2GYPATJ1STYBRSP<unique_ID>",
        #compartment_id_in_subtree=True)
        )

    )
# Get the data from response
print(summarize_metrics_data_response.data)
