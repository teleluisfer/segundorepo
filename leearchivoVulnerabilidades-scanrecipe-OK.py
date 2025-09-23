import json
import os
from django.conf import settings
from conexionMysql import insertaScanRecipe
from conexionMysql import insertaGraficaVulnerabilidades


#cmd = "python3  GetProblem2.py  ocid1.cloudguardproblem.oc1.sa-saopaulo-1.amaaaaaanla7rtcqy5gfuvv636cayo7vmurojcowudyuu6nfeo2ymlhrfmgq"
#cmd2 = "oci vulnerability-scanning vulnerability get  --vulnerability-id "
#r=os.system(cmd)
#with open('/home/lsuyo/oracle/scan-recipe-cross-20250918.txt', 'r') as fcc_file:
with open('/home/lsuyo/oracle/scan-recipe-cross-20250922.txt', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    datito=fcc_data["data"]["items"]
    y=0
    low=0
    medium=0
    critical=0
    high=0
    none=0
    for x in datito:
        #print( x["id"], x["name"])
        #file =  "vulnerabilidad"+str(y);
        #comando = cmd2 + x["id"] + " > resultados-leearchivoVulnerabilidades20250922/"+file+".txt"
        #print(comando)
        #r=os.system(comando)
        y=y+1
        print(" van ",y," registros...")
        #print(cmd2 , x["id"])
        match(x["severity"]):
            case 'HIGH':
                high=high+1          
            case 'MEDIUM':
                medium=medium+1
            case 'CRITICAL':
                critical=critical+1
            case 'LOW':
                low=low+1
            case 'NONE':
                none=none+1
        
        insertaScanRecipe(
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

    insertaGraficaVulnerabilidades('LOW',low)    
    insertaGraficaVulnerabilidades('NONE',none) 
    insertaGraficaVulnerabilidades('MEDIUM',medium) 
    insertaGraficaVulnerabilidades('HIGH',high) 
    insertaGraficaVulnerabilidades('CRITICAL',critical) 

