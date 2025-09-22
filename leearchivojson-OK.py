
import json
from aplicacionweb1.utils import insertaMysql 

with open('/home/lsuyo/oracle/scan-recipe-cross-20250918.txt', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    datito=fcc_data["data"]["items"]
    for x in datito:
        print( x["id"], x["name"])
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


