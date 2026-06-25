import json
from datetime import datetime

CODIFICACION = 'utf-8'
ARCHIVO_LOGS = './18_archivos/logs.txt'

def agregar_si_no_vacio(lista_palabras: list[str], palabra: str) -> bool:
    hubo_cambio = False
    if palabra != '':
        lista_palabras.append(palabra)
        hubo_cambio = True
    return hubo_cambio

def split_texto(texto: str, separador: str) -> list[str]:
    lista_str = []
    palabra = ''

    for caracter in texto:
        if caracter != separador:
            palabra += caracter
        else:
            if agregar_si_no_vacio(lista_str, palabra):
                palabra = ''
    
    agregar_si_no_vacio(lista_str, palabra)
    return lista_str

def join_lista_a_texto(lista_palabras: list[str], separador: str) -> str:
    texto_nuevo = ''
    for elemento in lista_palabras:
        texto_nuevo += f'{elemento}{separador}'

    texto_nuevo = texto_nuevo[:-1]

    return texto_nuevo

def trasponer_matriz(matriz: list[list]) -> list[list]:
    matriz_t = []

    cant_col = len(matriz[0])
    cant_fil = len(matriz)

    for indice_col in range(cant_col):

        nueva_fila = []

        for indice_fila in range(cant_fil):
            elemento = matriz[indice_fila][indice_col]
            nueva_fila.append(elemento)

        matriz_t.append(nueva_fila)
    
    return matriz_t


def guardar_matriz_archivo(matriz_t: list[list], cabecera: list[str],ruta: str):
    with open(ruta, 'w', encoding=CODIFICACION) as archivo:

        lista_texto = []

        headr = join_lista_a_texto(cabecera, ',') + '\n'
        lista_texto.append(headr)

        for fila in matriz_t:
            texto = join_lista_a_texto(fila, ',') + '\n'
            lista_texto.append(texto)

        archivo.writelines(lista_texto)


def extraer_datos_dict(target: list[str], diccionario: dict, separador: str, tipo_dato: str):
    
    if tipo_dato == 'keys':
        datos = list(diccionario.keys())
    else:
        datos = list(diccionario.values())
    headr = join_lista_a_texto(datos, separador) + '\n'
    target.append(headr)

def crear_texto_datos(dataset: list[dict]):
    lista_texto = []
    extraer_datos_dict(lista_texto, dataset[0], ',', 'keys')
    for heroe in dataset:
        extraer_datos_dict(lista_texto, heroe, ',', 'values')
    return lista_texto

def guardar_dataset_dict_archivo(dataset: list[dict], ruta: str):

    with open(ruta, 'w', encoding=CODIFICACION) as file:
        lista_texto = crear_texto_datos(dataset)
        file.writelines(lista_texto)

def parsear_dataset_matriz(datos: list[str]) -> list[list]:
    mi_matriz = []
    for linea in datos:
        if datos.index(linea) == 0:
            continue
        linea = linea.replace('\n', '')
        datos_linea = split_texto(linea, ',')
        mi_matriz.append(datos_linea)
    return mi_matriz

def parsear_dataset_lidict(datos: list[str]) -> list[dict]:
    str_claves_limpias = datos.pop(0).replace('\n', '')
    claves = split_texto(str_claves_limpias, ',')
    lista_dict_heroes = []

    for heroe in datos:
        heroe = heroe.replace('\n', '')
        datos_heroe = split_texto(heroe, ',')
        heroe_dict = {}

        for indice_clave in range(len(claves)):
            heroe_dict.update(
                {claves[indice_clave] : datos_heroe[indice_clave]}
            )
        lista_dict_heroes.append(heroe_dict)
    return lista_dict_heroes



def leer_dataset(ruta: str) ->list[str]:

    
    with open(ruta, 'r', encoding=CODIFICACION) as file:
        contenido = file.readlines()

    return contenido

def guardar_logs(mensaje: str):

    with open(ARCHIVO_LOGS, 'a', encoding=CODIFICACION) as logs:
        logs.write(f'{mensaje}\n')
        print('[SYSTEM]: NUEVO LOG GUARDADO CON EXITO!')

def generar_fecha_actual_str():
    fecha = datetime.now().strftime('%Y/%m/%d, %H:%M:%S')
    return fecha

def escribir_json(ruta: str, informacion: dict):
    with open(ruta, 'w', encoding=CODIFICACION) as json_file:
        json.dump(informacion, json_file, indent=4)
        print(f'[SYSTEM] Archivo creado con exito en: {ruta}')


def leer_json(ruta: str) -> dict:
    informacion = {}
    with open(ruta, 'r', encoding=CODIFICACION) as json_file:
        informacion = json.load(json_file)
        print('[SYSTEM] -- Informacion extraida --')
    return informacion

def es_formato_entero(numero_str: str) -> bool:
    return numero_str.isnumeric()

def es_formato_floatante(numero_str: str) -> bool:
    return numero_str.count('.') == 1

def parseint_numero(numero_str: str) -> int:
    return int(numero_str)

def parsefloat_numero(numero_str: str) -> float:
    return float(numero_str)
    
def tiene_8_caracteres(texto: str) -> bool:
    return len(texto) == 8

def hacer_mayuscula(texto: str) -> str:
    return texto.upper()

def validar_input(mensaje: str,callback_val, callback_parse) -> int | float:
    numero = input(mensaje)

    if callback_val(numero):
        return callback_parse(numero)
    else:
        print('ERROR')
        return validar_input(mensaje, callback_val, callback_parse)
