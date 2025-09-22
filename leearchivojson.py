import json
# Abrir el archivo ordenes.json
with open("ordenes.json") as archivo:
    # Cargar su contenido y crear un diccionario
    datos = json.load(archivo)

    # Eliminar el par clave-valor "cliente" de cada orden
    for orden in datos["ordenes"]:
        del orden["cliente"]

# Abir (o crear) un archivo ordenes_nuevo.json 
# y guardar la nueva versión de la información
with open("ordenes_nuevo.json", 'w') as archivo_nuevo:
    json.dump(datos, archivo_nuevo)
