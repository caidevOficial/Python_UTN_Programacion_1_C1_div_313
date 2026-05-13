from matematicas import (
    obtener_promedio,
    obtener_porcentaje
)

def asignar_lista(lista_origen: list) -> list:
    return lista_origen

def mostrar_datos(lista_nombre: list, lista_genero: list, lista_altura: list, lista_peso: list) -> None:

    print('NOMBRE,GENERO,ALTURA,PESO')
    for indice in range(len(lista_nombre)):
        nombre = lista_nombre[indice]
        genero = lista_genero[indice]
        altura = lista_altura[indice]
        peso = lista_peso[indice]

        datos = f'{nombre},{genero},{altura},{peso}'
        print(datos)

def sanear_datos(lista: list) -> None:

    for indice in range(len(lista)):
        lista[indice] = int(lista[indice])

    
    print(lista)

def obtener_indices_que_cumplen(lista: list, valor_limite: float, exactitud: bool = False) -> list:
    lista_indices = []

    for indice in range(len(lista)):
        if lista[indice] <= valor_limite and not exactitud or\
            lista[indice] == valor_limite and exactitud:
            lista_indices.append(indice)
    return lista_indices

def filtrar_elementos(lista_valores: list, lista_indices: list):
    
    lista_valores_filtrados = []

    for indice in lista_indices:
        lista_valores_filtrados.append(lista_valores[indice])
    return lista_valores_filtrados

def buscar_datos_sin_superar_promedio(lista_n: list, lista_g: list, lista_a: list, lista_p: list):
    promedio_a = obtener_promedio(lista_a)
    promedio_p = obtener_promedio(lista_p)

    indices_menos_al_promedio = obtener_indices_que_cumplen(lista_a, promedio_a)

    nombres_filtrados = filtrar_elementos(lista_n, indices_menos_al_promedio)
    generos_filtrados = filtrar_elementos(lista_g, indices_menos_al_promedio)
    alturas_filtrados = filtrar_elementos(lista_a, indices_menos_al_promedio)
    pesos_filtrados = filtrar_elementos(lista_p, indices_menos_al_promedio)

    indices_menos_al_promedio = obtener_indices_que_cumplen(pesos_filtrados, promedio_p)

    nombres_filtrados = filtrar_elementos(nombres_filtrados, indices_menos_al_promedio)
    generos_filtrados = filtrar_elementos(generos_filtrados, indices_menos_al_promedio)
    alturas_filtrados = filtrar_elementos(alturas_filtrados, indices_menos_al_promedio)
    pesos_filtrados = filtrar_elementos(pesos_filtrados, indices_menos_al_promedio)

    print('Personajes que no superen los siguientes valores:')
    print(f'Altura: {promedio_a} CM - Peso: {promedio_p} KG')
    mostrar_datos(nombres_filtrados, generos_filtrados, alturas_filtrados, pesos_filtrados)

def buscar_datos_sin_superar_promedio_v2(lista_n: list, lista_g: list, lista_a: list, lista_p: list):
    promedio_a = obtener_promedio(lista_a)
    promedio_p = obtener_promedio(lista_p)

    lista_n_aux = []
    lista_g_aux = []
    lista_a_aux = []
    lista_p_aux = []

    for indice in range(len(lista_a)):
        if lista_a[indice] <= promedio_a and\
           lista_p[indice] <= promedio_p:
            lista_n_aux.append(lista_n[indice])
            lista_g_aux.append(lista_g[indice])
            lista_a_aux.append(lista_a[indice])
            lista_p_aux.append(lista_p[indice])
    
    mostrar_datos(lista_n_aux, lista_g_aux, lista_a_aux, lista_p_aux)

def actualizar_indice_elegido(lista_comparar: list, indice_inicio: int, tamanio: int, orden: str):
    indice_mas_chico = indice_inicio
    for siguiente_indice in range(indice_inicio + 1, tamanio):
        if lista_comparar[indice_mas_chico] > lista_comparar[siguiente_indice] and orden == 'ASC' or\
            lista_comparar[indice_mas_chico] < lista_comparar[siguiente_indice] and orden == 'DES':
            indice_mas_chico = siguiente_indice
    return indice_mas_chico

def do_selection_sort(lista_importante: list, lista_b: list, lista_c: list, lista_d: list, orden: str = 'ASC') -> list:
    tamanio_lista = len(lista_importante)

    for primer_indice in range(tamanio_lista - 1):

        # indice_mas_chico = primer_indice

        indice_mas_chico = actualizar_indice_elegido(
            lista_importante, primer_indice, 
            tamanio_lista, orden)
        
        if indice_mas_chico != primer_indice:
            auxiliar = lista_importante[indice_mas_chico]
            lista_importante[indice_mas_chico] = lista_importante[primer_indice]
            lista_importante[primer_indice] = auxiliar

            auxiliar = lista_b[indice_mas_chico]
            lista_b[indice_mas_chico] = lista_b[primer_indice]
            lista_b[primer_indice] = auxiliar

            auxiliar = lista_c[indice_mas_chico]
            lista_c[indice_mas_chico] = lista_c[primer_indice]
            lista_c[primer_indice] = auxiliar

            auxiliar = lista_d[indice_mas_chico]
            lista_d[indice_mas_chico] = lista_d[primer_indice]
            lista_d[primer_indice] = auxiliar

def ordenar_por_peso_y_mostrar(lista_n: list, lista_g: list, lista_a: list, lista_p: list) -> None:
    do_selection_sort(lista_p, lista_n, lista_g, lista_a)
    print('Datos ordenados por PESO ASC')
    mostrar_datos(lista_n, lista_g, lista_a, lista_p)

def filtrar_mostrar_na(lista_n: list, lista_g: list, lista_a: list, lista_p: list):
    
    indices_na = obtener_indices_que_cumplen(lista_g, 'n/a', exactitud=True)

    nombres_filtrados = filtrar_elementos(lista_n, indices_na)
    generos_filtrados = filtrar_elementos(lista_g, indices_na)
    alturas_filtrados = filtrar_elementos(lista_a, indices_na)
    pesos_filtrados = filtrar_elementos(lista_p, indices_na)

    print('Personajes que Sean de Genero n/a:')
    mostrar_datos(nombres_filtrados, generos_filtrados, alturas_filtrados, pesos_filtrados)

def obtener_mostrar_porcentajes_por_genero(lista_g: list) -> None:
    generos_buscar = ['female', 'male', 'n/a']
    cantidades_cada_genero = []
    porcentajes_genero = []
    cantidad_total = len(lista_g)

    for genero in generos_buscar:
        indices_generos_encontrados = obtener_indices_que_cumplen(lista_g, genero, exactitud=True)
        cantidad = len(indices_generos_encontrados)
        porcentaje = obtener_porcentaje(cantidad_total, cantidad)
        
        cantidades_cada_genero.append(cantidad)
        porcentajes_genero.append(porcentaje)
    
    info =\
    f"""
    PORCENTAJES POR GÉNERO
    TOTAL PERSONAJES: {cantidad_total}

    {generos_buscar[0]}
    CANTIDAD: {cantidades_cada_genero[0]}
    PORCENTAJE: {porcentajes_genero[0]} %
    
    {generos_buscar[1]}
    CANTIDAD: {cantidades_cada_genero[1]}
    PORCENTAJE: {porcentajes_genero[1]} %
    
    {generos_buscar[2]}
    CANTIDAD: {cantidades_cada_genero[2]}
    PORCENTAJE: {porcentajes_genero[2]} %
    """
    print(info)