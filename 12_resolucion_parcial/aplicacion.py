
import os
from validaciones import validar_input
import manejo_listas as mali

def mostrar_menu():
    texto = """

    1 - Mostrar Datos: Debera recorrer las listas y 
            mostrar la info con el siguiente formato: 
            id,nombre,tipo,poder,condición. 
    2 - Buscar Pokémons 1: Debera buscar cuales son los 
            pokémons que superen el promedio de poder y mostrar 
            toda su info (usando la funcion del ejercicio 1). 
    3 - Filtrar y Ordenar Pokémons: Filtrar Pokémons cuya condicion 
            sea legendarios y ordenarlos de forma “DES” según su poder, 
            luego mostrar su info. 
    4 - Buscar Pokémons 2: Buscar los Pokémons que su tipo sea Fuego y 
            mostrar toda su info. 
    5 - Mas Poderoso: Buscar al Pokémon con más cantidad de poder y 
            mostrar todos sus datos. 
    6 - Obtener Porcentaje: Mostrar un mensaje indicando que porcentaje 
            de Pokémons son legendarios y que porcentaje son normales 
    7 - Salir. 
    """
    print(texto)

def aplicacion(lista_id: list, lista_n: list, lista_t: list, lista_p: list, lista_c: list):
    
    corriendo = True


    while corriendo:
        
        mostrar_menu()
        opcion = validar_input('1', '7')

        match opcion:
            case '1':
                mali.mostrar_info_completa_pokemones(lista_id, lista_n, lista_t, lista_p, lista_c)
            case '2':
                mali.mostrar_pokemones_promedio(lista_id, lista_n, lista_t, lista_p, lista_c)
            case '3':
                mali.mostrar_pokemones_legendarios(lista_id, lista_n, lista_t, lista_p, lista_c)
            case '4':
                mali.mostrar_pokemones_fuego(lista_id, lista_n, lista_t, lista_p, lista_c)
            case '5':
                mali.mostrar_pokemon_mas_fuerte_v1(lista_id, lista_n, lista_t, lista_p, lista_c)
                mali.mostrar_pokemon_mas_fuerte_v2(lista_id, lista_n, lista_t, lista_p, lista_c)
            case '6':
                mali.mostrar_porcentajes_condiciones(lista_c)
            case '7':
                corriendo = False
        os.system('pause')
        os.system('cls') # clear
            