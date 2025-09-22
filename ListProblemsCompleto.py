import oci
from datetime import datetime
import os
import subprocess as sp
config = oci.config.from_file()
cloud_guard_client = oci.cloud_guard.CloudGuardClient(config)

list_problems_response1 = cloud_guard_client.list_problems(
    compartment_id="ocid1.tenancy.oc1..aaaaaaaan3uvkgatj4cca5rmt4hltrx3maiwq63yo7gtsivpmtbfm54albqq",
    region="sa-saopaulo-1",
#    detector_type="IAAS_ACTIVITY_DETECTOR",
    detector_type="IAAS_CONFIGURATION_DETECTOR",
    compartment_id_in_subtree=True,
#    access_level="RESTRICTED",
    access_level="ACCESSIBLE",
    limit=1000,
    sort_order="DESC",
    sort_by="riskLevel",
    )
list_problems_response2 = cloud_guard_client.list_problems(
    compartment_id="ocid1.tenancy.oc1..aaaaaaaan3uvkgatj4cca5rmt4hltrx3maiwq63yo7gtsivpmtbfm54albqq",
    region="sa-saopaulo-1",
    detector_type="IAAS_ACTIVITY_DETECTOR",
    compartment_id_in_subtree=True,
    access_level="ACCESSIBLE",
    limit=1000,
    sort_order="DESC",
    sort_by="riskLevel",
    )

#print(list_problems_response.data)
y=0;
linea0="compartment_id;detector_id;detector_rule_id;id;labels0;lifecycle_detail;lifecycle_state;locks;region;resource_id;resource_name;resource_type;risk_level;risk_score;target_id;time_first_detected;time_last_detected;comment;description;recommendation"
print(linea0)

for x in list_problems_response1.data.items:
    y=y+1
    cmd="python3 GetProblem2.py "+x.id
    output = sp.getoutput(cmd)
    linea=str(x.compartment_id)+";"+str(x.detector_id)+";"+str(x.detector_rule_id)+";"+str(x.id)+";"+str(x.labels[0])+";"+str(x.lifecycle_detail)+";"+str(x.lifecycle_state)+";"+str(x.locks)+";"+str(x.region)+";"+str(x.resource_id)+";"+str(x.resource_name)+";"+str(x.resource_type)+";"+str(x.risk_level)+";"+str(x.risk_score)+";"+str(x.target_id)+";"+str(x.time_first_detected)+";"+str(x.time_last_detected)+";"+output
    print(linea)

for x in list_problems_response2.data.items:
    y=y+1
    cmd="python3 GetProblem2.py "+x.id
    output = sp.getoutput(cmd)
    linea=str(x.compartment_id)+";"+str(x.detector_id)+";"+str(x.detector_rule_id)+";"+str(x.id)+";"+str(x.labels[0])+";"+str(x.lifecycle_detail)+";"+str(x.lifecycle_state)+";"+str(x.locks)+";"+str(x.region)+";"+str(x.resource_id)+";"+str(x.resource_name)+";"+str(x.resource_type)+";"+str(x.risk_level)+";"+str(x.risk_score)+";"+str(x.target_id)+";"+str(x.time_first_detected)+";"+str(x.time_last_detected)+";"+output
    print(linea)
print("total:",y);

