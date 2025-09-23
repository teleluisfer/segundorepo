import mysql.connector
import json
from django.conf import settings



def insertaMysqlDetalleVulnerabilidad(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27):
#    db = mysql.connector.connect(user='root', password='lsuy0', host='192.168.1.178', database='orion', auth_plugin='mysql_native_password')
    db = mysql.connector.connect(user='root', password='lsuy0', host=settings.GLOBAL_VARIABLE_IP, database='orion', auth_plugin='mysql_native_password')
    cursor = db.cursor()
    sql = "INSERT INTO aplicacionweb1_detallevulnerabilidad ( authentication,compartment_id,cve_description, cve_reference, cvss3,description,exploitable,impact,patchable,reference_url,related_cve_reference,solution,threat,time_published,time_updated,title,idvulnerabilidad,impacted_resources_host_count,impacted_resources_image_count,lifecycle_state,name,severity,state,time_first_detected,time_last_detected,vulnerability_reference,vulnerability_type) VALUES (%s, %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s )"
    values = (var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27)
    cursor.execute(sql, values)
    db.commit()
    print(cursor.rowcount, "record inserted.")
