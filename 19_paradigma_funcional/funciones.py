import json

CODIFICACION = 'utf-8'

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



def escribir_json(ruta: str, informacion: dict):
    with open(ruta, 'w', encoding=CODIFICACION) as json_file:
        json.dump(informacion, json_file, indent=4)
        print(f'Archivo creado con exito en: {ruta}')


def leer_json(ruta: str) -> dict:
    informacion = {}
    with open(ruta, 'r', encoding=CODIFICACION) as json_file:
        informacion = json.load(json_file)
        print('Informacion extraida --')
    return informacion