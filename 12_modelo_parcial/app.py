import os
from manejo_listas import (
    asignar_lista, mostrar_datos, sanear_datos, 
    buscar_datos_sin_superar_promedio_v2,
    ordenar_por_peso_y_mostrar, filtrar_mostrar_na,
    obtener_mostrar_porcentajes_por_genero
)
from mensajes import (
    mostrar_menu
)
from validaciones import validar_input


def applicacion(lista_nombre: list, lista_genero: list, lista_altura: list, lista_peso: list) -> None:

    lista_nombres_sw = asignar_lista(lista_nombre)
    lista_generos_sw = asignar_lista(lista_genero)
    lista_alturas_sw = asignar_lista(lista_altura)
    lista_pesos_sw = asignar_lista(lista_peso)

    sanear_datos(lista_alturas_sw)
    sanear_datos(lista_pesos_sw)

    corriendo = True

    while corriendo:

        # mostrar menu y validar datos
        mostrar_menu()
        opcion = validar_input(min='1', max='6')

        match opcion:
            case '1':
                mostrar_datos(lista_nombres_sw, lista_generos_sw, lista_alturas_sw, lista_pesos_sw)
            case '2':
                buscar_datos_sin_superar_promedio_v2(lista_nombres_sw, lista_generos_sw, lista_alturas_sw, lista_pesos_sw)
            case '3':
                ordenar_por_peso_y_mostrar(lista_nombres_sw, lista_generos_sw, lista_alturas_sw, lista_pesos_sw)
            case '4':
                filtrar_mostrar_na(lista_nombres_sw, lista_generos_sw, lista_alturas_sw, lista_pesos_sw)
            case '5':
                obtener_mostrar_porcentajes_por_genero(lista_generos_sw)
            case '6':
                print('Saliendo del progrma')
                corriendo = False
        
        os.system('pause')
        os.system('cls') # UNIX -> clear
