import mysql.connector
import json
import os
import sys
from conexionMysql import insertaMysqlDetalleVulnerabilidad 

#cmd = "python3  GetProblem2.py  ocid1.cloudguardproblem.oc1.sa-saopaulo-1.amaaaaaanla7rtcqy5gfuvv636cayo7vmurojcowudyuu6nfeo2ymlhrfmgq"
#cmd2 = "oci vulnerability-scanning vulnerability get  --vulnerability-id "
#r=os.system(cmd)

idvfile=sys.argv[1]

with open("/home/lsuyo/oracle/resultados-leearchivoVulnerabilidades/"+idvfile, 'r') as fcc_file:
#with open('/home/lsuyo/oracle/resultados-leearchivoVulnerabilidades/vulnerabilidad130.txt', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    #datito=fcc_data["data"]["items"]
    datito=fcc_data["data"]
    #print(datito["authentication"],"|",datito["compartment-id"],"|",datito["name"],"|",datito["severity"],"|",datito["cve-details"]["cve-reference"],"|",datito["cve-details"]["cvss3"])
    y=0
    insertaMysqlDetalleVulnerabilidad(
            datito["authentication"],
            datito["compartment-id"],
            datito["cve-description"],
            datito["cve-details"]["cve-reference"],
            datito["cve-details"]["cvss3"],
            datito["cve-details"]["description"],
            datito["cve-details"]["exploitable"],
            datito["cve-details"]["impact"],
            datito["cve-details"]["patchable"],
            datito["cve-details"]["reference-url"],
            datito["cve-details"]["related-cve-reference"],
            datito["cve-details"]["solution"],
            datito["cve-details"]["threat"],
            datito["cve-details"]["time-published"],
            datito["cve-details"]["time-updated"],
            datito["cve-details"]["title"],
            datito["id"],
            datito["impacted-resources-count"]["host-count"],
            datito["impacted-resources-count"]["image-count"],
            datito["lifecycle-state"],
            datito["name"],
            datito["severity"],
            datito["state"],
            datito["time-first-detected"],
            datito["time-last-detected"],
            datito["vulnerability-reference"],
            datito["vulnerability-type"]
    )

    '''
    for x in datito:
        print( x.authentication, x.compartment-id)
        #file =  "vulnerabilidad"+str(y);
        #comando = cmd2 + x["id"] + " > resultados-leearchivoVulnerabilidades/"+file+".txt"
        #print(comando)
        #r=os.system(comando)
        y=y+1
        #print(cmd2 , x["id"])
        
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

