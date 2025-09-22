import os

#print(os.listdir('/home/lsuyo/oracle/resultados-leearchivoVulnerabilidades/'))
#r=os.listdir('/home/lsuyo/oracle/resultados-leearchivoVulnerabilidades/')
r=os.listdir('/home/lsuyo/oracle/resultados-leearchivoVulnerabilidades20250922/')

comando="python  insertaDetallesVulnerabilidades-OK.py "

for x in r:
    cmd=comando+x
    os.system(cmd)
    print(cmd)

