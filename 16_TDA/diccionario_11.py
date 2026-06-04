from utn_fra_datasets.datasets import lista_diccionario_heroes_small

"""
{
    #    "id": 731,
    #    "nombre": "Zoom",
        "identidad": "Desconocido",
        "alias": "No Tiene",
        "inteligencia": 50,
        "fuerza": 10,
        "velocidad": 100,
    #    "poder": 100,
        "genero": "Masculino",
    #    "raza": "-",
        "altura_mts": 1.85,
        "peso_kg": 81,
        "color_ojos": "Red",
        "color_pelo": "Brown",
        "alineacion": "bad",
        "empresa": "DC Comics"
    }
"""

lista_heroes_texto = []
lista_heroes_num = []

for heroe in lista_diccionario_heroes_small:

    nuevos_datos_str = {
        "id": heroe.get('id'),
        "nombre": heroe.get('nombre'),
        "identidad": heroe.get('identidad'),
        "alias": heroe.get('alias'),
        "genero": heroe.get('genero'),
        "raza": heroe.get('raza'),
        "color_ojos": heroe.get('color_ojos'),
        "color_pelo": heroe.get('color_pelo'),
        "alineacion": heroe.get('alineacion'),
        "empresa": heroe.get('empresa')
    }

    nuevos_datos_int = {
        "id": heroe.get('id'),
        "inteligencia": heroe.get('inteligencia'),
        "fuerza": heroe.get('fuerza'),
        "velocidad": heroe.get('velocidad'),
        "poder": heroe.get('poder'),
        "altura_mts": heroe.get('altura_mts'),
        "peso_kg": heroe.get('peso_kg')
    }

    lista_heroes_texto.append(nuevos_datos_str)
    lista_heroes_num.append(nuevos_datos_int)

# for heroe_str, heroe_num in zip(lista_heroes_texto, lista_heroes_num):
#     print(heroe_str, heroe_num, sep='\n')


def buscar_datos_por_id(lista_busqueda: list[dict], clave_busqueda: str, id_abuscar: int) -> dict:
    dato_encontrado = {}

    for dato_dict in lista_busqueda:
        if dato_dict.get(clave_busqueda) == id_abuscar:
            dato_encontrado = dato_dict
            break

    return dato_encontrado


# for elemento_num in lista_heroes_num:

#     id_buscar = elemento_num.get('id')
#     elem_encontrado = buscar_datos_por_id(lista_heroes_texto, 'id', id_buscar)
#     elemento_num.update(elem_encontrado)
#     print(elemento_num)