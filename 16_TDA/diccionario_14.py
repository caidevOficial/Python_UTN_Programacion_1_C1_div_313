from utn_fra_datasets.datasets import lista_diccionario_heroes_small

"""
{ 
    "id": 289, 
    "nombre": "Goku", 
    "identidad": "Desconocido", 
    "alias": "Son-Goku", 
    "inteligencia": 56, 
    "fuerza": 100, 
    "velocidad": 75, 
    "poder": 100, 
    "genero": "Masculino", 
    "raza": "Saiyan", 
    "altura_mts": 1.75, 
    "peso_kg": 62, 
    "color_ojos": "-", 
    "color_pelo": "-", 
    "alineacion": "good", 
    "empresa": "Shueisha" 
}

1 - Determinar cuántos superhéroes tienen cada tipo de color de ojos. 
2 - Determinar cuántos superhéroes tienen cada tipo de color de pelo.

3 - Listar todos los superhéroes agrupados por color de ojos. 
4 - Listar todos los superhéroes agrupados por color de pelo. 
"""

from listas_3 import join_lista_a_texto

def obtener_tipos_caracteristica(lista_heroes: list[dict], clave: str) -> list[str]:
    set_tipos_distintos = set()

    for elemento in lista_heroes:
        set_tipos_distintos.add(elemento.get(clave))
    

    lista_tipos_distintos = list(set_tipos_distintos)
    lista_tipos_distintos.sort()
    
    # print(lista_tipos_distintos)

    return lista_tipos_distintos

def obtener_cantidades_segun_caracteristica(lista_heroes: list[dict], clave: str) -> dict:
    diccionario_info = {}
    tipos_diferentes = obtener_tipos_caracteristica(lista_heroes, clave)

    for tipo in tipos_diferentes:
        diccionario_info[tipo] = 0

        for heroe in lista_heroes:

            tipo_heroe = heroe.get(clave)
            if tipo_heroe == tipo:
                diccionario_info[tipo] += 1
    
            
    return diccionario_info

def obtener_nombres_segun_caracteristica(lista_heroes: list[dict], clave: str) -> dict:
    diccionario_info = {}
    tipos_diferentes = obtener_tipos_caracteristica(lista_heroes, clave)

    for tipo in tipos_diferentes:
        diccionario_info[tipo] = []

        for heroe in lista_heroes:

            tipo_heroe = heroe.get(clave)
            if tipo_heroe == tipo:
                diccionario_info[tipo].append(heroe.get('nombre'))
    
            
    return diccionario_info

def obtener_maximo_caracteres(dict_tipos: dict) -> int:
    cantidad_max = 0

    for clave in dict_tipos.keys():
        if len(clave) > cantidad_max:
            cantidad_max = len(clave)
    return cantidad_max

def mostrar_info_tipos(dict_tipos: dict):
    max_carac = obtener_maximo_caracteres(dict_tipos)
    print('\n|    tipo    | cant |')
    print('-'* (max_carac + 11))
    for tipo, dato in dict_tipos.items():
        if type(dato) == int:
            informacion = f'| {tipo:<{max_carac}} | {dato:4d} |'
        elif type(dato) == list:
            
            limite_max_caract = 50
            cantidad_actual_caract = 0
            indice_maximo = 0
            cant_separadores = 0

            for indice_nombre in range(len(dato)):
                if cantidad_actual_caract + len(dato[indice_nombre]) + cant_separadores <= limite_max_caract:
                    cantidad_actual_caract += len(dato[indice_nombre])
                    indice_maximo = indice_nombre
                    cant_separadores += 1
                else:
                    break

            cantidades = join_lista_a_texto(dato[0:indice_maximo + 1], separador=',')
            # if len(cantidades) > 47:
            #     cantidades = f'{cantidades[:47]}'
            # else:
            #     cantidades = cantidades[:47]
            informacion = f'| {tipo:<{max_carac}} | {cantidades:{limite_max_caract}} |'
        print(informacion)

if __name__ == '__main__':
    # obtener_tipos_caracteristica(lista_diccionario_heroes_small, clave='raza')
    # obtener_tipos_caracteristica(lista_diccionario_heroes_small, clave='empresa')

    # informacion = obtener_cantidades_segun_caracteristica(lista_diccionario_heroes_small, clave='color_ojos')
    # mostrar_info_tipos(informacion)
    # informacion = obtener_cantidades_segun_caracteristica(lista_diccionario_heroes_small, clave='color_pelo')
    # mostrar_info_tipos(informacion)

    informacion = obtener_nombres_segun_caracteristica(lista_diccionario_heroes_small, clave='color_ojos')
    mostrar_info_tipos(informacion)
    # informacion = obtener_nombres_segun_caracteristica(lista_diccionario_heroes_small, clave='color_pelo')
    # mostrar_info_tipos(informacion)