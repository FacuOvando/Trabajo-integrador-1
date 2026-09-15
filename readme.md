Trabajo Práctico Integrador 1 Parte 1
Conversor de Archivos: TXT a JSON

este proyecto consiste en un programa en python que se encarga de automatizar ,filtrar y validar datos provenientes del servicio meteorologico nacional (SNM)

el programa se encarga de: leer un archivo de txt plano con los datos del SMN separado por espacios, filtrar los encabezados y lineas vacias, valida los datos y crear un reporte ordenado y limpio en formato json

Integrantes del Grupo:
    Facundo Ovando
    Nazareno Elissanburu

Estructura del Proyecto:
    el programa fue dividido en 2 modulos independientes:
        1. modulo_de_validaciones.py: contiene definiciones para funciones que tienen el fin de verificar, transformar y validar los datos de txt
        2. programa_principal.py: programa encargado de manejar los argumentos en la terminal, leer el archivo de txt como entrada y escribir una lista ordenada en formato json como salida

Requisitos y Preparación:
    el programa utiliza librearias nativas de python, por lo tanto no hay necesidad de utilizar un entorno virtual

asegurese de tener estos archivos en la misma carpeta antes de ejecutar
    1. modulo_de_validaciones.py
    2. adaptar_datos.py`
    3. Un archivo de texto de entrada con los datos meteorológicos

Comandos de Ejecución
    el programa se ejecuta a traves de la terminal de comandos, habiendo que pasar obligatoriamente dos argumentos:
    el archivo de txt de entrada y el archivo ordenado en formato json de salida

por ejemplo:
    python adaptar_datos.py info.txt formato.json

Formato del JSON Generado:
La estructura de salida organiza la información en tres objetos para facilitar la lectura para humanos:

    1. resumen_del_proceso: Contiene un balance general con las cantidades de líneas procesadas de forma exitosa y errónea.
    2. registros_validos: Lista de objetos meteorológicos limpios, mapeados con claves estándar y con sus zonas correctamente transformados a tipos de datos numéricos enteros (int) y decimales (float)
    3. registros_invalidos: Lista de objetos que conserva el contenido exacto de la línea original que falló y adjunta un mensaje breve explicando la razón o el filtro que no logró superar