
import json
import os
from aplicacionweb1.utils import insertaMysql 

#cmd = "python3  GetProblem2.py  ocid1.cloudguardproblem.oc1.sa-saopaulo-1.amaaaaaanla7rtcqy5gfuvv636cayo7vmurojcowudyuu6nfeo2ymlhrfmgq"
cmd2 = "oci vulnerability-scanning vulnerability get  --vulnerability-id "
#r=os.system(cmd)

with open('/home/lsuyo/oracle/scan-recipe-cross-20250918.txt', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    datito=fcc_data["data"]["items"]
    for x in datito:
        #print( x["id"], x["name"])
        comando = cmd2 + x["id"]
        r=os.system(comando)
        #print(cmd2 , x["id"])
        '''
        insertaMysql(
                x["compartment-id"],
                x["cve-reference"],
                x["host-count"],
                x["id"],
                x["lifecycle-state"],
                x["name"],
                x["severity"],
                x["state"],
                x["time-first-detected"],
                x["time-last-detected"],
                x["vulnerability-type"]
                )

        '''

