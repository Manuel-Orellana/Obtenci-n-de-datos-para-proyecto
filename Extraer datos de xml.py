import xml.etree.ElementTree as ET #sirve para leer archivos XML.
import pandas as pd

#Leer el XML
tree = ET.parse("DI_export_ecu/DI_export_ecu.xml") #representa todo el documento.
root = tree.getroot() #representa la raíz

for seccion in root: #Recorrer cada sección

    registros = seccion.findall("TR") #Buscar todos los registros

    if not registros: #Ignorar secciones vacías
        continue

    datos = [] #Lista donde se guardarán todas las filas

    for tr in registros: #Recorrer cada registro
        fila = {} #Crear un diccionario vacío

        for campo in tr: #Recorrer todos los campos
            fila[campo.tag] = campo.text #Guardar el nombre y el contenido

        datos.append(fila) #Agregar la fila a la lista

    df = pd.DataFrame(datos) #Crear el DataFrame en base a el diccionario

    nombre = f"{seccion.tag}.csv" #Crear el nombre del archivo
    df.to_csv(nombre, index=False, encoding="utf-8-sig")#Guardar el CSV

    print(f"{nombre}: {len(df)} filas") #Mostrar cuántas filas se exportaron