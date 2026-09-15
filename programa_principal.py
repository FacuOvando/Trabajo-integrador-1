import json
import sys
import modulo_de_validaciones

# variables y contador donde guardar los datos

registros_validos = [] 
registros_invalidos = [] 
leidas_totales = 0 

# control de argumentos en la terminal para que solo haya 2 archivos, uno de entrada y otro de salida

if len(sys.argv) != 3:
    print("error en el uso de argumentos")
    print("uso correcto de los argumentos")
    sys.exit()

archivo_entrada = sys.argv[1]
archivo_salida = sys.argv[2]

# se lee el archivo de txt 

try:
    with open (archivo_entrada, "r") as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    print(f"no se encontro el archivo requerido en la entrada: {archivo_entrada}")
    sys.exit()

# se reccore y valida linea por linea

for linea in lineas[1:]: # se usa el [1:] para saltar los encabezados y leer solo los datos
    linea_limpia = linea.strip()

    if not linea_limpia:
        continue

    leidas_totales += 1

# se separan los datos por ;

    zonas = linea_limpia.split()

# se valida que esten 7 zonas de datos como minimo

    if len(zonas) < 8:
        registros_invalidos.append({
            "linea original": linea_limpia,
            "motivo": "cantidad no suficiente de zonas"
        })
        continue

# se sacan los datos de forma individual para almacernarlos en variables

    fecha = zonas[0]
    hora = zonas[1]
    temperatura = zonas[2]
    humedad = zonas[3]
    presion = zonas[4]
    dir_viento = zonas[5]
    veloci_viento = zonas[6]
    estacion = zonas[7]

    estacion = " ".join(zonas[7:]) 

    error = None

# se utlizan las validaciones

    if not modulo_de_validaciones.validar_fecha(fecha):
        error = "fecha imvalida o inposible"
    elif not modulo_de_validaciones.validar_hora(hora):
        error = "hora invalida o imposible"
    elif not modulo_de_validaciones.validar_el_flotante(temperatura):
        error = "temperatura no numerica"
    elif not modulo_de_validaciones.validar_humedad(humedad):
        error = "humedad imposible"
    elif not modulo_de_validaciones.validar_presion(presion):
        error = "presion no numerica"
    elif not modulo_de_validaciones.validar_dirrecion_viento(dir_viento):
        error = "direccion del viento imposible"
    elif not modulo_de_validaciones.validar_veloci_viento(veloci_viento):
        error = "velocidad negativa o imposible"
    elif not modulo_de_validaciones.validar_estacion(estacion):
        error = "nombre de estacion vacio"

# segun los datos se almacena dependiendo su resultado

    if error: 
        registros_invalidos.append({
            "linea original": linea_limpia,
            "motivo": error
        })

# se transforman los datos a su tipo correcto

    else:
        registros_validos.append({

            "fecha": int(fecha),
            "hora": int(hora),
            "temperatura": float(temperatura),
            "humedad": float(humedad),
            "presion": float(presion),
            "viento_dir": float(dir_viento),
            "velo_viento": float(veloci_viento),
            "estacion": estacion.strip()
        })

# se arma la estructura para el formato json

formato_json ={
    "resumen_del_proceso": {
        "total_leidas": leidas_totales,
        "total_validas": len(registros_validos),
        "total_invalidas": len(registros_invalidos)
    },
    "registros_validos": registros_validos,
    "registros_invalidos": registros_invalidos
}

# se escribe el archivo en formato json 

with open(archivo_salida, "w") as archivo_json:
    json.dump(formato_json, archivo_json, indent=2)

# se muestran los resultados en la terminal

print("\nproceso terminado")
print(f"total de lineas leidas: {leidas_totales}")
print(f"archivos validos guardados: {len(registros_validos)}")
print(f"archivos invalidos guardados: {len(registros_invalidos)}")