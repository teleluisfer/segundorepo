import json
import numpy as np
import pandas as pd
from io import StringIO
pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

json_data = {
  "additional_details": {},
  "auto_resolve_date": "null",
  "comment": "",
  "compartment_id": "ocid1.compartment.oc1..aaaaaaaa5vohp4uuai7w5agkj6k33kj3kixnnkgrdrq2wj5z7jkzzjkr4jfa",
  "description": "Object Storage supports anonymous, unauthenticated access to a bucket. A public bucket that has read access enabled for anonymous users allows anyone to obtain object metadata, download bucket objects, and optionally list bucket contents.",
  "detector_id": "IAAS_CONFIGURATION_DETECTOR",
  "detector_rule_id": "BUCKET_IS_PUBLIC",
  "id": "ocid1.cloudguardproblem.oc1.sa-saopaulo-1.amaaaaaanla7rtcqy5gfuvv636cayo7vmurojcowudyuu6nfeo2ymlhrfmgq",
  "impacted_resource_id": "null",
  "impacted_resource_name": "null",
  "impacted_resource_type": "null",
  "labels": [
    "CIS_OCI_V1.1_OBJECTSTORAGE",
    "ObjectStorage",
    "CIS_OCI_V_2.0.0"
  ],
  "lifecycle_detail": "OPEN",
  "lifecycle_state": "ACTIVE",
  "locks": "null",
  "peak_risk_score": "null",
  "peak_risk_score_date": "null",
  "peak_risk_score_lookup_period_in_days": 14,
  "recommendation": "Ensure that the bucket is sanctioned for public access, and if not, direct the OCI administrator to restrict the bucket policy to allow only specific users access to the resources required to accomplish their job functions.",
  "region": "sa-saopaulo-1",
  "regions": [
    "sa-saopaulo-1"
  ],
  "resource_id": "axzwiir8h5ec/COM-SYN-PRO-BOS-OCI1-001",
  "resource_name": "COM-SYN-PRO-BOS-OCI1-001",
  "resource_type": "Bucket",
  "risk_level": "CRITICAL",
  "risk_score": "null",
  "target_id": "ocid1.cloudguardtarget.oc1.sa-saopaulo-1.amaaaaaanla7rtaajb2il27ksdnroig647dl76zahnhazxbh5jpf2mcjhp7a",
  "time_first_detected": "2025-06-09T22:04:17.665000+00:00",
  "time_last_detected": "2025-09-12T18:25:35.872000+00:00"
}

#data = json.loads(n_json)

#name  = data['description']
#age   = data['detector_id']
#age2  = data['detector_rule_id']
#city  = data['labels'][0]
#zipc  = data['labels'][1]

#print(f"Name: {name}")
#print(f"Age: {age}")
#print(f"Age2: {age2}")
#print(f"City: {city}")
#print(f"Zipcode: {zipc}")

#df = pd.json_normalize(
#    json_data,
#    #record_path=['employees', 'positions'],
#    record_path=['labels'],
#    meta=[
#        ['labels'],
#        ['labels']
#    ]
#)
df = pd.json_normalize(json_data)
#print(df)

df = pd.json_normalize(json_data)
csv_data = df.to_csv(index=False)
print(csv_data)

#print(df)


json_data2 = {
    'company': 'Example Corp',
    'employees': [
        {
            'id': 1,
            'name': 'John Doe',
            'positions': [
                {'title': 'CEO', 'years': 5},
                {'title': 'CTO', 'years': 3}
            ]
        },
        {
            'id': 2,
            'name': 'Jane Doe',
            'positions': [
                {'title': 'CFO', 'years': 4},
                {'title': 'CMO', 'years': 2}
            ]
        }
    ]
}

