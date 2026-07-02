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

def borrar_salto_linea(dato: str) -> str:
    return dato.replace('\n', '')

def parsear_numeros(datos: list[str]) -> list:
    datos[2] = int(datos[2])
    datos[3] = float(datos[3])
    return datos

def mapear_datos_v3(lista_indices: list[int], lista_dato: list, callback) -> list:
    for indice in lista_indices:
        lista_dato[indice] = callback(lista_dato[indice])
    return lista_dato

def parsear_num_heroes(datos: list[str]) -> list:
    indices_parseos_int = [0,4,5,6,7]
    indices_parseos_flt = [10,11]

    datos = mapear_datos_v3(indices_parseos_int, datos, int)
    datos = mapear_datos_v3(indices_parseos_flt, datos, float)
    
    return datos

def mapear_datos(lista_datos: list[str], callback) -> list[str]:
    datos_mapeados = []
    for index_dato in range(len(lista_datos)):
        dato_mapeado = callback(lista_datos[index_dato])
        datos_mapeados.append(dato_mapeado)
    return datos_mapeados

def crear_diccionario(lista_dato: list, cabeceras: list[str]) -> dict:
    dato = {}
    for clave, valor in zip(cabeceras, lista_dato):
        dato.update({clave: valor})
    return dato

def mapear_datos_v2(matriz_datos: list[list], callback_1, lista_claves):
    lista_dict = []
    for index_dato in range(len(matriz_datos)):
        dato_parseado = callback_1(matriz_datos[index_dato], lista_claves)
        lista_dict.append(dato_parseado)
    return lista_dict

def procesar_dataset_inicial(ruta: str):
    datos = leer_dataset(ruta)
    datos_saneados = mapear_datos(datos, lambda dato: dato.replace('\n', ''))
    claves = datos_saneados.pop(0)
    #LD
    datos_retorno = {
        "claves": split_texto(claves, separador=','),
        "datos_saneados": datos_saneados
    }
    return datos_retorno

def crear_matriz_datos_inicial(matriz_inicial: list[list]):
    matriz_retorno = []
    for indice_dato in range(len(matriz_inicial)):
        fila_saneada = split_texto(matriz_inicial[indice_dato], ',')
        matriz_retorno.append(fila_saneada)
    
    return matriz_retorno
    

def cargar_dataset_sistema(ruta: str, tipo_outuput_dataset: str):
    
    info_ds = procesar_dataset_inicial(ruta)
    dataset = info_ds.get('datos_saneados')
    
    matriz_datos = crear_matriz_datos_inicial(dataset)
    # matriz_mapeada = mapear_datos(matriz_datos, parsear_numeros)

    if tipo_outuput_dataset == 'matrix':
        return matriz_datos
    
    # caso contrario
    datos_saneados_v2 = mapear_datos_v2(matriz_datos, crear_diccionario, info_ds.get('claves'))
    return datos_saneados_v2

def mapear_dato(dato: dict, claves: list[str], callback):
    for clave in claves:
        if clave in dato.keys():
            valor = dato.get(clave)
            dato.update({clave: callback(valor)})

def mapear_ld(datos: list[dict], claves: list[str], callback):

    for dato in datos:
        mapear_dato(dato, claves, callback)

    return datos

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

def es_matriz(datos: list) -> bool:
    matriz = True

    if type(datos) == list:
        for dato in datos:
            if type(dato) != list:
                matriz = False
                break
    return matriz

def crear_info_dataset(cabecera: str, datos: list[dict]):
    info = cabecera

    for dato in datos:
        valores = list(dato.values())
        valores_str = '\n' + join_lista_a_texto(valores, ',')
        info += valores_str
    return info

def crear_informacion_ld(datos: list[dict]) -> str:
    cabecera = join_lista_a_texto(
        list(datos[0].keys()),
        separador=','
    )
    
    info = crear_info_dataset(cabecera, datos)
    
    return info

def crear_informacion_mtx(datos: list[list], cabecera: str) -> str:
    info = cabecera
    for fila in datos:
        fila_str = '\n' + join_lista_a_texto(fila, ',')
        info += fila_str
    return info


def guardar_dataset_csv(datos: list, ruta: str, cabeceras_auto: bool, cabeceras: str = None):
    # determinar si es L-D o M
    if es_matriz(datos) and not cabeceras_auto and cabeceras:
        # Procesar la informacion para guardar en archivo
        informacion = crear_informacion_mtx(datos, cabeceras)
    elif not es_matriz(datos) and cabeceras_auto:
        informacion = crear_informacion_ld(datos)
    else:
        print('El formato de algun parametro es incorrecto.')
        return False

    
    with open(ruta, 'w', encoding=CODIFICACION) as file:
        file.write(informacion)
        print(f'Archivo guardado en {ruta}')
    return True


