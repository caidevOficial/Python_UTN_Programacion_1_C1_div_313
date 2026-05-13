"""
Mostrar Datos: Debera recorrer las listas y mostrar la info con el siguiente formato: id,nombre,tipo,poder,condición. 

Buscar Pokémons 1: Debera buscar cuales son los pokémons que superen el promedio de poder y mostrar toda su info (usando la funcion del ejercicio 1). 

Filtrar y Ordenar Pokémons: Filtrar Pokémons cuya condicion sea legendarios y ordenarlos de forma “DES” según su poder, luego mostrar su info. 

Buscar Pokémons 2: Buscar los Pokémons que su tipo sea Fuego y mostrar toda su info. 

Mas Poderoso: Buscar al Pokémon con más cantidad de poder y mostrar todos sus datos. 

Obtener Porcentaje: Mostrar un mensaje indicando que porcentaje de Pokémons son legendarios y que porcentaje son normales 

Salir. 
"""

from aplicacion import aplicacion
from utn_fra_datasets.datasets import (
    lista_poke_nombres, lista_poke_ids,
    lista_poke_poderes, lista_poke_tipos,
    lista_poke_condiciones
)

if __name__ == '__main__':
    aplicacion(
        lista_poke_ids, lista_poke_nombres, 
        lista_poke_tipos, lista_poke_poderes, 
        lista_poke_condiciones)