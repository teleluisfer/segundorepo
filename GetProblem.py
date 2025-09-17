# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci
import sys
import json
import pandas as pd

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file()


# Initialize service client with default config file
cloud_guard_client = oci.cloud_guard.CloudGuardClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
get_problem_response = cloud_guard_client.get_problem(
    problem_id=sys.argv[1],
    #problem_id="ocid1.cloudguardproblem.oc1.sa-saopaulo-1.amaaaaaanla7rtcqy5gfuvv636cayo7vmurojcowudyuu6nfeo2ymlhrfmgq",
#   opc_request_id="WJEQYZXU8AYSDRMGIUTZ<unique_ID>")
    )

# Get the data from response
print(get_problem_response.data)


#primera="DESCRIPCION;DETECTOR_ID;DETECTOR_RULE_ID;";
#linea=x.description+";"+x.detector_id+";"+x.detector_rule_id+";"+x.lifecycle_detail+";"+x.lifecycle_state+";"+x.peak_risk_score_lookup_period_in_days+";"+x.recommendation+";"+x.region+";"+x.resource_id+";"+x.resource_name+";"+x.resource_type+";"+x.risk_level+";"+x.risk_score+";"+x.target_id+";"+x.time_first_detected+";"+x.time_last_detected

#data = json.loads(get_problem_response.data)
#datosDump = json.dumps(get_problem_response.data)
#datosJson = json.loads(datosDump)

#df = pd.json_normalize(get_problem_response.data)
#csv_data = df.to_csv(index=False)
#print(csv_data)

#for x in datosJson:
#for x in get_problem_response.data:
    #linea=x.description+";"+x.detector_id+";"+x.detector_rule_id+";"+x.lifecycle_detail+";"+x.lifecycle_state+";"+x.peak_risk_score_lookup_period_in_days+";"+x.recommendation+";"+x.region+";"+x.resource_id+";"+x.resource_name+";"+x.resource_type+";"+x.risk_level+";"+x.risk_score+";"+x.target_id+";"+x.time_first_detected+";"+x.time_last_detected
    #print(linea)
    #print(x.name,"-----",x.description)
    #name = data['description']
    #age = data['detector_id']
    #city = data['labels'][0]
    #zipc = data['labels'][0]
#    name = datosJson['description']
#    age  = datosJson['detector_id']
#    city = datosJson['labels'][0]
#    zipc = datosJson['labels'][0]

#print(f"Name: {name}")
#print(f"Age: {age}")
#print(f"City: {city}")
#print(f"Zipcode: {zipc}")



