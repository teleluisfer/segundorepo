import oci
from datetime import datetime
import os
import subprocess as sp
config = oci.config.from_file()
cloud_guard_client = oci.cloud_guard.CloudGuardClient(config)
list_problems_response = cloud_guard_client.list_problems(
    compartment_id="ocid1.tenancy.oc1..aaaaaaaan3uvkgatj4cca5rmt4hltrx3maiwq63yo7gtsivpmtbfm54albqq",
#    time_last_detected_greater_than_or_equal_to=datetime.strptime( "2039-04-21T14:26:34.461Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
#    time_last_detected_less_than_or_equal_to=datetime.strptime( "2021-12-07T11:08:06.927Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
#    time_first_detected_greater_than_or_equal_to=datetime.strptime( "2033-01-01T10:36:12.421Z", "%Y-%m-%dT%H:%M:%S.%fZ"),
#    time_first_detected_less_than_or_equal_to=datetime.strptime( "2025-09-09T06:14:41.409Z","%Y-%m-%dT%H:%M:%S.%fZ"),
#    lifecycle_detail="RESOLVED",
#    lifecycle_state="ACTIVE",
    region="sa-saopaulo-1",
   # risk_level="CRITICAL",
#    resource_type="EXAMPLE-resourceType-Value",
#    city="EXAMPLE-city-Value",
#    state="EXAMPLE-state-Value",
#    country="EXAMPLE-country-Value",
#    label="EXAMPLE-label-Value",
#    detector_rule_id_list=["EXAMPLE--Value"],
#    detector_type="IAAS_INSTANCE_SECURITY_DETECTOR",
# 'IAAS_ACTIVITY_DETECTOR', 'IAAS_CONFIGURATION_DETECTOR', 'IAAS_THREAT_DETECTOR', 'IAAS_LOG_INSIGHT_DETECTOR', 'IAAS_INSTANCE_SECURITY_DETECTOR', 'IAAS_CONTAINER_SECURITY_DETECTOR'
#     detector_type="IAAS_CONFIGURATION_DETECTOR",
    detector_type="IAAS_ACTIVITY_DETECTOR",
#    target_id="ocid1.test.oc1..<unique_ID>EXAMPLE-targetId-Value",
#    target_id="ocid1.compartment.oc1..aaaaaaaa3drricpqotqm7htfnwlf4bm7k2smksj7jrkxxtrsjjruh2cbakga",
#    problem_category="SECURITY_ZONE",
#    compartment_id_in_subtree=False,
    compartment_id_in_subtree=True,
#    access_level="RESTRICTED",
    access_level="ACCESSIBLE",
 #   resource_id="ocid1.test.oc1..<unique_ID>EXAMPLE-resourceId-Value",
   limit=1000,
 #   page="EXAMPLE-page-Value",
    sort_order="DESC",
    sort_by="riskLevel",
 #   opc_request_id="82QLUSYWTKTKCSZRYIB4<unique_ID>")
    )

# Get the data from response
#print(list_problems_response.data)
y=0;
linea0="compartment_id;detector_id;detector_rule_id;id;labels0;lifecycle_detail;lifecycle_state;locks;region;resource_id;resource_name;resource_type;risk_level;risk_score;target_id;time_first_detected;time_last_detected;comment;description;recommendation"
#print(linea0)
for x in list_problems_response.data.items:
    y=y+1
    cmd="python3 GetProblem2.py "+x.id
    output = sp.getoutput(cmd)

    #print(x.id,":    ",x.detector_id)
    #linea=str(x.compartment_id+","+x.detector_id+","+x.detector_rule_id+","+x.id+","+x.labels+","+x.lifecycle_detail+","+x.lifecycle_state+","+x.locks+","+x.region+","+x.regions+","+x.resource_id+","+x.resource_name+","+x.resource_type+","+x.risk_level+","+x.risk_score+","+x.target_id+",´"+x.time_first_detected+","+x.time_last_detected)
    linea=str(x.compartment_id)+";"+str(x.detector_id)+";"+str(x.detector_rule_id)+";"+str(x.id)+";"+str(x.labels[0])+";"+str(x.lifecycle_detail)+";"+str(x.lifecycle_state)+";"+str(x.locks)+";"+str(x.region)+";"+str(x.resource_id)+";"+str(x.resource_name)+";"+str(x.resource_type)+";"+str(x.risk_level)+";"+str(x.risk_score)+";"+str(x.target_id)+";"+str(x.time_first_detected)+";"+str(x.time_last_detected)+";"+output
    #linea=linea+";"+output
    print(linea)

#print("total:",y);

