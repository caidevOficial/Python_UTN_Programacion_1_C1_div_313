
def do_selection_sort(lista_1: list, lista_2: list, lista_3: list, orden: str = 'ASC') -> None:
    tamanio_lista = len(lista_1)

    for primer_indice in range(tamanio_lista - 1):

        indice_mas_chico = primer_indice

        for siguiente_indice in range(primer_indice + 1, tamanio_lista):

            if lista_1[indice_mas_chico] > lista_1[siguiente_indice] and orden == 'ASC' or\
               lista_1[indice_mas_chico] < lista_1[siguiente_indice] and orden == 'DES':
                indice_mas_chico = siguiente_indice
        
        if indice_mas_chico != primer_indice:
            auxiliar = lista_1[indice_mas_chico]
            lista_1[indice_mas_chico] = lista_1[primer_indice]
            lista_1[primer_indice] = auxiliar

            auxiliar_2 = lista_2[indice_mas_chico]
            lista_2[indice_mas_chico] = lista_2[primer_indice]
            lista_2[primer_indice] = auxiliar_2

            auxiliar_3 = lista_3[indice_mas_chico]
            lista_3[indice_mas_chico] = lista_3[primer_indice]
            lista_3[primer_indice] = auxiliar_3

lista_nombres = [
    "Pepe", "Moni", "Susana"
]
lista_edades = [
    56, 45, 70
]
lista_localidad = [
    "Bajo Flores", "Bajo Flores", "Uruguay"
]

running = True
while running:

    print('1 - Ingresar 3 datos\n2 - mostrar datos\n3 - Salir')
    opcion = input('ingrese su opcion: ')

    match opcion:
        case '1':
            for vuelta in range(3):
                nombre = input(f'ingrese el nombre de la {vuelta + 1}° persona: ')
                edad = input(f'ingrese la edad de la {vuelta + 1}° persona: ')
                localidad = input(f'ingrese la localidad de la {vuelta + 1}° persona: ')

                lista_nombres.append(nombre)
                lista_edades.append(edad)
                lista_localidad.append(localidad)

        case '2':

            tipo_orden = input('Ordenar por: nombre, edad, ciudad: ')
            modo = input('Ordenar por ASC - DES: ')

            if tipo_orden == 'nombre':
                do_selection_sort(lista_nombres, lista_localidad, lista_edades, modo)
            elif tipo_orden == 'edad':
                do_selection_sort(lista_edades, lista_localidad, lista_nombres, modo)
            else:
                do_selection_sort(lista_localidad, lista_edades, lista_nombres, modo)

            for indice in range(len(lista_edades)):
                info_persona = f'{lista_nombres[indice]} - {lista_edades[indice]} - {lista_localidad[indice]}'
                print(info_persona)

        case '3':
            running = False