def guardar_dataset_csv_v2(config: dict):
    if es_matriz(config.get('data')) and not config.get('auto_header') and config.get('header'):
        informacion = crear_informacion_mtx(config.get('data'), config.get('header'))
    elif not es_matriz(config.get('data')) and config.get('auto_header'):
        informacion = crear_informacion_ld(config.get('data'))
    else:
        print('El formato de algun parametro es incorrecto.')
        return False
    
    with open(config.get("path"), 'w', encoding=CODIFICACION) as file:
        file.write(informacion)
        print(f'Archivo guardado en {config.get("path")}')
    return True

def comparar_condicion(pokemon_1: dict, pokemon_2: dict, comparacion: str) -> bool:
    if comparacion == '==':
        return pokemon_1.get('condicion') == pokemon_2.get('condicion')
    elif comparacion == '>':
        return pokemon_1.get('condicion') > pokemon_2.get('condicion')

    return pokemon_1.get('condicion') < pokemon_2.get('condicion')

def comparar_nombre(pokemon_1: dict, pokemon_2: dict, comparacion: str) -> bool:
    if comparacion == '==':
        return pokemon_1.get('nombre') == pokemon_2.get('nombre')
    elif comparacion == '>':
        return pokemon_1.get('nombre') > pokemon_2.get('nombre')

    return pokemon_1.get('nombre') < pokemon_2.get('nombre')

def comparar_atributos(pokemon_1: dict, pokemon_2: dict, clave: str,comparacion: str) -> bool:
    if comparacion == '==':
        return pokemon_1.get(clave) == pokemon_2.get(clave)
    elif comparacion == '>':
        return pokemon_1.get(clave) > pokemon_2.get(clave)

    return pokemon_1.get(clave) < pokemon_2.get(clave)

def do_selection(datos: list[dict], configs: dict):
    datos_copia = datos.copy()
    callback_criterio = configs.get('cbk')
    modo = configs.get('modo')
    largo = len(datos_copia)
    cantidad_atributos = len(configs.get('claves').keys())
    compara_tres = cantidad_atributos == 3
    compara_dos = cantidad_atributos == 2
    claves_comp = configs.get('claves')    


    for indice_a in range(largo - 1):
        indice_elegido = indice_a

        for indice_b in range(indice_a + 1, largo):
            
            if callback_criterio(datos_copia[indice_elegido],datos_copia[indice_b], claves_comp.get('clave_primaria'),'<') and modo == 'DES' or\
               callback_criterio(datos_copia[indice_elegido],datos_copia[indice_b], claves_comp.get('clave_primaria'),'>') and modo == 'ASC' or\
               (compara_dos or compara_tres) and callback_criterio(datos_copia[indice_elegido],datos_copia[indice_b], claves_comp.get('clave_primaria'), '==') and (
                   callback_criterio(datos_copia[indice_elegido],datos_copia[indice_b], claves_comp.get('clave_secundaria'),'<') and modo == 'DES' or\
                   callback_criterio(datos_copia[indice_elegido],datos_copia[indice_b], claves_comp.get('clave_secundaria'),'>') and modo == 'ASC' or\
                   compara_tres and callback_criterio(datos_copia[indice_elegido],datos_copia[indice_b], claves_comp.get('clave_secundaria'), '==') and (
                        callback_criterio(datos_copia[indice_elegido],datos_copia[indice_b], claves_comp.get('clave_terciaria'),'<') and modo == 'DES' or\
                        callback_criterio(datos_copia[indice_elegido],datos_copia[indice_b], claves_comp.get('clave_terciaria'),'>') and modo == 'ASC'
                    )
                ):
                indice_elegido = indice_b

            # if datos_copia[indice_elegido].get('condicion') < datos_copia[indice_b].get('condicion') and modo == 'DES' or\
            #    datos_copia[indice_elegido].get('condicion') > datos_copia[indice_b].get('condicion') and modo == 'ASC' or\
            #    datos_copia[indice_elegido].get('condicion') == datos_copia[indice_b].get('condicion') and\
            #         ((datos_copia[indice_elegido].get('nombre') < datos_copia[indice_b].get('nombre') and modo == 'DES') or
            #          datos_copia[indice_elegido].get('nombre') > datos_copia[indice_b].get('nombre') and modo == 'ASC'):
        

        if indice_elegido != indice_a:
            datos_copia[indice_elegido], datos_copia[indice_a] =\
            datos_copia[indice_a],datos_copia[indice_elegido]
    
    return datos_copia


if __name__ == '__main__':

    from utn_fra_datasets.datasets import lista_dict_pokemones
    configuracion = {
        "cbk": comparar_atributos,
        "modo": 'ASC',
        "claves": {
            "clave_primaria": 'condicion',
            "clave_secundaria": 'tipo',
            "clave_terciaria": 'poder'
        }
    }
    resultado = do_selection(lista_dict_pokemones, configuracion)
    
    # print(lista_dict_pokemones)
    # print()
    print(resultado)