import mysql.connector
import json
from django.conf import settings

def reporteSeleccionado(valor):
    resultado=0
    json1={
            "tenis":"RogerFederer",
            "futbol":"Messi",
            "rock":"Soda Stereo",
            }
    json2={
            "tenis":"Novak Djokovic",
            "futbol":"Cristiano",
            "rock":"Mars",
            }
    json3={
            "tenis":"Alcaraz",
            "futbol":"Yamal",
            "rock":"No hay",
            }
    json4={
            "tenis":"N.A.",
            "futbol":"N.A.",
            "rock":"N.A.",
            }
    if(valor==1):
        resultado=json1
    elif(valor==2):
        resultado=json2
    elif(valor==3):
        resultado=json3
    else:
        resultado=json4
    return resultado

def insertaMysql(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11):
    db = mysql.connector.connect(user='root', password='lsuy0', host=settings.GLOBAL_VARIABLE_IP, database='orion', auth_plugin='mysql_native_password')
    #db = mysql.connector.connect(user='root', password='lsuy0', host='192.168.1.178', database='orion', auth_plugin='mysql_native_password')
    #db = mysql.connector.connect(user='root', password='lsuy0', host='10.221.93.147', database='orion', auth_plugin='mysql_native_password')
    cursor = db.cursor()
    #sql = "INSERT INTO host_vulnerability_list (compartment_id,cve_reference,host_count,idv,lifecycle_state,name_cve,severity,state,time_first_detected,time_last_detected,vulnerability_type) VALUES (%s, %s ,%s ,%s, %s ,%s ,%s, %s, %s ,%s, %s)"
    sql = "INSERT INTO aplicacionweb1_consulta1 (compartment_id,cve_reference,host_count,idv,lifecycle_state,name_cve,severity,state,time_first_detected,time_last_detected,vulnerability_type) VALUES (%s, %s ,%s ,%s, %s ,%s ,%s, %s, %s ,%s, %s)"
    values = ( var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11)
    cursor.execute(sql, values)
    db.commit()
    print(cursor.rowcount, "record inserted.")

def insertaMysqlDetalleVulnerabilidad(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27):
    db = mysql.connector.connect(user='root', password='lsuy0', host=settings.GLOBAL_VARIABLE_IP, database='orion', auth_plugin='mysql_native_password')
    #db = mysql.connector.connect(user='root', password='lsuy0', host='10.221.93.147', database='orion', auth_plugin='mysql_native_password')
    cursor = db.cursor()
    sql = "INSERT INTO aplicacionweb1_detallevulnerabilidad ( authentication,compartment_id,cve_description, cve_reference, cvss3,description,exploitable,impact,patchable,reference_url,related_cve_reference,solution,threat,time_published,time_updated,title,idvulnerabilidad,impacted_resources_host_count,impacted_resources_image_count,lifecycle_state,name,severity,state,time_first_detected,time_last_detected,vulnerability_reference,vulnerability_type) VALUES (%s, %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s )"
    values = (var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27)
    cursor.execute(sql, values)
    db.commit()
    print(cursor.rowcount, "record inserted.")

def leeMysql():
    #db = mysql.connector.connect(user='root', password='lsuy0', host='10.221.93.147', database='orion', auth_plugin='mysql_native_password')
    db = mysql.connector.connect(user='root', password='lsuy0', host=settings.GLOBAL_VARIABLE_IP, database='orion', auth_plugin='mysql_native_password')
    cursor = db.cursor()
    cursor.execute("select * from host_vulnerability_list")
    myresult = cursor.fetchall()
    y={}
    for x in myresult:
        #fila=x[y]
        #fila.split(',')
        y["compartment_id"]=x[0]
        y["cve_reference"]=x[1]
        y["host_count"]=x[2]
        y["idv"]=x[3]
        y["lifecycle_state"]=x[4]
        y["name_cve"]=x[5]
        y["severity"]=x[6]
        y["state"]=x[7]
        y["time_first_detected"]=x[8]
        y["time_last_detected"]=x[9]
        y["vulnerability_type"]=x[10]
        #print(x[0])
        #y=y+1
    #    print(x)
    json_result = json.dumps(y)
    #print(json_result)
    return json_result
    # Fetch all rows and convert to a list of dictionaries


    #rows = cursor.fetchall()
    #result = []
    #for row in rows:
    #    d = {}
    #    for i, col in enumerate(cursor.description):
    #        d[col[0]] = row[i]
    #        result.append(d)

    ## Convert the list of dictionaries to JSON and print it
    #json_result = json.dumps(result)
    ##print(json_result)
    #return json_result




